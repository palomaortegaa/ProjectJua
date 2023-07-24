# Created 20Mar23
# To create df of clinics system sizes for heatmaps of S1-S4 with mean emissions intensity
# Second part of this code is for plotting
# See Jupyter notebook: 'emi_clinics_S1-S4'
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
clinics_s1["Emissions_intensity"].describe().round(2)  # to know emissions values (all clinics)
# clinics_s1 # to show in Jupyter

# Emissions intensity
# Groups clinics by Initial storage and PV size and calculates average emi in that bin
emi_clinics_s1 = clinics_s1.groupby(["Initial_storage_size","Initial_PV_size"])["Emissions_intensity"].mean()

# Convert series to df
emi_clinics_s1 = emi_clinics_s1.to_frame()
# emi_clinics_s1.round(2) # to show in Jupyter

# to know clinics min and max average emi values (vmin & vmax)
emi_clinics_s1["Emissions_intensity"].describe().round(3)
                    # returns: min= 243.687  (vmin), max= 1252.262 (vmax)
                    # returns count != than 18 because some sites have same size

# Pivot df to be able to do heatmap
emi_clinics_s1_hp = emi_clinics_s1.reset_index().pivot(index="Initial_storage_size", columns="Initial_PV_size", values="Emissions_intensity")
# emi_clinics_s1_hp.round(2) # to show in Jupyter


# Setting style for plotting
sns.set(rc={"figure.dpi":300})
sns.set_style("ticks")
#sns.set_context("paper")  # poster

# S1 CLINIC emi PLOT (to plot data as it is - delete vmin and vmax for raw plot)
ax = sns.heatmap(emi_clinics_s1_hp, vmin=200, vmax=1300, cmap="YlGnBu")  # (annot=True, fmt=".0f") but format the values
ax.invert_yaxis()
ax.set_title("S1 - Clinics average emissions intensity (gCO2/kWh)")
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

# at the end try plotting with variable: "emi_clinics_s1_hp_ext"

# SCENARIO 2 - GENERATING DF TO PLOT HEATMAPS OF SYSTEM SIZES OF CLINICS PER SCENARIO
# Imports csv of scenario I want
s2 = pd.read_csv("Optim_res_unmet_0.01_inst.csv")  # change to other scenarios

# Separate df to get df of clinics only
clinics_s2 = s2[s2.Institution != 'School']
# to check there are 18 clinics
clinics_s2["Site_name"].count()  # returns 18
clinics_s2["Emissions_intensity"].describe().round(2)  # to know emissions values (all clinics)
# clinics_s2 # to show in Jupyter

# Emissions intensity
# Groups clinics by Initial storage and PV size and calculates average emi in that bin
emi_clinics_s2 = clinics_s2.groupby(["Initial_storage_size","Initial_PV_size"])["Emissions_intensity"].mean()

# Convert series to df
emi_clinics_s2 = emi_clinics_s2.to_frame()
# emi_clinics_s2.round(2) # to show in Jupyter

# to know clinics min and max average emi values (vmin & vmax)
emi_clinics_s2["Emissions_intensity"].describe().round(3)
                    # returns: min= 174.523 (vmin), max= 927.531 (vmax)
                    # returns count != than 18 because some sites have same size

# Pivot df to be able to do heatmap
emi_clinics_s2_hp = emi_clinics_s2.reset_index().pivot(index="Initial_storage_size", columns="Initial_PV_size", values="Emissions_intensity")
# emi_clinics_s2_hp.round(2) # to show in Jupyter

# S2 CLINIC SIZES PLOT (Plotting data as it is)
ax = sns.heatmap(emi_clinics_s2_hp, vmin=150, vmax=1000, cmap="YlGnBu")  # (annot=True, fmt=".0f") but format the values
ax.invert_yaxis()
ax.set_title("S2 - Clinics average emissions intensity (gCO2/kWh)")
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
clinics_s3["Emissions_intensity"].describe().round(2)  # to know emi values (all clinics)
# clinics_s3 # to show in Jupyter

# Emissions intensity
# Groups clinics by Initial storage and PV size and calculates average emi in that bin
emi_clinics_s3 = clinics_s3.groupby(["Initial_storage_size","Initial_PV_size"])["Emissions_intensity"].mean()

# Convert series to df
emi_clinics_s3 = emi_clinics_s3.to_frame()
# emi_clinics_s3.round(2) # to show in Jupyter

# to know clinics min and max average emi values (vmin & vmax)
emi_clinics_s3["Emissions_intensity"].describe().round(3)
                    # returns: min= 133.966 (vmin), max= 804.086 (vmax)
                    # returns count != than 18 because some sites have same size

# Pivot df to be able to do heatmap
emi_clinics_s3_hp = emi_clinics_s3.reset_index().pivot(index="Initial_storage_size", columns="Initial_PV_size", values="Emissions_intensity")
# emi_clinics_s3_hp.round(2) # to show in Jupyter

# S3 CLINIC SIZES PLOT (Plotting data as it is)
ax = sns.heatmap(emi_clinics_s3_hp, vmin=100, vmax=900, cmap="YlGnBu")  # (annot=True, fmt=".0f") but format the values
ax.invert_yaxis()
ax.set_title("S3 - Clinics average emissions intensity (gCO2/kWh)")
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
clinics_s4["Emissions_intensity"].describe().round(2)  # to know emi values (all clinics)
# clinics_s4 # to show in Jupyter

# Emissions intensity
# Groups clinics by Initial storage and PV size and calculates average emi in that bin
emi_clinics_s4 = clinics_s4.groupby(["Initial_storage_size","Initial_PV_size"])["Emissions_intensity"].mean()

# Convert series to df
emi_clinics_s4 = emi_clinics_s4.to_frame()
# emi_clinics_s4.round(2) # to show in Jupyter

