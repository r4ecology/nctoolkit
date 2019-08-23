
import xarray as xr
import pandas as pd
import numpy as np
import os
import tempfile
import itertools

from .flatten import str_flatten
from ._cleanup import cleanup
from ._filetracker import nc_created
from ._runcommand import run_command


def select_variables(self, vars = None, silent = True):

    self.target  = tempfile.NamedTemporaryFile().name + ".nc"
    nc_created.append(self.target)
    
    if type(vars) is str:
        vars_list = [vars]
    else:
        vars_list = vars
    vars_list = str_flatten(vars_list, ",")
    
    cdo_command = "cdo selname," + vars_list + " " + self.current + " " + self.target
    self.history.append(cdo_command)
    run_command(cdo_command, self, silent)
    
    if self.run: self.current = self.target 
    
    cleanup(keep = self.current)
    
    return(self)
