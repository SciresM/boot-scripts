# boot-scripts
![License](https://img.shields.io/badge/license-ISC-blue.svg)

This is a collection of code auto-generation utility scripts for the Horizon `Boot` system module, intended for use in Atmosphère.

## Usage

Usage is mostly fairly simple:

* Load the appropriate boot system module (currently 13.0.0 SHA256=BB6322036B539F535B21B5B147E16B0816E26ADE5F21746414E8B31837A9EBF3)
* Run the appopriate script in order to autogenerate the relevant parameter files into the directory the IDB is in.

However, a few scripts are based on parsing decompiler output as strings...these may not work on IDA versions other than IDA 7.5, and require you to use my types.

For those scripts (`boot_charger_params.py` and `drive_pad_initial_config.py`), you need to import my types (present as comments in script) and names, and apply them by hand before running to make stuff work.