# to know clinics min and max average emi values (vmin & vmax)
emi_clinics_s4["Emissions_intensity"].describe().round(3)
                    # returns: min= 142.168 (vmin), max= 759.693 (vmax)
                    # returns count != than 18 because some sites have same size

# Pivot df to be able to do heatmap
emi_clinics_s4_hp = emi_clinics_s4.reset_index().pivot(index="Initial_storage_size", columns="Initial_PV_size", values="Emissions_intensity")
# emi_clinics_s4_hp.round(2) # to show in Jupyter

# S4 CLINIC SIZES PLOT (Plotting data as it is)
ax = sns.heatmap(emi_clinics_s4_hp, vmin=100, vmax=800, cmap="YlGnBu")  # (annot=True, fmt=".0f") but format the values
ax.invert_yaxis()
ax.set_title("S4 - Clinics average emissions intensity (gCO2/kWh)")
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
# To make subplots with same axis use variables ending with _ext (e.g., emi_clinics_s1_hp_ext)
# comment Rhino marker for initial plots
fig, axes = plt.subplots(2, 2, figsize=(12, 8))  # The `figsize` is in inches and can be changed :)

# Python 3.7 etc. version
axis = axes[0, 0]   # top left
sns.heatmap(
    emi_clinics_s1_hp, vmin=100, vmax=1300, cmap="YlGnBu", annot=True, fmt=".0f",
    ax=axis,
)

# Code for writing titles etc.
axis.invert_yaxis()
axis.set_title("S1 - Clinics average emissions intensity (gCO2/kWh)")
axis.set_ylabel("Storage size (kWh)")
axis.set_xlabel("") # PV size (kWp)
axis.set_xticklabels(axis.get_xticklabels(), rotation=45)
axis.set_yticklabels(axis.get_yticklabels(), rotation=0)
# to add Rhino as data point (marker by matrix coordinates - not x and y axis values):
# axis.plot(8.5,9.5, marker="D", color= "black", ms="4")  # or "dimgrey"

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
    emi_clinics_s2_hp, vmin=100, vmax=1300, cmap="YlGnBu", annot=True, fmt=".0f",
    ax=axis,
)

# Code for writing titles etc.
axis.invert_yaxis()
axis.set_title("S2 - Clinics average emissions intensity (gCO2/kWh)")
axis.set_ylabel("Storage size (kWh)")
axis.set_xlabel("") # PV size (kWp)
axis.set_xticklabels(axis.get_xticklabels(), rotation=45)
axis.set_yticklabels(axis.get_yticklabels(), rotation=0)
# to add Rhino as data point (marker by matrix coordinates - not x and y axis values):
# axis.plot(8.5,9.5, marker="D", color= "black", ms="4")  # or "dimgrey"

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
    emi_clinics_s3_hp, vmin=100, vmax=1300, cmap="YlGnBu", annot=True, fmt=".0f",
    ax=axis,
)

# Code for writing titles etc.
axis.invert_yaxis()
axis.set_title("S3 - Clinics average emissions intensity (gCO2/kWh)")
axis.set_ylabel("Storage size (kWh)")
axis.set_xlabel("PV size (kWp)")
axis.set_xticklabels(axis.get_xticklabels(), rotation=45)
axis.set_yticklabels(axis.get_yticklabels(), rotation=0)
# to add Rhino as data point (marker by matrix coordinates - not x and y axis values):
# axis.plot(8.5,9.5, marker="D", color= "black", ms="4")  # or "dimgrey"

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
    emi_clinics_s4_hp, vmin=100, vmax=1300, cmap="YlGnBu", annot=True, fmt=".0f",
    ax=axis,
)

# Code for writing titles etc.
axis.invert_yaxis()
axis.set_title("S4 - Clinics average emissions intensity (gCO2/kWh)")
axis.set_ylabel("Storage size (kWh)")
axis.set_xlabel("PV size (kWp)")
axis.set_xticklabels(axis.get_xticklabels(), rotation=45)
axis.set_yticklabels(axis.get_yticklabels(), rotation=0)
# to add Rhino as data point (marker by matrix coordinates - not x and y axis values):
# axis.plot(8.5,9.5, marker="D", color= "black", ms="4")  # or "dimgrey"

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
emi_clinics_s1_hp_ext = emi_clinics_s1_hp.reindex(range(1,30), axis=0) # fill_value=0
emi_clinics_s1_hp_ext = emi_clinics_s1_hp_ext.reindex((np.arange(0.265, 6.095, 0.265)).round(3), axis=1)

# S2
emi_clinics_s2_hp_ext = emi_clinics_s2_hp.reindex(range(1,30), axis=0) # fill_value=0
emi_clinics_s2_hp_ext = emi_clinics_s2_hp_ext.reindex((np.arange(0.265, 6.095, 0.265)).round(3), axis=1)

# S3
emi_clinics_s3_hp_ext = emi_clinics_s3_hp.reindex(range(1,30), axis=0) # fill_value=0
emi_clinics_s3_hp_ext = emi_clinics_s3_hp_ext.reindex((np.arange(0.265, 6.095, 0.265)).round(3), axis=1)

# S4
emi_clinics_s4_hp_ext = emi_clinics_s4_hp.reindex(range(1,30), axis=0) # fill_value=0
emi_clinics_s4_hp_ext = emi_clinics_s4_hp_ext.reindex((np.arange(0.265, 6.095, 0.265)).round(3), axis=1)

# repeat plot above but changing variables to "_ext"

# other colours I like: "magma_r", "gist_heat_r", "Oranges"
# other colour options: "YlGn", "YlGnBu", "summer_r"

# to save image
#plt.tight_layout()
#plt.savefig('finalname.png', dpi=120)
