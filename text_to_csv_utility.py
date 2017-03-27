

# ###################################
# -----------------------------------
# -  Copyright 2016, Juan E. Rolon  -
# -  The Math Bayou                 -
# -  www.mathbayou.com              -
# -----------------------------------
# ###################################
#
# TEXT TO CSV CONVERTER UTILITY
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# ----------------------------------------------------------------
# DESCRIPTION:
# Uses csv to convert blank-space-delimited raw data text files to
# csv data file containing a single field (column); the csv data
# is intended to represent one-dimensional data series; please check
# the structure of the accompanying sample text file before running
# the script
# ----------------------------------------------------------------
#
#COMMENTS: Sample content of accompanying text file 'sample_data.txt'
#
# 11 19 24 30 12 20 25 29 15 21
# 24 31 16 23 25 26 32 17 22 26
# 35 18 24 18 27
#


import csv

txtfile = open('sample_data.txt', "r")
csvfile = open('sample_data.csv', 'w', newline='')

fields = ['data_series']
writer = csv.DictWriter(csvfile, fieldnames=fields, dialect='excel')

data = txtfile.readlines()

#writer.writeheader() uncomment this line if your csv file contains column headers (names)

for m in data:
    line_list = m.split(" ")
    for i in range(len(line_list)):
        print(line_list[i].strip())
        writer.writerow({'data_series': line_list[i].strip()})

txtfile.close()
csvfile.close()