# XTL-Converter

## Description

XTL-Converter is a simple Python script that converts a VESTA crystal file into the format used by the µSTEM multislice simulation program developed by Leslie Allen et al. at the University of Melbourne.

For more information about µSTEM, please visit: [µSTEM](http://tcmp.ph.unimelb.edu.au/mustem/muSTEM.html)

To download the VESTA crystal viewer, please visit:
[VESTA](http://jp-minerals.org/vesta/)

## Installation and Usage

Requirements: Python Environment (3.5+) and input VESTA fractional coordinates (`*.xtl`) file

First build your crystal in VESTA and apply any coordinate transformation needed to align the principal axes to the zone-axis of interest. Then export the fractional coordinates to a `*.xtl` file and copy it to the folder containing this script.

To run on OSX, execute the command `python xtl_converter.py input.xtl` from the terminal.

To run on Windows, make sure the extension `*.py` is associated with Python, then execute the command `xtl_converter.py input.xtl` from the command line.


## Frequently Asked Questions (FAQ)

1. **The program says it can't find a symbol and is crashing.**

XTL-Converter uses a lookup table of Debye-Waller factors (DWFs). While I've incldued these for many different elements, some are missing and not all space groups are included. You can add your own values by modifying the table in the first half of the program. The format is: `"Element Symbol", "Atomic Number", "Fractional Occupancy", "DWF / (8 * Pi^2)"`

## Reference

If you find this script useful, please cite the following reference:
[![DOI](https://zenodo.org/badge/18751/stevenspurgeon/xtl-converter.svg)](https://zenodo.org/badge/latestdoi/18751/stevenspurgeon/xtl-converter)

## History

v1.2.1 – 10/13/17 – Fixed typo in O Debye-Waller Factor.

v1.2 – 10/11/16 – Rewrote code to run under Python 3.5.10. The old version will no longer be supported.

v1.1.1 – 11/02/15 – Significantly expanded the element lookup table.

v1.0.1 – 10/07/15 – Added citation support.

v1.0 – 10/13/15 – Initial release.

## Credits

Thanks to Nathan Lugg (University of Tokyo) for helpful discussions.

## Disclaimer

This material was prepared as an account of work sponsored by an agency of the United States Government.  Neither the United States Government nor the United States Department of Energy, nor Battelle, nor any of their employees, nor any jurisdiction or organization that has cooperated in the development of these materials, makes any warranty, express or implied, or assumes any legal liability or responsibility for the accuracy, completeness, or usefulness or any information, apparatus, product, software, or process disclosed, or represents that its use would not infringe privately owned rights.

Reference herein to any specific commercial product, process, or service by trade name, trademark, manufacturer, or otherwise does not necessarily constitute or imply its endorsement, recommendation, or favoring by the United States Government or any agency thereof, or Battelle Memorial Institute. The views and opinions of authors expressed herein do not necessarily state or reflect those of the United States Government or any agency thereof.

Pacific Northwest National Laboratory operated by Battelle for the United States Department of Energy under Contract DE-AC05-76RL01830

