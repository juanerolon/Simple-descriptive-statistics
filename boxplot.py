
# ###################################
# -----------------------------------
# -  Copyright 2016, Juan E. Rolon  -
# -  The Math Bayou                 -
# -  www.mathbayou.com              -
# -----------------------------------
# ###################################
#
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
# Uses Numpy, Scipy, Matplotlib to generate a boxplot
# from a one-dimensional data series; the matplotlib method
# calls contain the neccessary arguments to customize
# the plot appearance
# ----------------------------------------------------------------

import scipy as sp
from scipy import stats
import matplotlib.pyplot as plt


# The following data give the time in months from hire to promotion to manager for a random
# sample of 25 software engineers from all software engineers employed by a large telecommunications
# firm.
# 5 7 229 453 12 14 18 14 14 483
# 22 21 25 23 24 34 37 34 49 64
# 47 67 69 192 125

# Import data from the acconpanying csv file, hiring_data.csv; the data is placed into a numpy(scipy)
# one-dimensional array conc_data; make sure the to have your csv file format properly configured;
# the csv file may be placed in the same folder as the
# script file if you decide not to customize the filepath accodingly

hiring_data = sp.genfromtxt('hiring_data.csv', delimiter = " ")

# Compute simple statistical descriptors, mean value and standard deviation
mean_value = sp.mean(hiring_data)
std_value = sp.std(hiring_data)

# create a box_plot with the one-dimensional series hiring_data; the box extends from the lower to upper quartile values
# of the data, with a line at the median. The whiskers extend from the box to show the range of the data.
# Flier points are those past the end of the whiskers.
# For official documentation visit: http://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.boxplot.html

plt.boxplot(hiring_data,notch=False,sym='gD',vert=True,meanline=True,showmeans=True)

#set the plot title
plt.title("Boxplot hire to promotion data", fontsize=18, y =1.03)

#set the x-label title fontsize and axis-label spacing
plt.xlabel('Data set number',fontsize=18,labelpad=10)
plt.xticks(fontsize=18)

#set the y-label title fontsize and axis-label spacing
plt.ylabel('Time in months from hire to promotion to manager',fontsize=18,labelpad=10)
plt.yticks(fontsize=18)

plt.show()
