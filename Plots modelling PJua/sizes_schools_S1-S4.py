# Created 15Mar23
# To create df of schools system sizes for heatmaps of S1-S4
# Second part of this code is for plotting
# See Jupyter notebook: 'sizes_schools_S1-S4'
# check outputs with excel: 'S0-S4 analysis and check'
# previous version of this code: 'system_size_data_hp.py'

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#from matplotlib.ticker import FormatStrFormatter  # to format ticks but doesn't work i think

# Move to path where csv are saved
path = "/Users/po416/Library/CloudStorage/OneDrive-ImperialCollegeLondon/PhDOct2018/Projects (12Mar20)/Project Jua/Modelling PJua analysis/Results_outputs"
path

cwd = os.getcwd()
cwd

os.chdir(path)
cwd    # pwd

# SCENARIO 1 - GENERATING DF TO PLOT HEATMAPS OF SYSTEM SIZES OF SCHOOLS PER SCENARIO
# Imports csv of scenario I want
s1 = pd.read_csv("Optim_res_unmet_0_inst.csv")  # change to other scenarios
            # scenario= "Optim_res_unmet_0_inst.csv"  # S1

# Separate df to get df of schools only
schools_s1 = s1[s1.Institution != 'Clinic']
# Groups schools by Initial storage and PV size
schools_s1 = schools_s1.groupby(["Initial_storage_size","Initial_PV_size"])
# Counts unique site names to know number of sites per system size combination
schools_s1_cnt = schools_s1.Site_name.nunique()  # returns a series
schools_s1_cnt.head()

# Convert series to df
schools_s1_cnt_df = schools_s1_cnt.to_frame()
# Pivot df so it has a wide-spread form
# schools_s1_cnt_df # to show in Jupyter

# to check there are 148 schools
schools_s1_cnt_df["Site_name"].sum()  # returns 148
schools_s1_cnt_df["Site_name"].describe().round(2)    # to know schools min and max values (vmin & vmax)
                    # returns: min= 1 (vmin), max= 17 (vmax) # count of system configurations

schools_s1_hp = schools_s1_cnt_df.reset_index().pivot(index="Initial_storage_size", columns="Initial_PV_size", values="Site_name")
# schools_s1_hp # to show in Jupyter

# Setting style for plotting
sns.set(rc={"figure.dpi":300})
sns.set_style("ticks")
#sns.set_context("paper")  # poster

# S1 SCHOOL SIZES PLOT (Plotting data as it is)
ax = sns.heatmap(schools_s1_hp, cmap="mako_r", annot=True)   # vmin= 1, vmax= 50
ax.invert_yaxis()
ax.set_title("S1 - Schools")
ax.set_ylabel("Storage size (kWh)")
ax.set_xlabel("PV size (kWp)")
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
ax.set_yticklabels(ax.get_yticklabels(), rotation=0)

# to add Impala as data point (marker by matrix coordinates - not x and y axis values):
# ax.plot(3.5,5.1, marker="D", color= "black", ms="5") # change ms for marker size

# Drawing the frame
for _, spine in ax.spines.items():
    spine.set_visible(True)
    spine.set_linewidth(1)

# show plot
plt.show()


# SCENARIO 2 - GENERATING DF TO PLOT HEATMAPS OF SYSTEM SIZES OF SCHOOLS PER SCENARIO
# Imports csv of scenario I want
s2 = pd.read_csv("Optim_res_unmet_0.01_inst.csv")  # change to other scenarios

# Separate df to get df of schools only
schools_s2 = s2[s2.Institution != 'Clinic']
# Groups schools by Initial storage and PV size
schools_s2 = schools_s2.groupby(["Initial_storage_size","Initial_PV_size"])
# Counts unique site names to know number of sites per system size combination
schools_s2_cnt = schools_s2.Site_name.nunique()  # returns a series
schools_s2_cnt.head()

# Convert series to df
schools_s2_cnt_df = schools_s2_cnt.to_frame()
# Pivot df so it has a wide-spread form
# schools_s2_cnt_df # to show in Jupyter

# to check there are 148 schools
schools_s2_cnt_df["Site_name"].sum()  # returns 148
schools_s2_cnt_df["Site_name"].describe().round(2)    # to know schools min and max values (vmin & vmax)
                    # returns: min= 1 (vmin), max= 37 (vmax)

