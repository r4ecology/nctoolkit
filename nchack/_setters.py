# todo:
    # add checker for date validity

import os
import tempfile

from ._filetracker import nc_created
from ._cleanup import cleanup
from ._runthis import run_this


def set_date(self, year, month, day, base_year = 1900, silent = True):
    """Function to set the date"""

    # check that the values supplied are valid
    # This will convert things to ints, and if it can't be done, throw an error
    if type(year) is not int:
        year = float(year)
    if type(month) is not int:
        month = float(month)

    if type(day) is not int:
        day = float(day)
    cdo_command = "cdo -setreftime," + str(base_year) + "-01-01 -setdate," + str(year) + "-" + str(month) + "-" + str(day)

    run_this(cdo_command, self, silent, output = "ensemble")

    # clean up the directory
    cleanup(keep = self.current)

#    return self

def set_longname(self, var, new_long, silent = True):
    """Function to set the date"""

    # Check that the unit supplied is a string
    if type(new_long) is not str:
        ValueError("new_lon supplied is not a string")

    if type(new_long) is not str:
        ValueError("Only works with single vars currently")

    if type(self.current) is not str:
        ValueError("Method does not yet work with ensembles")

    if self.run == False:
        ValueError("NCO methods do not work in hold mode")

    target = tempfile.NamedTemporaryFile().name + ".nc"
    nc_created.append(target)

    nco_command = "ncatted -a long_name," + var + ",o,c,'" + new_long + "' " + self.current + " " + target
    self.history.append(nco_command)

    os.system(nco_command)

    if os.path.exists(target) == False:
        raise ValueError(nco_command + " was not successful. Check output")
    self.current = target


    # clean up the directory
    cleanup(keep = self.current)

#    return self


def set_missing(self, value, silent = True, cores = 1):
    """Function to set the missing values"""
    """This is either a range or a single value"""

    if type(value) is int:
        value = float(value)

    if type(value) is float:
        cdo_command = "cdo setctomiss," + str(value)
    if type(value) is list:
        cdo_command = "cdo setrtomiss," + str(value[0]) + "," + str(value[1])

    run_this(cdo_command, self, silent, output = "ensemble", cores = cores)

    # clean up the directory
    cleanup(keep = self.current)

#    return self


def set_unit(self, unit, silent = True):
    """Function to set the date"""

    # Check that the unit supplied is a string
    if type(unit) is not str:
        ValueError("Unit supplied is not a string")

    cdo_command = "cdo -setunit,'" + unit +"'"

    run_this(cdo_command, self, silent, output = "ensemble")

    # clean up the directory
    cleanup(keep = self.current)

#    return self