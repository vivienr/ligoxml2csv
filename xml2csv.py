#!/usr/bin/env python

"""xml2csv: Conversion of LIGOLW XML files to CSV

This script converts LIGOLW XML files into CSV tables for each table
contained in each XML files. The script DOES NOT depend on any LVC
software. The only format assumptions are the repsence of "Table"
elements, containing "Columns" elements and a "Stream" element with
the comma-separated data.

Example:

      $ python xml2csv.py --help


Vivien Raymond <vivien.raymond@ligo.org>

"""

try:
    import xml.etree.cElementTree as ET
except:
    import xml.etree.ElementTree as ET

import numpy as np
import csv
import sys
import argparse

parser = argparse.ArgumentParser(description='Converts LIGOLW XML into CSV tables.')
parser.add_argument('xmlfiles', type=str, nargs='+',
                    help='XML files to convert')
parser.add_argument('-s','--screen', action='store_true',
                    default=False,
                    help='Print tables to screen instead of saving as files.')

args = parser.parse_args()


for filename in args.xmlfiles:

    tree = ET.parse(filename)
    root = tree.getroot()

    for Table in root.findall("Table"):
        table_name=Table.attrib["Name"].strip(':table')
        print filename.strip('.xml')+'_'+table_name
        header=""
        count=0
        columns=[col.attrib["Name"].split(':')[-1] for col in Table.findall("Column")]
        header=' '.join(columns)
        count=len(columns)
        for stream in csv.reader([Table.find("Stream").text.replace('\n','')]):
            stream=[element.strip() for element in stream]
            data=np.array(stream)
        try:
            data=data.reshape(-1,count)
        except:
            data=data[:-1]
            data=data.reshape(-1,count)
        if args.screen:
            np.savetxt(sys.stdout,data,fmt="%s",delimiter=' ',header=header)
            print ''
        else:
            np.savetxt(filename.strip('.xml')+'_'+table_name+'.dat',data,fmt="%s",delimiter=' ',header=header)
