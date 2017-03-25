
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
# Description
# Uses Numpy, Scipy, Matplotlib to generate a histogram
# from a one-dimensional data series; the matplotlib method
# calls contain the neccessary arguments to customize
# the plot appearance
# ----------------------------------------------------------------

import scipy as sp
from scipy import stats
import matplotlib.pyplot as plt


# The following data series refer to a certain type of chemical impurity measured in parts per million in 25
# drinking-water samples randomly collected from different areas of a county

# 11 19 24 30 12 20 25 29 15 21
#------------------------------
# 24 31 16 23 25 26 32 17 22 26
#------------------------------
# 35 18 24 18 27

#import data from the acconpanying csv file; the data is placed into a numpy(scipy) one-dimensional array conc_data
#make sure the to have your csv file format properly configured; the csv file may be placed in the same folder as the
#script file if you decide not to customize the filepath accodingly

conc_data = sp.genfromtxt('conc_data.csv', delimiter = " ")

#compute simple statistical descriptors, mean value and standard deviation
mean_value = sp.mean(conc_data)
std_value = sp.std(conc_data)

#create histogram using 5 equally spaced data bins
plt.hist(conc_data, bins=5,facecolor='g')  # plt.hist passes it's arguments to np.histogram

#set the plot margins
plt.margins(0.01)
plt.subplots_adjust(bottom=0.15)

#set the plot title
plt.title("Impurity concentration measurements", fontsize=18, y =1.03)

#set the x-label title fontsize and axis-label spacing
plt.xlabel('Concentration (ppm)',fontsize=18,labelpad=10)
plt.xticks(fontsize=18)

#set the y-label title fontsize and axis-label spacing
plt.ylabel('Frequency count',fontsize=18,labelpad=10)
plt.yticks(fontsize=18)


#append leyends to plot area indicating the mean value and standard deviation
plt.text(12, 7.5, r'$\mu={:.3f}$'.format(mean_value),fontsize=20)
plt.text(12, 6.8, r'$\sigma={:.3f}$'.format(std_value),fontsize=20)

#save the histogram figure as a pdf file
plt.savefig('impurity_hist.pdf', dpi=300)

#show an on-screen preview of the resulting histogram figure
plt.show()
