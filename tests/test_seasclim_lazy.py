import nctoolkit as nc

nc.options(lazy=True)
import pandas as pd
import xarray as xr
import os, pytest


class TestSeasclim:
    def test_empty(self):
        n = len(nc.session_files())
        assert n == 0

    def test_mean(self):
        ff = "data/sst.mon.mean.nc"
        tracker = nc.open_data(ff)
        tracker.seasonal_mean_climatology()
        tracker.select_seasons("DJF")
        tracker.spatial_mean()

        x = tracker.to_dataframe().sst.values[0]

        tracker = nc.open_data(ff)
        tracker.select_seasons("DJF")
        tracker.tmean()
        tracker.spatial_mean()
        y = tracker.to_dataframe().sst.values[0]

        assert x == y
        n = len(nc.session_files())
        assert n == 1

    def test_max(self):
        ff = "data/sst.mon.mean.nc"
        tracker = nc.open_data(ff)
        tracker.seasonal_max_climatology()
        tracker.select_seasons("DJF")
        tracker.spatial_mean()

        x = tracker.to_dataframe().sst.values[0]

        tracker = nc.open_data(ff)
        tracker.select_seasons("DJF")
        tracker.tmax()
        tracker.spatial_mean()
        y = tracker.to_dataframe().sst.values[0]

        assert x == y
        n = len(nc.session_files())
        assert n == 1

    def test_min(self):
        ff = "data/sst.mon.mean.nc"
        tracker = nc.open_data(ff)
        tracker.seasonal_min_climatology()
        tracker.select_seasons("DJF")
        tracker.spatial_mean()

        x = tracker.to_dataframe().sst.values[0]

        tracker = nc.open_data(ff)
        tracker.select_seasons("DJF")
        tracker.tmin()
        tracker.spatial_mean()
        y = tracker.to_dataframe().sst.values[0]

        assert x == y
        n = len(nc.session_files())
        assert n == 1

    def test_range(self):
        ff = "data/sst.mon.mean.nc"
        tracker = nc.open_data(ff)
        tracker.seasonal_range_climatology()
        tracker.select_seasons("DJF")
        tracker.spatial_mean()

        x = tracker.to_dataframe().sst.values[0]

        tracker = nc.open_data(ff)
        tracker.select_seasons("DJF")
        tracker.trange()
        tracker.spatial_mean()
        y = tracker.to_dataframe().sst.values[0]

        assert x == y
        n = len(nc.session_files())
        assert n == 1
