# Created 7Apr23
# Imports csv of S0 (PJua simulation results) and LCUE & Emissions df generated before
# Selects subset of sites with Unmet_energy_fraction == 0 from S0 (124 sites)
# Saves them in a list to be able to plot only subset of those sites LCUE and emissions
# Separates by institution type too
# check Jupyter notebook version: 'subset_unmet0'
# check excel: 'S0-S4 analysis and check'
# plots to add in Ch. 4 analysis

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Move to path where csv are saved
path = "/Users/po416/Library/CloudStorage/OneDrive-ImperialCollegeLondon/PhDOct2018/Projects (12Mar20)/Project Jua/Modelling PJua analysis/Results_outputs"

cwd = os.getcwd()
cwd

os.chdir(path) # or put the whole path
os.getcwd()   # or put pwd

# Imports/reads csv of S0 to look for sites with Unmet_energy_fraction of 0
s0 = pd.read_csv("Simu_res_S0_inst.csv")

# Get new df with subset of data based on a condition of a column
# in this case is the sites of Unmet_energy_fraction == 0
subset_df = s0[s0["Unmet_energy_fraction"] == 0]

# Save the Site_name of sites in this subset as a list
subset_list = subset_df.Site_name.values.tolist()
print(subset_list)    # should be 124 in this case (124 sites with unmet of 0 in S0)

# Imports/reads csv of LCUE of S0-S4 (created with another code)
lcue_s0_s4 = pd.read_csv("lcue_s0_s4.csv")

# Creates new df including only subset of sites on subset_list:
lcue_subset = lcue_s0_s4[lcue_s0_s4["Site_name"].isin(subset_list)]
# lcue_subset # to show in Jupyter

# Set style to plot
sns.set(rc={"figure.dpi":300})
sns.set_context("notebook")
#sns.set_style("ticks") # with axis ticks, no background lines
sns.set_style("whitegrid") # no axis ticks, with background lines

# Plot subset of LCUE sites that had Unmet_energy_fraction == 0 in S0 (124 sites)
g = sns.catplot(
    data=lcue_subset, kind= "box", palette= "Set2")  # change to violin
g.set(xlabel= "Scenarios", ylabel= "LCUE ($/kWh)")
#g.set(ylim=(0, 3)) # to get rid of outlier
g.set_xticklabels(["S0", "S1", "S2", "S3", "S4"])
g.set(title="Subset")
sns.despine(top=False, right=False)

# Separate df by Institution type (by Clinics LCUE)
lcue_subset_clinics = lcue_subset[lcue_subset.Institution != 'School']

# returns LCUE df of only clinics (13 sites/count)
lcue_subset_clinics.describe().round(3)

# Plot subset of LCUE clinics
g = sns.catplot(
    data=lcue_subset_clinics, kind= "box", palette= "Set2")  # change to violin
g.set(xlabel= "Scenarios", ylabel= "LCUE ($/kWh)")
#g.set(ylim=(0, 3)) # to get rid of outlier
g.set_xticklabels(["S0", "S1", "S2", "S3", "S4"])
g.set(title="Clinics subset")
sns.despine(top=False, right=False)

# to separate df by Institution type (by Schools LCUE)
lcue_subset_schools = lcue_subset[lcue_subset.Institution != 'Clinic']

# returns LCUE df of only schools (111 sites/count)
lcue_subset_schools.describe().round(3)


# Plot subset of LCUE schools
g = sns.catplot(
    data=lcue_subset_schools, kind= "box", palette= "Set2")
g.set(xlabel= "Scenarios", ylabel= "LCUE ($/kWh)")
#g.set(ylim=(0, 3)) # to get rid of outlier
g.set_xticklabels(["S0", "S1", "S2", "S3", "S4"])
g.set(title="Schools subset")
sns.despine(top=False, right=False)

# NOW REPEAT FOR EMISSIONS INTENSITY
# Imports/reads csv of Emissions intensity of S0-S4 (created with another code)
emi_s0_s4 = pd.read_csv("emi_s0_s4.csv")

# Creates new df including only subset of sites on subset_list:
emi_subset = emi_s0_s4[emi_s0_s4["Site_name"].isin(subset_list)]
# emi_subset # to show in Jupyter

# Plot subset of Emissions_int sites that had Unmet_energy_fraction == 0 in S0 (124 sites)
g = sns.catplot(
    data=emi_subset, kind= "box", palette= "Set2")
g.set(xlabel= "Scenarios", ylabel= "Emissions intensity (gCO2/kWh)")
#g.set(ylim=(0, 3)) # to get rid of outlier
g.set_xticklabels(["S0", "S1", "S2", "S3", "S4"])
g.set(title="Subset")
sns.despine(top=False, right=False)

# Separate df by Institution type (by Clinics emissions intensity)
emi_subset_clinics = emi_subset[emi_subset.Institution != 'School']
emi_subset_clinics

# returns Emissions intensity df of only clinics (13 sites/count)
emi_subset_clinics.describe().round(3)

# Plot it (see Jupyter notebook 'subset_unmet0')

# to separate df by Institution type (by Schools Emissions intensity)
emi_subset_schools = emi_subset[emi_subset.Institution != 'Clinic']

# returns Emissions intensity df of only schools (111 sites/count)
emi_subset_schools.describe().round(3)

# Plot it (see Jupyter notebook 'subset_unmet0')

# Notes:
# Another way of choosing subset of data (by adding ~) but in this case it will return
# 42 sites (instead of 124) which are the ones that had an Unmet_energy_fraction != 0 in S0
output_df = lcue_s0_s4[~lcue_s0_s4["Site_name"].isin(subset_list)]
          # returns the other 42

# Do it for emissions and plot it, save plots and do Jupyter version of this
