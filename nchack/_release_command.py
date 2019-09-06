
import os
import tempfile
import copy

from ._cleanup import cleanup
from ._filetracker import nc_created
from ._runthis import run_this

def release_command(self):
    """Method to print release commands"""
    # the first step is to set the run status to true
    if self.run:
        return("Warning: tracker is in run mode. Nothing to release")

    if self.run == False:
        self.run = True
        read = os.popen("cdo --operators").read()
        cdo_methods = [x.split(" ")[0] for x in read.split("\n")]
        cdo_methods = [mm for mm in cdo_methods if len(mm) > 0]
        
        pre_history = copy.deepcopy(self.hold_history)
        
        the_history = copy.deepcopy(self.history)
        
        the_history = the_history[len(pre_history):len(the_history)]

        # first, thing to check is whether all of the calls are to cdo
        if len([f for f in the_history if f.startswith("cdo") == False]) > 0:
            raise ValueError("Not all of the calls are to cdo. Exiting!")
        
        # we need to reverse the history so that the commands are in the correct order for chaining
        the_history.reverse()

        # now, pull all of the history together into one string
        # We can then tweak that
        
        the_history = "  ".join(the_history)
        # First, get rid of any mention of cdo
        the_history = the_history.replace("cdo ", "").replace("  ", " ")
        the_history = the_history.split(" ")
        # Now, we need to remove any files from the history
        # This should probably be removed, as it should not do anything...
        
        the_history = [f for f in the_history if ("," not in f and f.endswith(".nc")) == False]
        the_history = " ".join(the_history)
        the_history = " " + the_history
        # now, the cdo methods need to have a - in front of them
        
        for mm in cdo_methods:
            old_history = the_history
            the_history = the_history.replace(" " + mm, " -"+mm)

        cdo_command = "cdo " + the_history

        cdo_command = cdo_command.replace("  ", " ")

        # OK. We might have reduced dimensions at one point. This needs to be handled.
        if "--reduce_dim" in cdo_command:
            cdo_command = cdo_command.replace("--reduce_dim", "")
            cdo_command = cdo_command.replace("cdo","cdo --reduce_dim")

        cdo_command = cdo_command.replace("cdo","cdo -L ")
        cdo_command = cdo_command.replace("  ", " ")
#        cdo_command = cdo_command.replace("cdo ", "")

        return cdo_command
