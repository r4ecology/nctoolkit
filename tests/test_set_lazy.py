import nctoolkit as nc

nc.options(lazy=True)
import pandas as pd
import xarray as xr
import os, pytest


import subprocess


def cdo_version():
    cdo_check = subprocess.run(
        "cdo --version", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    cdo_check = str(cdo_check.stderr).replace("\\n", "")
    cdo_check = cdo_check.replace("b'", "").strip()
    return cdo_check.split("(")[0].strip().split(" ")[-1]


ff = "data/sst.mon.mean.nc"


class TestSetters:
    def test_empty(self):
        n = len(nc.session_files())
        assert n == 0

    def test_setdate(self):

        # do not run this test with cdo version 1.9.3 as there is a bug
        if cdo_version() not in ["1.9.3"]:
            tracker = nc.open_data(ff)
            tracker.select_years(list(range(1970, 1971)))
            tracker.select_months([1])
            tracker.set_date(year=1990, month=1, day=1)
            tracker.run()
            x = tracker.years[0]

            assert x == 1990

            y = tracker.months[0]

            assert y == 1
            n = len(nc.session_files())
            assert n == 1

    def test_setdate2(self):
        if cdo_version() not in ["1.9.3"]:
            tracker = nc.open_data(ff)
            tracker.select_years(list(range(1970, 1971)))
            tracker.select_months([1])
            tracker.set_date(year=1990, month=1, day=1)
            tracker.run()
            x = tracker.years[0]

            assert x == 1990

            y = tracker.months[0]

            assert y == 1
            n = len(nc.session_files())
            assert n == 1

    def test_setdate3(self):
        if cdo_version() not in ["1.9.3"]:
            tracker = nc.open_data(ff)
            tracker.select_years(list(range(1970, 1971)))
            tracker.select_months([1])
            tracker.set_date(year=1990, month=3, day=1)
            tracker.run()
            x = tracker.years[0]

            assert x == 1990

            y = tracker.months[0]
            assert y == 3

            n = len(nc.session_files())
            assert n == 1

    def test_setmissing(self):
        tracker = nc.open_data(ff)
        tracker.select_years(1990)
        tracker.select_months([1])

        tracker.set_missing([0, 1000])
        tracker.spatial_mean()
        tracker.run()
        x = tracker.to_dataframe().sst.values[0]

        assert x == -1.2176581621170044444
        n = len(nc.session_files())
        assert n == 1

    def test_setmissing2(self):
        tracker = nc.open_data(ff)
        tracker.set_missing([100, 100])
        x = tracker.history

        tracker = nc.open_data(ff)
        tracker.set_missing(100)
        y = tracker.history

    def test_setunits(self):
        tracker = nc.open_data(ff)
        tracker.select_years(1990)
        tracker.select_months([1])

        tracker.set_units({"sst": "C"})
        tracker.run()
        x = tracker.variables_detailed.units[0]

        assert x == "C"
        n = len(nc.session_files())
        assert n == 1

    def test_setmissing3(self):
        tracker = nc.open_data(ff)
        with pytest.raises(TypeError):
            tracker.set_missing("x")

        with pytest.raises(ValueError):
            tracker.set_date()

        with pytest.raises(ValueError):
            tracker.set_date(year=1990)

        with pytest.raises(ValueError):
            tracker.set_date(year=1990, month=1)

        with pytest.raises(ValueError):
            tracker.set_date(year=1990, month=1)

        with pytest.raises(ValueError):
            tracker.set_missing()

        with pytest.raises(ValueError):
            tracker.set_units()

        with pytest.raises(TypeError):
            tracker.set_units({"x": 1})

        with pytest.raises(TypeError):
            tracker.set_units({1: 1})

        with pytest.raises(ValueError):
            tracker.set_longnames()

        with pytest.raises(TypeError):
            tracker.set_longnames({"x": 1})

        with pytest.raises(TypeError):
            tracker.set_longnames({1: 1})

        with pytest.raises(TypeError):
            tracker.set_date(year=1990, month="x", day=1)

        with pytest.raises(TypeError):
            tracker.set_date(year="x", month="x", day=1)

        with pytest.raises(TypeError):
            tracker.set_date(year=1, month=1, day="x")

        with pytest.raises(TypeError):
            tracker.set_missing([1, "x"])

        n = len(nc.session_files())
        assert n == 0

    def test_setunits2(self):
        tracker = nc.open_data(ff)
        with pytest.raises(TypeError):
            tracker.set_units("x")
            n = len(nc.session_files())
            assert n == 0

    def test_longname_error(self):
        tracker = nc.open_data(ff)
        with pytest.raises(TypeError):
            tracker.set_longnames("x")
            n = len(nc.session_files())
            assert n == 0

    def test_setlongnames(self):
        tracker = nc.open_data(ff)
        tracker.select_years(1990)
        tracker.select_months([1])

        tracker.set_longnames({"sst": "temp"})
        tracker.run()
        x = tracker.variables_detailed.long_name[0]

        assert x == "temp"
        n = len(nc.session_files())
        assert n == 1

    def test_setlongnames2(self):
        tracker = nc.open_data(ff)
        tracker.select_years(1990)
        tracker.split("yearmonth")

        tracker.set_longnames({"sst": "temp"})
        tracker.merge_time()
        tracker.run()

        x = tracker.variables_detailed.long_name[0]

        assert x == "temp"
        n = len(nc.session_files())
        assert n == 1
