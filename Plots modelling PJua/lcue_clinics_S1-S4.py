# Created 20Mar23
# To create df of clinics system sizes for heatmaps of S1-S4 with mean LCUE
# Second part of this code is for plotting
# See Jupyter notebook: 'lcue_clinics_S1-S4'
# check outputs with excel: 'S0-S4 analysis and check'
# previous version of this code: 'trial_heatmap.py'


import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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
# to check there are 18 clinics
clinics_s1["Site_name"].count()  # returns 18
clinics_s1["LCUE"].describe().round(2)  # to know LCUE values (all clinics)
# clinics_s1 # to show in Jupyter

# LCUE:
# Groups clinics by Initial storage and PV size and calculates average LCUE in that bin
lcue_clinics_s1 = clinics_s1.groupby(["Initial_storage_size","Initial_PV_size"])["LCUE"].mean()

# Convert series to df
lcue_clinics_s1 = lcue_clinics_s1.to_frame()
# lcue_clinics_s1.round(3) # to show in Jupyter

# to know clinics min and max average LCUE values (vmin & vmax)
lcue_clinics_s1["LCUE"].describe().round(3)
                    # returns: min= 0.602 (vmin), max= 2.873 (vmax)
                    # returns count != than 18 because some sites have same size

# Pivot df to be able to do heatmap
lcue_clinics_s1_hp = lcue_clinics_s1.reset_index().pivot(index="Initial_storage_size", columns="Initial_PV_size", values="LCUE")
# lcue_clinics_s1_hp # to show in Jupyter


# Setting style for plotting
sns.set(rc={"figure.dpi":300})
sns.set_style("ticks")
#sns.set_context("paper")  # poster

# S1 CLINIC LCUE PLOT (to plot data as it is - delete vmin and vmax for raw plot)
ax = sns.heatmap(lcue_clinics_s1_hp, vmin=0.5, vmax=3, cmap="gist_heat_r")  # (annot=True, fmt=".3g") but format the values
ax.invert_yaxis()
ax.set_title("S1 - Clinics average LCUE ($/kWh)")
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

# try plotting with variable: "lcue_clinics_s1_hp_ext"

# SCENARIO 2 - GENERATING DF TO PLOT HEATMAPS OF SYSTEM SIZES OF CLINICS PER SCENARIO
# Imports csv of scenario I want
s2 = pd.read_csv("Optim_res_unmet_0.01_inst.csv")  # change to other scenarios

# Separate df to get df of clinics only
clinics_s2 = s2[s2.Institution != 'School']
# to check there are 18 clinics
clinics_s2["Site_name"].count()  # returns 18
clinics_s2["LCUE"].describe().round(2)  # to know LCUE values (all clinics)
# clinics_s2 # to show in Jupyter

# LCUE:
# Groups clinics by Initial storage and PV size and calculates average LCUE in that bin
lcue_clinics_s2 = clinics_s2.groupby(["Initial_storage_size","Initial_PV_size"])["LCUE"].mean()

# Convert series to df
lcue_clinics_s2 = lcue_clinics_s2.to_frame()
# lcue_clinics_s2.round(3) # to show in Jupyter

# to know clinics min and max average LCUE values (vmin & vmax)
lcue_clinics_s2["LCUE"].describe().round(3)
                    # returns: min= 0.475 (vmin), max= 2.468 (vmax)
                    # returns count != than 18 because some sites have same size

# Pivot df to be able to do heatmap
lcue_clinics_s2_hp = lcue_clinics_s2.reset_index().pivot(index="Initial_storage_size", columns="Initial_PV_size", values="LCUE")
# lcue_clinics_s2_hp # to show in Jupyter

# S2 CLINIC SIZES PLOT (Plotting data as it is)
ax = sns.heatmap(lcue_clinics_s2_hp, vmin=0.4, vmax=3, cmap="gist_heat_r", annot=True) #
ax.invert_yaxis()
ax.set_title("S2 - Clinics average LCUE ($/kWh)")
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

# to check there are 18 clinics
clinics_s3["Site_name"].count()  # returns 18
clinics_s3["LCUE"].describe().round(2)  # to know LCUE values (all clinics)
# clinics_s3 # to show in Jupyter

# LCUE:
# Groups clinics by Initial storage and PV size and calculates average LCUE in that bin
lcue_clinics_s3 = clinics_s3.groupby(["Initial_storage_size","Initial_PV_size"])["LCUE"].mean()

# Convert series to df
lcue_clinics_s3 = lcue_clinics_s3.to_frame()
# lcue_clinics_s3.round(3) # to show in Jupyter

# to know clinics min and max average LCUE values (vmin & vmax)
lcue_clinics_s3["LCUE"].describe().round(3)
                    # returns: min=0.42  (vmin), max= 2.005 (vmax)
                    # returns count != than 18 because some sites have same size

# Pivot df to be able to do heatmap
lcue_clinics_s3_hp = lcue_clinics_s3.reset_index().pivot(index="Initial_storage_size", columns="Initial_PV_size", values="LCUE")
# lcue_clinics_s3_hp.round(3) # to show in Jupyter

