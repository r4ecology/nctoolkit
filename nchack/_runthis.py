import os
import copy
import tempfile
import multiprocessing

from ._filetracker import nc_created
from .flatten import str_flatten

def run_it(command, target):
    os.system(command)
    if os.path.exists(target) == False:
        raise ValueError(command + " was not successful. Check output")
    return target

def run_this(os_command, self, silent = False, output = "one", cores = 1):
    """ Function to run an nco/cdo system command and check output was generated"""
    # Works on multiple files
    run = self.run
    # Step one

    # Step 2: run the system command
    
    if run == False:
        self.history.append(os_command)

    if run:

        if type(self.current) is str:
            # single file case
            if silent:
                os_command = os_command.replace("cdo ", "cdo -s ")

            target = tempfile.NamedTemporaryFile().name + ".nc"
            nc_created.append(target)
            os_command = os_command + " " + self.current + " " + target

            run_history = [x for x in self.history if x.endswith(".nc")]
            self.history = copy.deepcopy(run_history)
            self.history.append(os_command)

            os.system(os_command)
            
            # check the file was actually created
            # Raise error if it wasn't

            if os.path.exists(target) == False:
                raise ValueError(os_command + " was not successful. Check output")
            self.current = target
        else:
            # multiple file case

            if output == "one":
                if silent:
                    ff_command = os_command.replace("cdo ", "cdo -s ")
                else:
                    ff_command = copy.deepcopy(os_command)

                target = tempfile.NamedTemporaryFile().name + ".nc"
                nc_created.append(target)
                flat_ensemble = str_flatten(self.current, " ")
                ff_command = ff_command + " " + flat_ensemble + " " + target

                run_history = copy.deepcopy(self.history)
                run_history = [x for x in run_history if x.endswith(".nc")]
                self.history = copy.deepcopy(run_history)
                self.history.append(ff_command)
                os.system(ff_command)
                
                # check the file was actually created
                # Raise error if it wasn't

                if os.path.exists(target) == False:
                    raise ValueError(ff_command + " was not successful. Check output")
                self.current = target

            else:
                if cores == 1:
                    target_list = []
                    for ff in self.current:
                    
                        if silent:
                            ff_command = os_command.replace("cdo ", "cdo -s ")
                        else:
                            ff_command = copy.deepcopy(os_command)

                        target = tempfile.NamedTemporaryFile().name + ".nc"
                        nc_created.append(target)
                        ff_command = ff_command + " " + ff + " " + target

                        self.history.append(ff_command)
                        os.system(ff_command)
                        
                        # check the file was actually created
                        # Raise error if it wasn't

                        if os.path.exists(target) == False:
                            raise ValueError(ff_command + " was not successful. Check output")
                        target_list.append(target) 

                    self.current = copy.deepcopy(target_list)

                else:
                # multi-core case

                    pool = multiprocessing.Pool(cores)
                    target_list = []
                    results = dict()
                    for ff in self.current:
                    
                        if silent:
                            ff_command = os_command.replace("cdo ", "cdo -s ")
                        else:
                            ff_command = copy.deepcopy(os_command)

                        target = tempfile.NamedTemporaryFile().name + ".nc"
                        nc_created.append(target)
                        ff_command = ff_command + " " + ff + " " + target

                        self.history.append(ff_command)
                        temp = pool.apply_async(run_it,[ff_command, target])
                        results[ff] = temp 

                    pool.close()
                    pool.join()
                    new_current = []
                    for k,v in results.items():
                        target_list.append(v.get())

                    self.current = copy.deepcopy(target_list)




    else:
        # Now, if this is not a cdo command we need throw an error

        if os_command.strip().startswith("cdo") == False:
            raise ValueError("You can only use cdo commands in hold mode")
        # Now, we need to throw an error if the command is generating a grid
        
        commas = [x for x in os_command.split(" ") if "," in x]
        commas = "".join(commas)
        if "gen" in commas:
            raise ValueError("You cannot generate weights as part of a chain!")



