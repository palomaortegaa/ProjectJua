# Created 13Mar23
# To create df of clinics system sizes for heatmaps of S1-S4
# Second part of this code is for plotting
# See Jupyter notebook: 'sizes_clinics_S1-S4'
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

# SCENARIO 1 - GENERATING DF TO PLOT HEATMAPS OF SYSTEM SIZES OF CLINICS PER SCENARIO
# Imports csv of scenario I want
s1 = pd.read_csv("Optim_res_unmet_0_inst.csv")  # change to other scenarios

# Separate df to get df of clinics only
clinics_s1 = s1[s1.Institution != 'School']
# Groups clinics by Initial storage and PV size
clinics_s1 = clinics_s1.groupby(["Initial_storage_size","Initial_PV_size"])
# Counts unique site names to know number of sites per system size combination
clinics_s1_cnt = clinics_s1.Site_name.nunique()  # returns a series
clinics_s1_cnt.head()

# Convert series to df
clinics_s1_cnt_df = clinics_s1_cnt.to_frame()
# Pivot df so it has a wide-spread form
# clinics_s1_cnt_df # to show in Jupyter

# to check there are 18 clinics
clinics_s1_cnt_df["Site_name"].sum()  # returns 18
clinics_s1_cnt_df["Site_name"].describe().round(2)   # to know clinics min and max values (vmin & vmax)
                    # returns: min= 1 (vmin), max=2 (vmax)

clinics_s1_hp = clinics_s1_cnt_df.reset_index().pivot(index="Initial_storage_size", columns="Initial_PV_size", values="Site_name")
# clinics_s1_hp # to show in Jupyter

# Setting style for plotting
sns.set(rc={"figure.dpi":300})
sns.set_style("ticks")
#sns.set_context("paper")  # poster

# S1 CLINIC SIZES PLOT (to plot data as it is - delete vmin and vmax and ticks dictionary)
ax = sns.heatmap(clinics_s1_hp, vmin=1, vmax=4, cmap="rocket_r", cbar_kws={'ticks':[1, 2, 3, 4]}) # annot=True
ax.invert_yaxis()
ax.set_title("S1 - Clinics")
ax.set_ylabel("Storage size (kWh)")
ax.set_xlabel("PV size (kWp)")
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
ax.set_yticklabels(ax.get_yticklabels(), rotation=0)

# to add Rhino as data point (marker by matrix coordinates - not x and y axis values):
# ax.plot(8.5,9.5, marker="D", color= "black", ms="5")  # or "black", "dimgrey"

# Drawing the frame
for _, spine in ax.spines.items():
    spine.set_visible(True)
    spine.set_linewidth(1)

# show plot
# plt.tight_layout()
plt.show()


# SCENARIO 2 - GENERATING DF TO PLOT HEATMAPS OF SYSTEM SIZES OF CLINICS PER SCENARIO
# Imports csv of scenario I want
s2 = pd.read_csv("Optim_res_unmet_0.01_inst.csv")  # change to other scenarios

# Separate df to get df of clinics only
clinics_s2 = s2[s2.Institution != 'School']
# Groups clinics by Initial storage and PV size
clinics_s2 = clinics_s2.groupby(["Initial_storage_size","Initial_PV_size"])
# Counts unique site names to know number of sites per system size combination
clinics_s2_cnt = clinics_s2.Site_name.nunique()  # returns a series
clinics_s2_cnt.head()

# Convert series to df
clinics_s2_cnt_df = clinics_s2_cnt.to_frame()
# Pivot df so it has a wide-spread form
# clinics_s2_cnt_df # to show in Jupyter

# to check there are 18 clinics
clinics_s2_cnt_df["Site_name"].sum()  # returns 18
clinics_s2_cnt_df["Site_name"].describe().round(2)   # to know clinics min and max values (vmin & vmax)
                    # returns: min= 1 (vmin), max=3 (vmax)

clinics_s2_hp = clinics_s2_cnt_df.reset_index().pivot(index="Initial_storage_size", columns="Initial_PV_size", values="Site_name")
# clinics_s2_hp # to show in Jupyter


# S2 CLINIC SIZES PLOT (Plotting data as it is)
ax = sns.heatmap(clinics_s2_hp, cmap="rocket_r", annot=True) # vmin=1, vmax=4
ax.invert_yaxis()
ax.set_title("S2 - Clinics")
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


