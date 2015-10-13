#!/usr/bin/env python

#title           : xtl_converter.py
#description     : Converts VESTA XTL Fractional Coordinate crystal files to muSTEM format
#author          : Steven R. Spurgeon
#date            : 09-09-2015
#version         : 1.0
#usage           : python xtl_converter.py input.xtl
#python_version  : 2.7.10
#==============================================================================

import os, sys # Required libraries

# Get the input file from the user and setup the output file
input_file = str(sys.argv[1])
input_file_name, input_file_extension = os.path.splitext(input_file)
output_file_name = input_file_name + "_converted.xtl"

# Get simulation parameter from user
voltage = int(raw_input('Enter the accelerating voltage (Default: 200 keV): ') or "200")

# Element reference table
# Each row is of the form: "Element Name", Z, Fractional Occupancy, and
# Debye-Waller Factor / (8*Pi^2)
reference_table = ["La", 57, 1, "2.247E-2",
                   "Ni", 28, 1, "3.6E-3",
                   "Mn", 25, 1, "0.1E-3",
                   "O",  8,  1, "0.9275"]

# Define an empty element list specific to this crystal
element_list = []

# Search the input file and remove integer Miller indices, then write to a temp file
with open(input_file) as oldfile, open ('cif_temp.txt', 'w') as newfile:

    lattice_parameters = ['1.000000'] # Remove integer lattice parameters

    # Write everything to the final file
    for line in oldfile:
        if not any(lattice_parameter in line for lattice_parameter in lattice_parameters):
            newfile.write(line)

# Loop through the CIF and figure out what elements are present and how many
# atoms of each type there are
with open('cif_temp.txt') as oldfile:

    # Some counting variables
    n = 0
    current_atom = ""
    atom_count = 1
    atom_types = 0

    for line in oldfile:

        if n == 7: # Skip the first 7 lines of the program that are headers
            current_atom = line[:2]
            element_list.append(current_atom)

        if n > 7: # Compare each atom to the current atom
            new_atom = line[:2]

            if new_atom != current_atom:
                element_list.append(atom_count)
                atom_types += 1

                if new_atom != 'EO': # Make sure the 'EOF' marker isnt counted
                    element_list.append(new_atom.strip())

                atom_count = 0
                current_atom = new_atom

            atom_count += 1

        n += 1

# Loop through the CIF, reformatting and printing the header. Then go through
# each type of atom, group, and print everything to the final file
with open('cif_temp.txt') as oldfile, open (output_file_name, 'w') as newfile:

    sys.stdout = newfile # Write output from the console to the file

    # Initialize some variables
    n = 0
    current_atom = ""
    atom_count = 1

    for line in oldfile:

        # Header stuff
        # Write title of file
        if n == 0:
            line_temp = line.rstrip()
            print "Filename: " + input_file_name + "    Crystal: " + line_temp.split("TITLE ")[1]

        # Write some user-input parameters
        if n == 2:
            print line.strip()
            print voltage
            print atom_types

        # Loop through each type of element and print a header, as well as the
        # atom positions for that element
        if n > 6:
            new_atom = line[:2]

            if new_atom != current_atom and new_atom != "EO": # Skip EOF marker

                # Start a new entry every time a new element is encountered
                print new_atom
                element_list_entry = element_list.index(new_atom.strip()) + 1
                print "    ",element_list[element_list_entry],

                # Compare the current element to the element database to recall
                # element parameters
                for i in range (1,4):
                    reference_table_entry = reference_table.index(new_atom.strip()) + i
                    print "    ",reference_table[reference_table_entry],

                print "\r" # Space things out
                current_atom = new_atom

            # Prevent "EOF" from printing at the end
            if new_atom != "EO":
                stripped_line = line.strip(current_atom)
                print "    ",stripped_line.strip()

        n += 1

    # Add orientation information used by muSTEM
    newfile.write("Orientation \n" + "    " + "0 0 1 \n" + "    " + "1 0 0 \n" + "    "
     + "0 1 0 \n")

# Clean up temporary file
os.remove('cif_temp.txt')
