# todo:
    # add checker for date validity

import os

from ._temp_file import temp_file
from ._session import nc_safe
from ._cleanup import cleanup
from ._runthis import run_this
from ._runthis import run_nco


def set_date(self, year, month, day, base_year = 1900):

    """
    Set the date in a dataset
    You should only do this if you have to fix/change a dataset with a single, not multiple dates. 

    Parameters
    -------------
    year : int 
        The year
    month : int 
        The month
    day : int 
        The day
    base_year : int
        The base year for time creation in the netcdf. Defaults to 1900.
    cores: int
        Number of cores to use if files are processed in parallel. Defaults to non-parallel operation 

    """

    # check that the values supplied are valid
    # This will convert things to ints, and if it can't be done, throw an error
    if type(year) is not int:
        year = float(year)
    if type(month) is not int:
        month = float(month)

    if type(day) is not int:
        day = float(day)
    cdo_command = "cdo -L -setreftime," + str(base_year) + "-01-01 -setdate," + str(year) + "-" + str(month) + "-" + str(day)

    run_this(cdo_command, self,  output = "ensemble")



def set_missing(self, value,  cores = 1):
    """
    Set the missing value for a single number or a range

    Parameters
    -------------
    value : int or list
        IIf int is supplied, this will be converted to a missing value. If a two variable list is supplied this will used for the range to to apply missing values to. 
    cores: int
        Number of cores to use if files are processed in parallel. Defaults to non-parallel operation 

    """

    if type(value) is int:
        value = float(value)

    if type(value) is float:
        cdo_command = "cdo -setctomiss," + str(value)
    if type(value) is list:
        cdo_command = "cdo -setrtomiss," + str(value[0]) + "," + str(value[1])

    run_this(cdo_command, self,  output = "ensemble", cores = cores)

    # clean up the directory
    cleanup(keep = self.current)


def set_units(self, var_dict):
    """
    Set the units for variables 

    Parameters
    -------------
    var_dict : dict
        A dictionary where the key, value pair are the variables and new units respectively.

    """


    # Check that a dictionary has been supplied
    if type(var_dict) is not dict:
        ValueError("A dictionary has not been supplied!")
    
    # change the units in turn. This doesn't seem to be something you can chain?
    for i in var_dict:
        cdo_command = ""
        cdo_command = cdo_command + " -setattribute," + i + "@units=" + '"' + var_dict[i]  + '"'
        cdo_command = "cdo " + cdo_command 
        run_this(cdo_command, self,  output = "ensemble")



def set_gridtype(self, grid):
    """
    Set the grid type. Only use this if, for example, the grid is "generic" when it should be lonlat. 

    Parameters
    -------------
    grid : str
        Grid type. Needs to be one of "curvilinear", "unstructured", "dereference", "regular", "regularnn" or "lonlat".

    """


    # check that the values supplied are valid
    # This will convert things to ints, and if it can't be done, throw an error

    if grid not in ["curvilinear", "unstructured", "dereference", "regular", "regularnn", "lonlat"]:
            raise ValueError("Grid type supplies is not supported")

    cdo_command = "cdo -setgridtype," + grid

    run_this(cdo_command, self,  output = "ensemble") 



def set_attributes(self, att_dict):
    """
    Set Global attributes 

    Parameters
    -------------
    att_dict : dict
        Dictionary with key, value pairs representing the attribute names and their long names

    """

    if self.run == False:
        ValueError("NCO methods do not work in hold mode")

    if type(self.current) is not str:
        ValueError("Method does not yet work with ensembles")

    if type(att_dict) is not dict:
        ValueError("A dictionary has not been supplied!")
    
    # change the units in turn. This doesn't seem to be something you can chain?

    nco_command = "ncatted -O -h "
    for i in att_dict:
        nco_command += "-a authors,global,o,c,'" + att_dict[i]+ "' "

    target = ""
    if type(self.start) is list:
        target = "" 
    else:
        if self.start == self.current:
            target = temp_file("nc") 

    nco_command+= self.current + " " + target

    target = run_nco(nco_command, target)

    if target != "":
        nc_safe.remove(self.current)
        self.current = target
        nc_safe.append(self.current)

    # clean up the directory
    if self.run:
        cleanup(keep = self.current)

    self.history.append(nco_command)




def set_longnames(self, var_dict):
    """
    Set Global attributes 

    Parameters
    -------------
    var_dict : dict
        Dictionary with key, value pairs representing the attribute names and their long names

    """

    if self.run == False:
        ValueError("NCO methods do not work in hold mode")

    if type(self.current) is not str:
        ValueError("Method does not yet work with ensembles")

    if type(var_dict) is not dict:
        ValueError("A dictionary has not been supplied!")
    
    # change the units in turn. This doesn't seem to be something you can chain?

    nco_command = "ncatted "
    for i in var_dict:
        nco_command += "-a long_name," + i + ",o,c,'" + var_dict[i]+ "' "

    target = ""
    if type(self.start) is list:
        target = "" 
    else:
        if self.start == self.current:
            target = temp_file("nc") 

    nco_command+= self.current + " " + target

    target = run_nco(nco_command, target)


    if target != "":
        nc_safe.remove(self.current)
        self.current = target
        nc_safe.append(self.current)

    # clean up the directory
    if self.run:
        cleanup(keep = self.current)

    self.history.append(nco_command)







def assign_coords(self, lon_name = None, lat_name = None):
    """
    Assign coordinates to variables 

    Parameters
    -------------
    lon_name : str
        Name of the longitude dimension
    lat_name : str
        Name of the latitude dimension
    """

    # add grid number check

    if self.run == False:
        ValueError("NCO methods do not work in hold mode")

    if type(lon_name) is not str:
        ValueError("Method does not yet work with ensembles")

    if type(lat_name) is not str:
        ValueError("Method does not yet work with ensembles")
    
    # change the units in turn. This doesn't seem to be something you can chain?

    variables = self.variables 

    nco_command = "ncatted "

    for vv in variables:
        nco_command += "-a coordinates,"+ vv + ",c,c,'" + lon_name + " " + lat_name + "' "

    target = ""
    if type(self.start) is list:
        target = "" 
    else:
        if self.start == self.current:
            target = temp_file("nc") 

    nco_command+= self.current + " " + target

    print(nco_command)
    return None

    target = run_nco(nco_command, target)

    if target != "":
        nc_safe.remove(self.current)
        self.current = target
        nc_safe.append(self.current)

    # clean up the directory
    if self.run:
        cleanup(keep = self.current)

    self.history.append(nco_command)








