# ligoxml2csv
Converter for LIGOLW XML files to CSV without LAL dependencies

This script converts LIGOLW XML files into CSV tables for each table
contained in each XML files. The script DOES NOT depend on any LVC
software. The only format assumptions are the presence of "Table"
elements, containing "Columns" elements and a "Stream" element with
the comma-separated data.

No prior knowledge of the table names or column names is used.

Example:

      $ python xml2csv.py --help
