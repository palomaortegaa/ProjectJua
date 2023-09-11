# Created 19 Apr 23
# To calculate % difference in LCUEs across scenarios (S1-S4 vs S0)
# Includes all 166 sites (just for my records)
# Useful code to see how to get colors ID
# Last part of code is more for exercise purpose (to understand what NS said)
# check Jupyter notebook version for plots: 'diff_lcue'
# plots to add in Ch. 4 analysis (but not on final draft)

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Move to path where csv is saved
path = "/Users/po416/Library/CloudStorage/OneDrive-ImperialCollegeLondon/PhDOct2018/Projects (12Mar20)/Project Jua/Modelling PJua analysis/Results_outputs"

cwd = os.getcwd()
cwd

os.chdir(path)
cwd  #pwd

# Import df with LCUEs for each scenario
data = pd.read_csv("lcue_s0_s4.csv")

# Define function to calculate percentage change
def percentage_change(col1, col2):
    return ((col2 - col1) / col1) * 100

# Create new pandas DataFrame from copy of original df
perchange = data[["Site_name", "County", "Institution"]].copy()

# Add columns with calculated values of percentage change vs S0
perchange["S1_S0"] = percentage_change(data["S0_LCUE"], data["S1_LCUE"]).round(2)
perchange["S2_S0"] = percentage_change(data["S0_LCUE"], data["S2_LCUE"]).round(2)
perchange["S3_S0"] = percentage_change(data["S0_LCUE"], data["S3_LCUE"]).round(2)
perchange["S4_S0"] = percentage_change(data["S0_LCUE"], data["S4_LCUE"]).round(2)

# To see how the data looks, here it shows the % change in LCUEs of S1-S4 vs S0
perchange.describe().round(2)

# Import library to plot and set style in Seaborn
import seaborn as sns

sns.set(rc={"figure.dpi":300})
sns.set_context("notebook")  # change to paper maybe? I prefer notebook style i think...
sns.set_style("ticks") # with axis ticks, no background lines
# sns.set_style("whitegrid")

# To format plot with scenarios colors
print(sns.color_palette("Set2").as_hex()) # to know colours
#  returns hex ID of each color in palette Set2
# ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854', '#ffd92f', '#e5c494', '#b3b3b3']

# Define my Set2 custom palette without S0 color (skip first one)
colors = ["#fc8d62", "#8da0cb", "#e78ac3", "#a6d854"]

# Final version of plot (for now)
fig,ax = plt.subplots(1,1)
sns.kdeplot(data=perchange.S1_S0, color=colors[0],label="S1", ax=ax) # fill=True
sns.kdeplot(data=perchange.S2_S0, color=colors[1],label="S2", ax=ax) # fill=True
sns.kdeplot(data=perchange.S3_S0, color=colors[2],label="S3", ax=ax) # fill=True
sns.kdeplot(data=perchange.S4_S0, color=colors[3],label="S4", ax=ax) # fill=True
plt.xlabel("Percentage difference (%)")
plt.legend(frameon=False)

# Another way of plotting one by one
fig,ax = plt.subplots(1,1)
sns.kdeplot(data=perchange.S1_S0, color="#fc8d62",label="S1", ax=ax) # fill=True

# Another way but it is wrong (i think) as it takes density calculating 664 in total instead of 166 in each
sns.kdeplot(data=perchange, palette=colors)

# Refs:
# https://seaborn.pydata.org/tutorial/distributions.html
# https://stackoverflow.com/questions/65759931/seaborn-kde-plot-plotting-probabilities-instead-of-density-histplot-without-bar

# In all of the following plots I think it was calculating the density based on the 664 observations
# that is why the density values were so low (0.008 - which multiplied by 4 gives 0.032)
# but i'm putting trials here for reference

# Plot 1
sns.displot(perchange)
# returns histogram with stacked bars

# Plotting density curves
# Plot 2
sns.displot(perchange, kind="kde") # fill=True
# returns lines (este era el bueno antes)

# Plot 3
sns.displot(perchange, kde=True)
# returns histogram with lines

