import nctoolkit as nc

nc.options(lazy=True)
import pandas as pd
import xarray as xr
import numpy as np
import os, pytest


ff = "data/sst.mon.mean.nc"
ff1 = "data/2003.nc"
ff2 = "data/2004.nc"


class TestAppend:
    def test_append(self):
        new = nc.open_data(ff)
        new.mutate({"tos": "sst+273.15"})
        new.append(ff)

        assert len(new.current) == 2

        new = nc.open_data(ff)

        with pytest.raises(ValueError):
            new.append(ff)

        with pytest.raises(ValueError):
            new.append("xyz")

        new = nc.open_data(ff)
        with pytest.raises(TypeError):
            new.append()

        del new
        n = len(nc.session_files())
        assert n == 0

        new = nc.open_data(ff)
        with pytest.warns(UserWarning):
            new.append([ff1, ff1])

        new = nc.open_data([ff1, ff2])

        with pytest.raises(ValueError):
            new.append(ff1)

        new.append(ff)

        assert new.current == [ff1, ff2, ff]
