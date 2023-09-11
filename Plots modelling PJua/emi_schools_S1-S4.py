# Created 21Mar23
# To create df of schools system sizes for heatmaps of S1-S4 with mean emissions intensity
# Second part of this code is for plotting
# See Jupyter notebook: 'emi_schools_S1-S4'
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

# SCENARIO 1 - GENERATING DF TO PLOT HEATMAPS OF SYSTEM SIZES OF SCHOOLS PER SCENARIO
# Imports csv of scenario I want
s1 = pd.read_csv("Optim_res_unmet_0_inst.csv")  # change to other scenarios

# Separate df to get df of schools only
schools_s1 = s1[s1.Institution != 'Clinic']

# to check there are 148 schools
schools_s1["Site_name"].count()  # returns 148
schools_s1["Emissions_intensity"].describe().round(2)  # to know emi values (all schools)
# schools_s1 # to show in Jupyter

# Emissions intensity
# Groups schools by Initial storage and PV size and calculates average emi in that bin
emi_schools_s1 = schools_s1.groupby(["Initial_storage_size","Initial_PV_size"])["Emissions_intensity"].mean()

# Convert series to df
emi_schools_s1 = emi_schools_s1.to_frame()
# emi_schools_s1.round(2) # to show in Jupyter

# to know schools min and max average emi values (vmin & vmax)
emi_schools_s1["Emissions_intensity"].describe().round(3)
                    # returns: min= 219.135 (vmin), max= 1582.407 (vmax)
                    # returns count != than 148 because some sites have same size

# Pivot df to be able to do heatmap
emi_schools_s1_hp = emi_schools_s1.reset_index().pivot(index="Initial_storage_size", columns="Initial_PV_size", values="Emissions_intensity")
# emi_schools_s1_hp.round(2) # to show in Jupyter


# Setting style for plotting
sns.set(rc={"figure.dpi":300})
sns.set_style("ticks")
#sns.set_context("paper")  # poster

# S1 SCHOOL emi PLOT (to plot data as it is - delete vmin and vmax for raw plot)
ax = sns.heatmap(emi_schools_s1_hp, vmin=200, vmax=1600, cmap="Greens")  # (annot=True, fmt=".0f") but format the values
ax.invert_yaxis()
ax.set_title("S1 - Schools average emissions intensity (gCO2/kWh)")
ax.set_ylabel("Storage size (kWh)")
ax.set_xlabel("PV size (kWp)")
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
ax.set_yticklabels(ax.get_yticklabels(), rotation=0)
# to add Impala as data point (marker by matrix coordinates - not x and y axis values):
# ax.plot(3.5,5.1, marker="D", color= "black", ms="4")

# Drawing the frame
for _, spine in ax.spines.items():
    spine.set_visible(True)
    spine.set_linewidth(1)

# show plot
# plt.tight_layout()
plt.show()

# at the end try plotting with variable: "emi_schools_s1_hp_ext"

# SCENARIO 2 - GENERATING DF TO PLOT HEATMAPS OF SYSTEM SIZES OF SCHOOLS PER SCENARIO
# Imports csv of scenario I want
s2 = pd.read_csv("Optim_res_unmet_0.01_inst.csv")  # change to other scenarios

# Separate df to get df of schools only
schools_s2 = s2[s2.Institution != 'Clinic']
# to check there are 148 schools
schools_s2["Site_name"].count()  # returns 148
schools_s2["Emissions_intensity"].describe().round(2)  # to know emi values (all schools)
# schools_s2 # to show in Jupyter

# Emissions intensity
# Groups schools by Initial storage and PV size and calculates average emi in that bin
emi_schools_s2 = schools_s2.groupby(["Initial_storage_size","Initial_PV_size"])["Emissions_intensity"].mean()

# Convert series to df
emi_schools_s2 = emi_schools_s2.to_frame()
# emi_schools_s2.round(2) # to show in Jupyter

# to know schools min and max average emi values (vmin & vmax)
emi_schools_s2["Emissions_intensity"].describe().round(3)
                    # returns: min= 172.850 (vmin), max= 1512.607 (vmax)
                    # returns count != than 148 because some sites have same size

