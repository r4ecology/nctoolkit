import unittest
import nchack as nc
import pandas as pd
import xarray as xr
import os


ff = "data/sst.mon.mean.nc"

class TestSelect(unittest.TestCase):

    def test_mean(self):
        tracker = nc.open_data(ff)
        tracker.select_years(range(1990, 1999))
        tracker.select_months(1)
        tracker.mean()
        x = tracker.to_dataframe().sst.values[0].astype("float")

        tracker = nc.open_data(ff)
        tracker.select_years(range(1990, 1999))
        tracker.monthly_mean_climatology()
        tracker.select_months(1)
        y = tracker.to_dataframe().sst.values[0].astype("float")

        self.assertEqual(x,  y)


    def test_min(self):
        tracker = nc.open_data(ff)
        tracker.select_years(range(1990, 1999))
        tracker.select_months(1)
        tracker.min()
        x = tracker.to_dataframe().sst.values[0].astype("float")

        tracker = nc.open_data(ff)
        tracker.select_years(range(1990, 1999))
        tracker.monthly_min_climatology()
        tracker.select_months(1)
        y = tracker.to_dataframe().sst.values[0].astype("float")

        self.assertEqual(x,  y)


    def test_max(self):
        tracker = nc.open_data(ff)
        tracker.select_years(range(1990, 1999))
        tracker.select_months(1)
        tracker.max()
        x = tracker.to_dataframe().sst.values[0].astype("float")

        tracker = nc.open_data(ff)
        tracker.select_years(range(1990, 1999))
        tracker.monthly_max_climatology()
        tracker.select_months(1)
        y = tracker.to_dataframe().sst.values[0].astype("float")

        self.assertEqual(x,  y)

    def test_range(self):
        tracker = nc.open_data(ff)
        tracker.select_years(range(1990, 1999))
        tracker.select_months(1)
        tracker.range()
        x = tracker.to_dataframe().sst.values[0].astype("float")

        tracker = nc.open_data(ff)
        tracker.select_years(range(1990, 1999))
        tracker.monthly_range_climatology()
        tracker.select_months(1)
        y = tracker.to_dataframe().sst.values[0].astype("float")

        self.assertEqual(x,  y)

if __name__ == '__main__':
    unittest.main()

