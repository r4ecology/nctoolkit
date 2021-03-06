.. currentmodule:: nctoolkit


####################
API Reference
####################

Session options
------------------

.. autosummary::
   :toctree: generated/

   options


Reading/copying data
------------------

.. autosummary::
   :toctree: generated/

   open_data
   open_url
   open_thredds
   DataSet.copy

Merging or analyzing multiple datasets
------------------

.. autosummary::
   :toctree: generated/

    merge
    cor_time
    cor_space
    

Adding file(s) to a dataset
------------------

.. autosummary::
   :toctree: generated/

    append

Accessing attributes
------------------

.. autosummary::
   :toctree: generated/

   DataSet.variables
   DataSet.years
   DataSet.months
   DataSet.times
   DataSet.levels
   DataSet.size
   DataSet.current
   DataSet.history
   DataSet.start

Plotting
------------------

.. autosummary::
   :toctree: generated/

   DataSet.plot


Variable modification 
---------------------

.. autosummary::
   :toctree: generated/

   DataSet.assign
   DataSet.rename
   DataSet.set_missing
   DataSet.sum_all

NetCDF file attribute modification 
---------------------

.. autosummary::
   :toctree: generated/

   DataSet.set_longnames
   DataSet.set_units

Vertical/level methods
---------------------

.. autosummary::
   :toctree: generated/

   DataSet.surface
   DataSet.bottom
   DataSet.vertical_interp
   DataSet.vertical_mean
   DataSet.vertical_min
   DataSet.vertical_max
   DataSet.vertical_range
   DataSet.vertical_sum
   DataSet.vertical_cumsum
   DataSet.invert_levels
   DataSet.bottom_mask



Rolling methods
---------------------

.. autosummary::
   :toctree: generated/

   DataSet.rolling_mean
   DataSet.rolling_min
   DataSet.rolling_max
   DataSet.rolling_sum
   DataSet.rolling_range



Evaluation setting
---------------------

.. autosummary::
   :toctree: generated/

   DataSet.run


Cleaning functions
---------------------

.. autosummary::
   :toctree: generated/

   cleanup()
   deep_clean()

=======

Ensemble creation
---------------------

.. autosummary::
   :toctree: generated/

   create_ensemble
   generate_ensemble

Arithemetic methods
---------------------

.. autosummary::
   :toctree: generated/

   DataSet.assign
   DataSet.add
   DataSet.subtract
   DataSet.multiply
   DataSet.divide


Ensemble statistics
---------------------

.. autosummary::
   :toctree: generated/

   DataSet.ensemble_mean
   DataSet.ensemble_min
   DataSet.ensemble_max
   DataSet.ensemble_percentile
   DataSet.ensemble_range
   DataSet.ensemble_sum


Subsetting operations
---------------------

.. autosummary::
   :toctree: generated/

   DataSet.crop
   DataSet.select
   DataSet.drop

Time-based methods
---------------------

.. autosummary::
   :toctree: generated/

   DataSet.set_date
   DataSet.shift

Interpolation and resampling methods
---------------------

.. autosummary::
   :toctree: generated/

   DataSet.regrid
   DataSet.to_latlon
   DataSet.resample_grid
   DataSet.time_interp
   DataSet.timestep_interp


Masking methods
---------------------

.. autosummary::
   :toctree: generated/

   DataSet.mask_box




Statistical methods
---------------------

.. autosummary::
   :toctree: generated/

   DataSet.tmean
   DataSet.tmin
   DataSet.tmedian
   DataSet.tpercentile
   DataSet.tmax
   DataSet.tsum
   DataSet.trange
   DataSet.tvariance
   DataSet.tstdev
   DataSet.tcumsum

   DataSet.cor_space
   DataSet.cor_time

   DataSet.spatial_mean
   DataSet.spatial_min
   DataSet.spatial_max
   DataSet.spatial_percentile
   DataSet.spatial_range
   DataSet.spatial_sum

   DataSet.centre

   DataSet.zonal_mean
   DataSet.zonal_min
   DataSet.zonal_max
   DataSet.zonal_range

   DataSet.meridonial_mean
   DataSet.meridonial_min
   DataSet.meridonial_max
   DataSet.meridonial_range




Merging methods
---------------------

.. autosummary::
   :toctree: generated/

   DataSet.merge
   DataSet.merge_time


Splitting methods
---------------------

.. autosummary::
   :toctree: generated/

   DataSet.split


Output and formatting methods
---------------------

.. autosummary::
   :toctree: generated/

   DataSet.to_nc
   DataSet.to_xarray
   DataSet.to_dataframe
   DataSet.zip
   DataSet.format

Miscellaneous methods
---------------------

.. autosummary::
   :toctree: generated/

   DataSet.cell_area
   DataSet.cdo_command
   DataSet.nco_command
   DataSet.compare_all
   DataSet.reduce_dims
   DataSet.reduce_grid



Ecological methods
---------------------

.. autosummary::
   :toctree: generated/

   DataSet.phenology