# Pivot df to be able to do heatmap
emi_schools_s2_hp = emi_schools_s2.reset_index().pivot(index="Initial_storage_size", columns="Initial_PV_size", values="Emissions_intensity")
# emi_schools_s2_hp.round(2) # to show in Jupyter

# S2 SCHOOL SIZES PLOT (Plotting data as it is)
ax = sns.heatmap(emi_schools_s2_hp, vmin=100, vmax=1600, cmap="Greens")  # (annot=True, fmt=".0f") but format the values
ax.invert_yaxis()
ax.set_title("S2 - Schools average emissions intensity (gCO2/kWh)")
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

# to check there are 148 schools
schools_s3["Site_name"].count()  # returns 148
schools_s3["Emissions_intensity"].describe().round(2)  # to know emi values (all schools)
# schools_s3 # to show in Jupyter

# Emissions intensity
# Groups schools by Initial storage and PV size and calculates average emi in that bin
emi_schools_s3 = schools_s3.groupby(["Initial_storage_size","Initial_PV_size"])["Emissions_intensity"].mean()

# Convert series to df
emi_schools_s3 = emi_schools_s3.to_frame()
# emi_schools_s3.round(2) # to show in Jupyter

# to know schools min and max average emi values (vmin & vmax)
emi_schools_s3["Emissions_intensity"].describe().round(3)
                    # returns: min= 163.654 (vmin), max= 437.455  (vmax)
                    # returns count != than 148 because some sites have same size

# Pivot df to be able to do heatmap
emi_schools_s3_hp = emi_schools_s3.reset_index().pivot(index="Initial_storage_size", columns="Initial_PV_size", values="Emissions_intensity")
# emi_schools_s3_hp.round(2) # to show in Jupyter

# S3 SCHOOL SIZES PLOT (Plotting data as it is)
ax = sns.heatmap(emi_schools_s3_hp, vmin=100, vmax=500, cmap="Greens")  # (annot=True, fmt=".0f") but format the values
ax.invert_yaxis()
ax.set_title("S3 - Schools average emissions intensity (gCO2/kWh)")
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

# to check there are 148 schools
schools_s4["Site_name"].count()  # returns 148
schools_s4["Emissions_intensity"].describe().round(2)  # to know emi values (all schools)
# schools_s4 # to show in Jupyter

# Emissions intensity
# Groups schools by Initial storage and PV size and calculates average emi in that bin
emi_schools_s4 = schools_s4.groupby(["Initial_storage_size","Initial_PV_size"])["Emissions_intensity"].mean()

# Convert series to df
emi_schools_s4 = emi_schools_s4.to_frame()
# emi_schools_s4.round(2) # to show in Jupyter

# to know schools min and max average emi values (vmin & vmax)
emi_schools_s4["Emissions_intensity"].describe().round(3)
                    # returns: min= 141.542 (vmin), max= 440.792 (vmax)
                    # returns count != than 148 because some sites have same size

# Pivot df to be able to do heatmap
emi_schools_s4_hp = emi_schools_s4.reset_index().pivot(index="Initial_storage_size", columns="Initial_PV_size", values="Emissions_intensity")
# emi_schools_s4_hp.round(2) # to show in Jupyter

# S4 SCHOOL SIZES PLOT (Plotting data as it is)
ax = sns.heatmap(emi_schools_s4_hp, vmin=100, vmax=500, cmap="Greens")  # (annot=True, fmt=".0f") but format the values
ax.invert_yaxis()
ax.set_title("S4 - Schools average emissions intensity (gCO2/kWh)")
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
# To make subplots with same axis use variables ending with '_ext' (e.g., emi_schools_s1_hp_ext)
# comment Impala marker for initial plots
fig, axes = plt.subplots(2, 2, figsize=(12, 8))  # The `figsize` is in inches and can be changed :)

# Python 3.7 etc. version
axis = axes[0, 0]   # top left
sns.heatmap(
    emi_schools_s1_hp, vmin=50, vmax=1600, cmap="Greens", annot=True, fmt=".0f",
    ax=axis,
)