schools_s2_hp = schools_s2_cnt_df.reset_index().pivot(index="Initial_storage_size", columns="Initial_PV_size", values="Site_name")
# schools_s2_hp # to show in Jupyter


# S2 SCHOOL SIZES PLOT (Plotting data as it is)
ax = sns.heatmap(schools_s2_hp, cmap="mako_r") #  annot=True, vmin=1, vmax=50
ax.invert_yaxis()
ax.set_title("S2 - Schools")
ax.set_ylabel("Storage size (kWh)")
ax.set_xlabel("PV size (kWp)")
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
ax.set_yticklabels(ax.get_yticklabels(), rotation=0)

# Drawing the frame
for _, spine in ax.spines.items():
    spine.set_visible(True)
    spine.set_linewidth(1)

# show plot
plt.show()


# SCENARIO 3 - GENERATING DF TO PLOT HEATMAPS OF SYSTEM SIZES OF SCHOOLS PER SCENARIO
# Imports csv of scenario I want
s3 = pd.read_csv("Optim_res_unmet_0.05_inst.csv")  # change to other scenarios

# Separate df to get df of schools only
schools_s3 = s3[s3.Institution != 'Clinic']
# Groups schools by Initial storage and PV size
schools_s3 = schools_s3.groupby(["Initial_storage_size","Initial_PV_size"])
# Counts unique site names to know number of sites per system size combination
schools_s3_cnt = schools_s3.Site_name.nunique()  # returns a series
schools_s3_cnt.head()

# Convert series to df
schools_s3_cnt_df = schools_s3_cnt.to_frame()
# Pivot df so it has a wide-spread form
# schools_s3_cnt_df # to show in Jupyter

# to check there are 148 schools
schools_s3_cnt_df["Site_name"].sum()  # returns 148
schools_s3_cnt_df["Site_name"].describe().round(2)    # to know schools min and max values (vmin & vmax)
                    # returns: min= 1 (vmin), max= 48 (vmax)

schools_s3_hp = schools_s3_cnt_df.reset_index().pivot(index="Initial_storage_size", columns="Initial_PV_size", values="Site_name")
# schools_s3_hp # to show in Jupyter


# S3 school SIZES PLOT (Plotting data as it is)
ax = sns.heatmap(schools_s3_hp, cmap="mako_r")  # vmin=1, vmax=50, annot=True
ax.invert_yaxis()
ax.set_title("S3 - Schools")
ax.set_ylabel("Storage size (kWh)")
ax.set_xlabel("PV size (kWp)")
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
ax.set_yticklabels(ax.get_yticklabels(), rotation=0)

# Drawing the frame
for _, spine in ax.spines.items():
    spine.set_visible(True)
    spine.set_linewidth(1)

# show plot
plt.show()


# SCENARIO 4 - GENERATING DF TO PLOT HEATMAPS OF SYSTEM SIZES OF SCHOOLS PER SCENARIO
# Imports csv of scenario I want
s4 = pd.read_csv("Optim_res_unmet_0.1_inst.csv")  # change to other scenarios

# Separate df to get df of schools only
schools_s4 = s4[s4.Institution != 'Clinic']
# Groups schools by Initial storage and PV size
schools_s4 = schools_s4.groupby(["Initial_storage_size","Initial_PV_size"])
# Counts unique site names to know number of sites per system size combination
schools_s4_cnt = schools_s4.Site_name.nunique()  # returns a series
schools_s4_cnt.head()

# Convert series to df
schools_s4_cnt_df = schools_s4_cnt.to_frame()
# Pivot df so it has a wide-spread form
# schools_s4_cnt_df # to show in Jupyter

# to check there are 148 schools
schools_s4_cnt_df["Site_name"].sum()  # returns 148
schools_s4_cnt_df["Site_name"].describe().round(2)    # to know schools min and max values (vmin & vmax)
                    # returns: min= 1 (vmin), max= 44 (vmax)

schools_s4_hp = schools_s4_cnt_df.reset_index().pivot(index="Initial_storage_size", columns="Initial_PV_size", values="Site_name")
# schools_s4_hp # to show in Jupyter