# Plot 4 - adjusting bandwidth to better represent the data (trial 1)
sns.displot(perchange, kind="kde", bw_adjust=.25) # or 0.5
# returns a plot with curve less smooth but shows bumps clearer
# however i'm not sure of the meaningfulness of these bumps (they could be bc of bad sample or systematic error)

# Plot 5 - adjusting bandwidth to better represent the data (trial 2)
sns.displot(perchange, kind="kde", bw_adjust=2)
# curve is now too smooth, loses modes in dataset

# Plot 6 - adjusting bandwidth to better represent the data (trial 3)
sns.displot(perchange, kind="kde", bw_adjust=1.5) # or 0.5
# curve is still too smooth (1.5) or too spikey (0.5) so i think is better to stick with default value of
# bw_adjust which I'm pretty sure default is 1

# Plot 7 - Plotting line by line
sns.kdeplot(perchange.S1_S0)  # shade=True
                              # cumulative=True (but not sure what this shows)


# Calculating the difference between the lines (instead of eyeballing plot)
# Using np.histogram to display the frequency of data distribution in a numerical form.
# Represents frequency (y-axis) and class interval call bin (x-axis)
np.histogram(perchange["S1_S0"], bins=3)
# returns:  (array([106,  50,  10]),
 # array([-54.12      , -11.06666667,  31.98666667,  75.04      ]))
#  meaning that it cut the data in 3 bins (-54 to -11; -11 to 31.98; 31.98 to 75)
# gives total observations (n=166) in each bin (106, 50, 10)

# Same as above but accessing certain elements of the return of np.histogram
np.histogram(perchange["S1_S0"], bins=3)[0] # or [1]

# I can also specify the exact values of the bins
np.histogram(perchange["S1_S0"], bins=[-100,0,100])
# returns for S1: (array([124,  42]), array([-100,    0,  100]))
# meaning that 124 observations have a cost difference lower than 0 (negative)
# and 42 have a cost difference higher than 0 (positive)

# Same as above but for S2
np.histogram(perchange["S2_S0"], bins=[-100,0,100])
# returns: (array([139,  27]), array([-100,    0,  100]))
# NS said this means that the probability of having a cost increase for S1 is 40%
# and 30% for S2. So I think he just round up the 40 and 30 values above 0 but not
# completely sure that is how you interpret it?... double check

# other useful refs:
# https://numpy.org/doc/stable/reference/generated/numpy.histogram.html
# https://stackoverflow.com/questions/65759931/seaborn-kde-plot-plotting-probabilities-instead-of-density-histplot-without-bar

# Previous plot trials
ax= sns.displot(perchange, kind="kde", palette=colors) # fill=True
ax.set(xlabel= "Percentage difference (%)")
# ax.set(xlabel= "Name", ylabel= "Name")
# ax.set(title="Name")
# plt.legend(labels = ["S1", "S2", "S3", "S4"]) # add this but doesn't work
plt.show()
# returns plot but density is from all 664 observations instead of line per line (so wrong i think)

# Notes of other legend trials that didn't work properly (to avoid repeating it)
# ax._legend.remove() # gets rid of legend

# ax.legend(loc="upper right", frameon=True)

# ax.legend(title="Smoker", bbox_to_anchor=(1.05, 1), labels=["S1", "S2", "S3","S4"])

# sns.move_legend(ax, title='', loc='best')
#
# sns.move_legend(
#     ax, "center right", bbox_to_anchor=(1, 1),
#     frameon=True,
# )
#
# sns.move_legend(ax, "center right")
# legend = ax._legend
# legend.set_title("Holi")
# plt.show()
#
# sns.legend(["S1", "S2", "S3", "S4"])
#
# ax.legend(["S1", "S2", "S3", "S4"])
#
# legend_handles, _= ax.get_legend_handles_labels()
# ax.legend(legend_handles, ["S1","S2","S3","S4",],
#           bbox_to_anchor=(1,1),
#           title='whatever title you want to use')
#
# g = sns.displot(perchange, kind="kde", palette=colors) # fill=True
# g.set(xlabel= "Percentage difference (%)")
# g._legend.remove()