# Code for writing titles etc.
axis.invert_yaxis()
axis.set_title("S1 - Schools average emissions intensity (gCO2/kWh)")
axis.set_ylabel("Storage size (kWh)")
axis.set_xlabel("") # PV size (kWp)
axis.set_xticklabels(axis.get_xticklabels(), rotation=45)
axis.set_yticklabels(axis.get_yticklabels(), rotation=0)
# to add Impala as data point (marker by matrix coordinates - not x and y axis values):
# axis.plot(3.5,5.1, marker="D", color= "black", ms="4")

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
    emi_schools_s2_hp, vmin=50, vmax=1600, cmap="Greens", annot=True, fmt=".0f",
    ax=axis,
)

# Code for writing titles etc.
axis.invert_yaxis()
axis.set_title("S2 - Schools average emissions intensity (gCO2/kWh)")
axis.set_ylabel("Storage size (kWh)")
axis.set_xlabel("") # PV size (kWp)
axis.set_xticklabels(axis.get_xticklabels(), rotation=45)
axis.set_yticklabels(axis.get_yticklabels(), rotation=0)
# to add Impala as data point (marker by matrix coordinates - not x and y axis values):
# axis.plot(3.5,5.1, marker="D", color= "black", ms="4")

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
    emi_schools_s3_hp, vmin=50, vmax=1600, cmap="Greens", annot=True, fmt=".0f",
    ax=axis,
)

# Code for writing titles etc.
axis.invert_yaxis()
axis.set_title("S3 - Schools average emissions intensity (gCO2/kWh)")
axis.set_ylabel("Storage size (kWh)")
axis.set_xlabel("PV size (kWp)")
axis.set_xticklabels(axis.get_xticklabels(), rotation=45)
axis.set_yticklabels(axis.get_yticklabels(), rotation=0)
# to add Impala as data point (marker by matrix coordinates - not x and y axis values):
# axis.plot(3.5,5.1, marker="D", color= "black", ms="4")

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
    emi_schools_s4_hp, vmin=50, vmax=1600, cmap="Greens", annot=True, fmt=".0f",
    ax=axis,
)

# Code for writing titles etc.
axis.invert_yaxis()
axis.set_title("S4 - Schools average emissions intensity (gCO2/kWh)")
axis.set_ylabel("Storage size (kWh)")
axis.set_xlabel("PV size (kWp)")
axis.set_xticklabels(axis.get_xticklabels(), rotation=45)
axis.set_yticklabels(axis.get_yticklabels(), rotation=0)
# to add Impala as data point (marker by matrix coordinates - not x and y axis values):
# axis.plot(3.5,5.1, marker="D", color= "black", ms="4")

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
emi_schools_s1_hp_ext = emi_schools_s1_hp.reindex(range(1,15), axis=0) # fill_value=0
emi_schools_s1_hp_ext = emi_schools_s1_hp_ext.reindex((np.arange(0.265, 3.71, 0.265)).round(3), axis=1)

# S2
emi_schools_s2_hp_ext = emi_schools_s2_hp.reindex(range(1,15), axis=0) # fill_value=0
emi_schools_s2_hp_ext = emi_schools_s2_hp_ext.reindex((np.arange(0.265, 3.71, 0.265)).round(3), axis=1)

# S3
emi_schools_s3_hp_ext = emi_schools_s3_hp.reindex(range(1,15), axis=0) # fill_value=0
emi_schools_s3_hp_ext = emi_schools_s3_hp_ext.reindex((np.arange(0.265, 3.71, 0.265)).round(3), axis=1)

# S4
emi_schools_s4_hp_ext = emi_schools_s4_hp.reindex(range(1,15), axis=0) # fill_value=0
emi_schools_s4_hp_ext = emi_schools_s4_hp_ext.reindex((np.arange(0.265, 3.71, 0.265)).round(3), axis=1)

# repeat plot above but changing variables to "_ext"

# other colours I like: "magma_r", "gist_heat_r", "Oranges"


# to save image
#plt.tight_layout()
#plt.savefig('finalname.png', dpi=120)