# S4 SCHOOL SIZES PLOT (Plotting data as it is)
ax = sns.heatmap(schools_s4_hp, cmap="mako_r")  # set annot=True, vmin= 1, vmax= 50
ax.invert_yaxis()
ax.set_title("S4 - Schools")
ax.set_ylabel("Storage size (kWh)")
ax.set_xlabel("PV size (kWp)")
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
ax.set_yticklabels(ax.get_yticklabels(), rotation=0)

# Drawing the frame
for _, spine in ax.spines.items():
    spine.set_visible(True)
    spine.set_linewidth(1)

# show plot
plt.show()


##  BEGINNING OF SUBPLOTS PLOT No. 1  ##
# Subplots of S1-S4 with data as it is (different axis but same colour scale)
fig, axes = plt.subplots(2, 2, figsize=(12, 8))  # The `figsize` is in inches and can be changed :)

# Python 3.7 etc. version
axis = axes[0, 0]   # top left
sns.heatmap(
    schools_s1_hp, vmin=1, vmax=50, cmap="mako_r",
    ax=axis,
)

# Code for writing titles etc.
axis.invert_yaxis()
axis.set_title("S1 - Schools")
axis.set_ylabel("Storage size (kWh)")
axis.set_xlabel("") # PV size (kWp)
axis.set_xticklabels(axis.get_xticklabels(), rotation=45)
axis.set_yticklabels(axis.get_yticklabels(), rotation=0)
#axis.plot(3.5,5.1, marker="D", color= "black", ms="5")

# Drawing the frame
for _, spine in axis.spines.items():
    spine.set_visible(True)
    spine.set_linewidth(1)

# Code for writing the letters, might also be possible to add other labels e.g., "Rhino" near the Rhino column
axis.text(
    -0.08,
    1.1,
    "a.",
    transform=axis.transAxes,
    fontsize=16,
    fontweight="bold",
    va="top",
    ha="right",
)

# Repeat but with the other indicies as needed.
axis = axes[0, 1]  # top-right
sns.heatmap(
    schools_s2_hp, vmin=1, vmax=50, cmap="mako_r",
    ax=axis,
)

# Code for writing titles etc.
axis.invert_yaxis()
axis.set_title("S2 - Schools")
axis.set_ylabel("Storage size (kWh)")
axis.set_xlabel("") # PV size (kWp)
axis.set_xticklabels(axis.get_xticklabels(), rotation=45)
axis.set_yticklabels(axis.get_yticklabels(), rotation=0)
#axis.plot(3.5,5.1, marker="D", color= "black", ms="5")

# Drawing the frame
for _, spine in axis.spines.items():
    spine.set_visible(True)
    spine.set_linewidth(1)

# Code for writing the letters, might also be possible to add other labels e.g., "Rhino" near the Rhino column
axis.text(
    -0.08,
    1.1,
    "b.",
    transform=axis.transAxes,
    fontsize=16,
    fontweight="bold",
    va="top",
    ha="right",
)

axis = axes[1, 0]  # bottom-left
sns.heatmap(
    schools_s3_hp, vmin=1, vmax=50, cmap="mako_r",
    ax=axis,
)

# Code for writing titles etc.
axis.invert_yaxis()
axis.set_title("S3 - Schools")
axis.set_ylabel("Storage size (kWh)")
axis.set_xlabel("PV size (kWp)")
axis.set_xticklabels(axis.get_xticklabels(), rotation=45)
axis.set_yticklabels(axis.get_yticklabels(), rotation=0)
#axis.plot(3.5,5.1, marker="D", color= "black", ms="5")

# Drawing the frame
for _, spine in axis.spines.items():
    spine.set_visible(True)
    spine.set_linewidth(1)

# Code for writing the letters, might also be possible to add other labels e.g., "Rhino" near the Rhino column
axis.text(
    -0.08,
    1.1,
    "c.",
    transform=axis.transAxes,
    fontsize=16,
    fontweight="bold",
    va="top",
    ha="right",
)

axis = axes[1, 1]  # bottom-right
sns.heatmap(
    schools_s4_hp, vmin=1, vmax=50, cmap="mako_r",
    ax=axis,
)