# SCENARIO 3 - GENERATING DF TO PLOT HEATMAPS OF SYSTEM SIZES OF CLINICS PER SCENARIO
# Imports csv of scenario I want
s3 = pd.read_csv("Optim_res_unmet_0.05_inst.csv")  # change to other scenarios

# Separate df to get df of clinics only
clinics_s3 = s3[s3.Institution != 'School']
# Groups clinics by Initial storage and PV size
clinics_s3 = clinics_s3.groupby(["Initial_storage_size","Initial_PV_size"])
# Counts unique site names to know number of sites per system size combination
clinics_s3_cnt = clinics_s3.Site_name.nunique()  # returns a series
clinics_s3_cnt.head()

# Convert series to df
clinics_s3_cnt_df = clinics_s3_cnt.to_frame()
# Pivot df so it has a wide-spread form
# clinics_s3_cnt_df # to show in Jupyter

# to check there are 18 clinics
clinics_s3_cnt_df["Site_name"].sum()  # returns 18
clinics_s3_cnt_df["Site_name"].describe().round(2)   # to know clinics min and max values (vmin & vmax)
                    # returns: min= 1 (vmin), max= 3 (vmax)

clinics_s3_hp = clinics_s3_cnt_df.reset_index().pivot(index="Initial_storage_size", columns="Initial_PV_size", values="Site_name")
# clinics_s3_hp # to show in Jupyter


# S3 CLINIC SIZES PLOT (Plotting data as it is)
ax = sns.heatmap(clinics_s3_hp, cmap="rocket_r", annot=True)  # vmin=1, vmax=4
ax.invert_yaxis()
ax.set_title("S3 - Clinics")
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


# SCENARIO 4 - GENERATING DF TO PLOT HEATMAPS OF SYSTEM SIZES OF CLINICS PER SCENARIO
# Imports csv of scenario I want
s4 = pd.read_csv("Optim_res_unmet_0.1_inst.csv")  # change to other scenarios

# Separate df to get df of clinics only
clinics_s4 = s4[s4.Institution != 'School']
# Groups clinics by Initial storage and PV size
clinics_s4 = clinics_s4.groupby(["Initial_storage_size","Initial_PV_size"])
# Counts unique site names to know number of sites per system size combination
clinics_s4_cnt = clinics_s4.Site_name.nunique()  # returns a series
clinics_s4_cnt.head()

# Convert series to df
clinics_s4_cnt_df = clinics_s4_cnt.to_frame()
# Pivot df so it has a wide-spread form
# clinics_s4_cnt_df # to show in Jupyter

# to check there are 18 clinics
clinics_s4_cnt_df["Site_name"].sum()  # returns 18
clinics_s4_cnt_df["Site_name"].describe().round(2)   # to know clinics min and max values (vmin & vmax)
                    # returns: min= 1 (vmin), max= 4 (vmax)

clinics_s4_hp = clinics_s4_cnt_df.reset_index().pivot(index="Initial_storage_size", columns="Initial_PV_size", values="Site_name")
# clinics_s4_hp # to show in Jupyter


# S4 CLINIC SIZES PLOT (Plotting data as it is)
ax = sns.heatmap(clinics_s4_hp, cmap="rocket_r", annot=True)
ax.invert_yaxis()
ax.set_title("S4 - Clinics")
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
# To make subplots with same axis use variables ending with _ext (e.g., clinics_s1_hp_ext)
# comment Rhino marker for initial plots 
fig, axes = plt.subplots(2, 2, figsize=(12, 8))  # The `figsize` is in inches and can be changed :)

# Python 3.7 etc. version
axis = axes[0, 0]   # top left
sns.heatmap(
    clinics_s1_hp, vmin=1, vmax=4, cmap="rocket_r", annot=True, cbar_kws={'ticks':[1, 2, 3, 4]},
    ax=axis,
)

# Code for writing titles etc.
axis.invert_yaxis()
axis.set_title("S1 - Clinics")
axis.set_ylabel("Storage size (kWh)")
axis.set_xlabel("") # PV size (kWp)
axis.set_xticklabels(axis.get_xticklabels(), rotation=45)
axis.set_yticklabels(axis.get_yticklabels(), rotation=0)
# to add Rhino as data point (marker by matrix coordinates - not x and y axis values):
axis.plot(8.5,9.5, marker="D", color= "black", ms="4")  # or "dimgrey"

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
    clinics_s2_hp, vmin=1, vmax=4, cmap="rocket_r", annot=True, cbar_kws={'ticks':[1, 2, 3, 4]},
    ax=axis,
)

