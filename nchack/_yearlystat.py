from ._cleanup import cleanup
from ._runthis import run_this

def yearlystat(self, stat = "mean", silent = True, cores = 1):
    """Function to calculate the seasonal statistic from a function""" 

    cdo_command = "cdo -year" + stat

    run_this(cdo_command, self, silent, output = "ensemble", cores = cores)

    # clean up the directory
    cleanup(keep = self.current)

    

def yearly_mean(self, silent = True, cores = 1):
    return yearlystat(self, stat = "mean", silent = True, cores = cores)

def yearly_min(self, silent = True, cores = 1):
    return yearlystat(self, stat = "min", silent = True, cores = cores)

def yearly_max(self, silent = True, cores = 1):
    return yearlystat(self, stat = "max", silent = True, cores = cores)
    
def yearly_range(self, silent = True, cores = 1):
    return yearlystat(self, stat = "range", silent = True, cores = cores)
