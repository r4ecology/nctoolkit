
from .flatten import str_flatten
from ._cleanup import cleanup
from ._runthis import run_this

def remove_variables(self, vars, cores = 1):
    """
    Remove variables from tracker 

    Parameters
    -------------
    vars : str or list
        Variable or variables to be removed from the tracker
    cores: int
        Number of cores to use if files are processed in parallel. Defaults to non-parallel operation 

    Returns
    -------------
    nchack.NCData
        Reduced tracker without the listed variables
    """

    if type(vars) is not list:
        vars = [vars]

    vars = str_flatten(vars, ",")
    
    cdo_command = "cdo -delete,name=" + vars
    run_this(cdo_command, self, output = "ensemble", cores = cores)
    
    cleanup(keep = self.current)
    