# Code for writing titles etc.
axis.invert_yaxis()
axis.set_title("S2 - Clinics")
axis.set_ylabel("Storage size (kWh)")
axis.set_xlabel("") # PV size (kWp)
axis.set_xticklabels(axis.get_xticklabels(), rotation=45)
axis.set_yticklabels(axis.get_yticklabels(), rotation=0)
# to add Rhino as data point (marker by matrix coordinates - not x and y axis values):
axis.plot(8.5,9.5, marker="D", color= "black", ms="4")  # or "dimgrey"

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
    clinics_s3_hp, vmin=1, vmax=4, cmap="rocket_r", annot=True, cbar_kws={'ticks':[1, 2, 3, 4]},
    ax=axis,
)

# Code for writing titles etc.
axis.invert_yaxis()
axis.set_title("S3 - Clinics")
axis.set_ylabel("Storage size (kWh)")
axis.set_xlabel("PV size (kWp)")
axis.set_xticklabels(axis.get_xticklabels(), rotation=45)
axis.set_yticklabels(axis.get_yticklabels(), rotation=0)
# to add Rhino as data point (marker by matrix coordinates - not x and y axis values):
axis.plot(8.5,9.5, marker="D", color= "black", ms="4")  # or "dimgrey"

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
    clinics_s4_hp, vmin=1, vmax=4, cmap="rocket_r", annot=True, cbar_kws={'ticks':[1, 2, 3, 4]},
    ax=axis,
)

# Code for writing titles etc.
axis.invert_yaxis()
axis.set_title("S4 - Clinics")
axis.set_ylabel("Storage size (kWh)")
axis.set_xlabel("PV size (kWp)")
axis.set_xticklabels(axis.get_xticklabels(), rotation=45)
axis.set_yticklabels(axis.get_yticklabels(), rotation=0)
# to add Rhino as data point (marker by matrix coordinates - not x and y axis values):
axis.plot(8.5,9.5, marker="D", color= "black", ms="4")  # or "dimgrey"

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

# CHANGE DF TO EXTEND X AND Y AXIS AND REINDEX DF TO COMPARE PLOTS
# S1
clinics_s1_hp_ext = clinics_s1_hp.reindex(range(1,30), axis=0) # fill_value=0
clinics_s1_hp_ext = clinics_s1_hp_ext.reindex((np.arange(0.265, 6.095, 0.265)).round(3), axis=1)

# S2
clinics_s2_hp_ext = clinics_s2_hp.reindex(range(1,30), axis=0) # fill_value=0
clinics_s2_hp_ext = clinics_s2_hp_ext.reindex((np.arange(0.265, 6.095, 0.265)).round(3), axis=1)

# S3
clinics_s3_hp_ext = clinics_s3_hp.reindex(range(1,30), axis=0) # fill_value=0
clinics_s3_hp_ext = clinics_s3_hp_ext.reindex((np.arange(0.265, 6.095, 0.265)).round(3), axis=1)

# S4
clinics_s4_hp_ext = clinics_s4_hp.reindex(range(1,30), axis=0) # fill_value=0
clinics_s4_hp_ext = clinics_s4_hp_ext.reindex((np.arange(0.265, 6.095, 0.265)).round(3), axis=1)

# repeat plot above but changing variables to "_ext"

# See more on customising heatmap: https://www.python-graph-gallery.com/91-customize-seaborn-heatmap

# Customising heatmap
# sns.heatmap(df, yticklabels=False) # deletes yticks and y-axis line
# sns.heatmap(df, xticklabels=False)  # deletes xticks and x-axis line

# Other formatting options:
# ax.tick_params(left=False, bottom=False)
# g1.set(xticklabels=[])  # remove the tick labels
# g1.set(xlabel=None)  # remove the axis label

# Another option to add rhino as data point
# ax.text(2,10, "o")
# ax.text(6.5,6.5, "o")


# NOTES:
# Code for making subplots BW
#  https://gist.github.com/BenWinchester/b80dacf73507f05162f865fb04845359


# Export csv of clinics (not worth doing as when I reimport the data plotting doesn't work but just in case)
# sizes_clinics_hp.to_csv("sizes_clinics_hp_SCENARIO_NAME.csv") # change name depending on scenario
                                        # S1, S2, S3 or S4
