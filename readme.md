
<!-- README.md is generated from README.Rmd. Please edit that file -->

[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/dwyl/esta/issues) ![code coverage](coverage.svg)
[![Build Status](https://travis-ci.org/r4ecology/nchack.png?branch=master)](https://travis-ci.org/r4ecology/nchack)
[![Documentation Status](https://readthedocs.org/projects/nctoolkit/badge/?version=latest)](https://nctoolkit.readthedocs.io/en/latest/?badge=latest)




# nctoolkit - easy tools for manipulating NetCDF data in Python

The goal of nctoolkit is to provide a comprehensive tool in Python for manipulating individual NetCDF files and ensembles of NetCDF files. The philosophy is to provide sufficient methods to carry out 80-90% of NetCDF manipulations.

This package will work with Python 3.6 upwards.

## Installation


You can install the development version of nctoolkit using using pip as follows.
```sh
pip install git+https://github.com/r4ecology/nctoolkit.git
```

This package relies on CDO and NCO under the hood.
Visit <https://code.mpimet.mpg.de/projects/cdo/files> for CDO download and
installation instructions. Note that the development version is
currently tested using CDO Version 1.9.7. Vist http://nco.sourceforge.net/ to download and install NCO.

If you use Anaconda, you can install these packages as follows:

```sh
conda install -c conda-forge cdo 
```
```sh
conda install -c conda-forge nco 
```
 
Currently, the package has been tested for Linux computers. It will not
work on Windows platforms, currently. But (buyer beware) it should work on Macs.

## Reference and tutorials

A full API reference, in depth tutorials and a how-to guide are available at [readthedocs](https://nchack.readthedocs.io/en/latest/).


