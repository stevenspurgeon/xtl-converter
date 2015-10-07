# XTL-Converter

## Description

XTL-Converter is a simple Python script that converts a VESTA crystal file into the format used by the µSTEM multislice simulation program developed by Leslie Allen et al. at the University of Melbourne.

For more information about µSTEM, please visit: [µSTEM](http://tcmp.ph.unimelb.edu.au/mustem/muSTEM.html)

To download the VESTA crystal viewer, please visit:
[VESTA](http://jp-minerals.org/vesta/)

## Installation and Usage

Requirements: Python Environment (2.7+) and input VESTA fractional coordinates (`*.xtl`) file

First build your crystal in VESTA and apply any coordinate transformation needed to align the principal axes to the zone-axis of interest. Then export the fractional coordinates to a `*.xtl` file and copy it to the folder containing this script.

To run: Execute the command `python xtl_converter.py input.xtl`

## History

v1.0 – 10/07/15 – Initial release.

## Credits

Thanks to Nathan Lugg (University of Tokyo) for helpful discussions.

## License

This script was developed at Pacific Northwest National Laboratory, managed by Battelle Inc. for the Department of Energy. The script is released under an open source license.