# Code for writing titles etc.
axis.invert_yaxis()
axis.set_title("S4 - Schools")
axis.set_ylabel("Storage size (kWh)")
axis.set_xlabel("PV size (kWp)")
axis.set_xticklabels(axis.get_xticklabels(), rotation=45)
axis.set_yticklabels(axis.get_yticklabels(), rotation=0)
#axis.plot(3.5,5.1, marker="D", color= "black", ms="5")

# Drawing the frame
for _, spine in axis.spines.items():
    spine.set_visible(True)
    spine.set_linewidth(1)

# Code for writing the letters, might also be possible to add other labels e.g., "Rhino" near the Rhino column
axis.text(
    -0.08,
    1.1,
    "d.",
    transform=axis.transAxes,
    fontsize=16,
    fontweight="bold",
    va="top",
    ha="right",
)

# plt.savefig(
#     "figure_title.png",
#     transparent=True,
#     dpi=300,
#     bbox_inches="tight",
# )
plt.tight_layout()
plt.show()

##  END OF SUBPLOTS PLOT No. 1  ##

# CHANGE DF TO EXTEND X AND Y AXIS AND REINDEX DF TO COMPARE PLOTS S1-S4
# BUT FIRST CHANGE AXIS DEPENDING OF SYSTEM SIZES MAX sizes (all scenarios together)

# to print ranges of axis (storage size - S1 has the largest)
for p in range(1, 15):
    print(p, end=', ')

# to print ranges of axis (PV size - S1 has the largest) with better format
for i in (np.arange(0.265, 3.71, 0.265)).round(3):
    print(i, end=', ')


# S1
schools_s1_hp_ext = schools_s1_hp.reindex(range(1,15), axis=0) # fill_value=0
schools_s1_hp_ext = schools_s1_hp_ext.reindex((np.arange(0.265, 3.71, 0.265)).round(3), axis=1)

# S2
schools_s2_hp_ext = schools_s2_hp.reindex(range(1,15), axis=0) # fill_value=0
schools_s2_hp_ext = schools_s2_hp_ext.reindex((np.arange(0.265, 3.71, 0.265)).round(3), axis=1)

# S3
schools_s3_hp_ext = schools_s3_hp.reindex(range(1,15), axis=0) # fill_value=0
schools_s3_hp_ext = schools_s3_hp_ext.reindex((np.arange(0.265, 3.71, 0.265)).round(3), axis=1)

# S4
schools_s4_hp_ext = schools_s4_hp.reindex(range(1,15), axis=0) # fill_value=0
schools_s4_hp_ext = schools_s4_hp_ext.reindex((np.arange(0.265, 3.71, 0.265)).round(3), axis=1)

# repeat plot above but changing variables to "_ext"  (just add this at the end)
# schools_s1_hp_ext
# schools_s2_hp_ext
# schools_s3_hp_ext
# schools_s4_hp_ext

# S1 SCHOOL SIZES PLOT (extending axis and adding Impala with marker)
ax = sns.heatmap(schools_s1_hp_ext, cmap="mako_r", vmin= 1, vmax= 50)
ax.invert_yaxis()
ax.set_title("S1 - Schools")
ax.set_ylabel("Storage size (kWh)")
ax.set_xlabel("PV size (kWp)")
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
ax.set_yticklabels(ax.get_yticklabels(), rotation=0)

# to add Impala as data point (marker by matrix coordinates - not x and y axis values):
ax.plot(3.5,5.1, marker="D", color= "dimgrey", ms="5")  # or "black", change ms for marker size

# Drawing the frame
for _, spine in ax.spines.items():
    spine.set_visible(True)
    spine.set_linewidth(1)

# show plot
plt.show()

# Another option to add Impala as data point
# ax.text(2,10, "o")
# ax.text(6.5,6.5, "o")  # or "Impala" instead of "o"

# See more on customising heatmap: https://www.python-graph-gallery.com/91-customize-seaborn-heatmap

# Customising heatmap
# sns.heatmap(df, yticklabels=False) # deletes yticks and y-axis line
# sns.heatmap(df, xticklabels=False)  # deletes xticks and x-axis line

# Other formatting options:
# ax.tick_params(left=False, bottom=False)
# g1.set(xticklabels=[])  # remove the tick labels
# g1.set(xlabel=None)  # remove the axis label

# NOTES:
# Code for making subplots BW
#  https://gist.github.com/BenWinchester/b80dacf73507f05162f865fb04845359
