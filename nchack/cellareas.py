import copy
from .runthis import run_this
from .runthis import tidy_command
from .runthis import run_cdo
from .temp_file import temp_file
from .cleanup import cleanup
from .cleanup import disk_clean
from .session import nc_safe
from .show import nc_variables


def cell_areas(self, join=True):
    """
    Calculate the cell areas in square meters

    Parameters
    -------------
    join: boolean
        Set to False if you only want the cell areas to be in the output. join=True adds the areas as a variable to the dataset.
    """

    if isinstance(join, bool) == False:
        raise TypeError("join is not boolean")

    # release if you need to join the cell areas to the original file
    if join:
        self.run()

    # first run the join case
    if join:

        new_files = []
        new_commands = []

        for ff in self:

            if "cell_area" in nc_variables(ff):
                raise ValueError("cell_area is already a variable")

            target = temp_file(".nc")

            cdo_command = f"cdo -merge {ff} -gridarea {ff} {target}"
            cdo_command = tidy_command(cdo_command)
            target = run_cdo(cdo_command, target)
            new_files.append(target)

            new_commands.append(cdo_command)

        for x in new_commands:
            self.history.append(x)

        self.current = new_files

        self._hold_history = copy.deepcopy(self.history)

        cleanup()

    else:

        cdo_command = "-gridarea"
        run_this(cdo_command, self, output="ensemble")

    # add units

    self.set_units({"cell_area": "m^2"})

    if join:
        self.run()
        self.disk_clean()
