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

## Reference

If you find this script useful, please cite the following reference:
[![DOI](https://zenodo.org/badge/18751/stevenspurgeon/xtl-converter.svg)](https://zenodo.org/badge/latestdoi/18751/stevenspurgeon/xtl-converter)

## History

v1.0.1 – 10/07/15 – Added citation support.
v1.0 – 10/13/15 – Initial release.

## Credits

Thanks to Nathan Lugg (University of Tokyo) for helpful discussions.

## Disclaimer

This material was prepared as an account of work sponsored by an agency of the United States Government.  Neither the United States Government nor the United States Department of Energy, nor Battelle, nor any of their employees, nor any jurisdiction or organization that has cooperated in the development of these materials, makes any warranty, express or implied, or assumes any legal liability or responsibility for the accuracy, completeness, or usefulness or any information, apparatus, product, software, or process disclosed, or represents that its use would not infringe privately owned rights.

Reference herein to any specific commercial product, process, or service by trade name, trademark, manufacturer, or otherwise does not necessarily constitute or imply its endorsement, recommendation, or favoring by the United States Government or any agency thereof, or Battelle Memorial Institute. The views and opinions of authors expressed herein do not necessarily state or reflect those of the United States Government or any agency thereof.

Pacific Northwest National Laboratory operated by Battelle for the United States Department of Energy under Contract DE-AC05-76RL01830