# S3 CLINIC SIZES PLOT (Plotting data as it is)
ax = sns.heatmap(lcue_clinics_s3_hp, vmin=0.4, vmax=2, cmap="gist_heat_r")  # annot=True
ax.invert_yaxis()
ax.set_title("S3 - Clinics average LCUE ($/kWh)")
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

# to check there are 18 clinics
clinics_s4["Site_name"].count()  # returns 18
clinics_s4["LCUE"].describe().round(2)  # to know LCUE values (all clinics)
# clinics_s4 # to show in Jupyter

# LCUE:
# Groups clinics by Initial storage and PV size and calculates average LCUE in that bin
lcue_clinics_s4 = clinics_s4.groupby(["Initial_storage_size","Initial_PV_size"])["LCUE"].mean()

# Convert series to df
lcue_clinics_s4 = lcue_clinics_s4.to_frame()
# lcue_clinics_s4.round(3) # to show in Jupyter

# to know clinics min and max average LCUE values (vmin & vmax)
lcue_clinics_s4["LCUE"].describe().round(3)
                    # returns: min=0.416  (vmin), max= 1.808 (vmax)
                    # returns count != than 18 because some sites have same size

# Pivot df to be able to do heatmap
lcue_clinics_s4_hp = lcue_clinics_s4.reset_index().pivot(index="Initial_storage_size", columns="Initial_PV_size", values="LCUE")
# lcue_clinics_s4_hp.round(3) # to show in Jupyter

# S4 CLINIC SIZES PLOT (Plotting data as it is)
ax = sns.heatmap(lcue_clinics_s4_hp, vmin=0.3, vmax=2, cmap="gist_heat_r")  # annot=True
ax.invert_yaxis()
ax.set_title("S4 - Clinics average LCUE ($/kWh)")
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
# To make subplots with same axis use variables ending with _ext (e.g., lcue_clinics_s1_hp_ext)
# comment Rhino marker for initial plots
fig, axes = plt.subplots(2, 2, figsize=(12, 8))  # The `figsize` is in inches and can be changed :)

# Python 3.7 etc. version
axis = axes[0, 0]   # top left
sns.heatmap(
    lcue_clinics_s1_hp, vmin=0.3, vmax=3, cmap="gist_heat_r", annot=True,
    ax=axis,
)

# Code for writing titles etc.
axis.invert_yaxis()
axis.set_title("S1 - Clinics average LCUE ($/kWh)")
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
    lcue_clinics_s2_hp, vmin=0.3, vmax=3, cmap="gist_heat_r", annot=True,
    ax=axis,
)

# Code for writing titles etc.
axis.invert_yaxis()
axis.set_title("S2 - Clinics average LCUE ($/kWh)")
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
    lcue_clinics_s3_hp, vmin=0.3, vmax=3, cmap="gist_heat_r", annot=True,
    ax=axis,
)

# Code for writing titles etc.
axis.invert_yaxis()
axis.set_title("S3 - Clinics average LCUE ($/kWh)")
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
    lcue_clinics_s4_hp, vmin=0.3, vmax=3, cmap="gist_heat_r", annot=True,
    ax=axis,
)

# Code for writing titles etc.
axis.invert_yaxis()
axis.set_title("S4 - Clinics average LCUE ($/kWh)")
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

# CHANGE DF TO EXTEND X AND Y AXIS AND REINDEX DF TO COMPARE PLOTS ACROSS SCENARIOS
# S1
lcue_clinics_s1_hp_ext = lcue_clinics_s1_hp.reindex(range(1,30), axis=0) # fill_value=0
lcue_clinics_s1_hp_ext = lcue_clinics_s1_hp_ext.reindex((np.arange(0.265, 6.095, 0.265)).round(3), axis=1)

# S2
lcue_clinics_s2_hp_ext = lcue_clinics_s2_hp.reindex(range(1,30), axis=0) # fill_value=0
lcue_clinics_s2_hp_ext = lcue_clinics_s2_hp_ext.reindex((np.arange(0.265, 6.095, 0.265)).round(3), axis=1)

# S3
lcue_clinics_s3_hp_ext = lcue_clinics_s3_hp.reindex(range(1,30), axis=0) # fill_value=0
lcue_clinics_s3_hp_ext = lcue_clinics_s3_hp_ext.reindex((np.arange(0.265, 6.095, 0.265)).round(3), axis=1)

# S4
lcue_clinics_s4_hp_ext = lcue_clinics_s4_hp.reindex(range(1,30), axis=0) # fill_value=0
lcue_clinics_s4_hp_ext = lcue_clinics_s4_hp_ext.reindex((np.arange(0.265, 6.095, 0.265)).round(3), axis=1)

# repeat plot above but changing variables to "_ext"

# other colours I like: "magma_r", "gist_heat_r", "Oranges"

# to save image
#plt.tight_layout()
#plt.savefig('finalname.png', dpi=120)
