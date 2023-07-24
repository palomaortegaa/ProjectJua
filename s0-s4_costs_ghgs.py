# Created 2Mar23
# Imports csv with PJua scenarios modelling results, builds new df with LCUE,
# emissions intensity, cumu system costs and GHG for each scenario for all 166
# sites, exports csv with S0-S4 results per metric and plots LCUE as trial
# check Jupyter notebook for plots of LCUE: 'lcue_s0-s4_plots' and of other
# metrics: 'emissions_s0-s4_plots'; 'cumsys_cost_s0-s4_plots'; 'cumsys_ghg_s0-s4_plots'
# with this code i did plots on 'Modelling prel results' PJua ppt

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
pwd

# Imports/reads csv of each scenario
s0 = pd.read_csv("Simu_res_S0_inst.csv")
s1 = pd.read_csv("Optim_res_unmet_0_inst.csv") # maybe use different csv w/out Institution column
s2 = pd.read_csv("Optim_res_unmet_0.01_inst.csv")
s3 = pd.read_csv("Optim_res_unmet_0.05_inst.csv")
s4 = pd.read_csv("Optim_res_unmet_0.1_inst.csv")

# to check which columns include
s0.columns

# creates df with 166 sites and their LCUEs from each scenario (S0-S4)
lcue_s0_s4 = pd.DataFrame({"Site_name": s0.Site_name, "County": s0.County,\
            "Institution": s0.Institution, "S0_LCUE":s0.LCUE,\
            "S1_LCUE":s1.LCUE, "S2_LCUE":s2.LCUE, "S3_LCUE":s3.LCUE,\
            "S4_LCUE":s4.LCUE})

# save csv LCUE df
lcue_s0_s4.to_csv("lcue_s0_s4.csv", index=False)
                        #OJO: IF I RERUN THIS IT WILL OVERWRITE SAVED FILE WITH THIS NAME


# creates df with 166 sites and their Emissions_intensity from each scenario (S0-S4)
emi_s0_s4 = pd.DataFrame({"Site_name": s0.Site_name, "County": s0.County,\
            "Institution": s0.Institution, "S0_EI":s0.Emissions_intensity,\
            "S1_EI":s1.Emissions_intensity, "S2_EI":s2.Emissions_intensity,\
            "S3_EI":s3.Emissions_intensity, "S4_EI":s4.Emissions_intensity})

# save csv Emissions_intensity df
emi_s0_s4.to_csv("emi_s0_s4.csv", index=False)
                        #OJO: IF I RERUN THIS IT WILL OVERWRITE SAVED FILE WITH THIS NAME


# creates df with 166 sites and their Cumulative_system_cost from each scenario (S0-S4)
cumsys_cost_s0_s4 = pd.DataFrame({"Site_name": s0.Site_name,\
            "County": s0.County, "Institution": s0.Institution,\
            "S0_system_cost": s0.Cumulative_system_cost,\
            "S1_system_cost": s1.Cumulative_system_cost,\
            "S2_system_cost": s2.Cumulative_system_cost,\
            "S3_system_cost": s3.Cumulative_system_cost,\
            "S4_system_cost": s4.Cumulative_system_cost})

# save csv Cumulative_system_cost df
cumsys_cost_s0_s4.to_csv("cumsys_cost_s0_s4.csv", index=False)
                        #OJO: IF I RERUN THIS IT WILL OVERWRITE SAVED FILE WITH THIS NAME


# creates df with 166 sites and their Cumulative_system_GHG from each scenario (S0-S4)
cumsys_ghg_s0_s4 = pd.DataFrame({"Site_name": s0.Site_name,\
            "County": s0.County, "Institution": s0.Institution,\
            "S0_system_ghg": s0.Cumulative_system_GHG,\
            "S1_system_ghg": s1.Cumulative_system_GHG,\
            "S2_system_ghg": s2.Cumulative_system_GHG,\
            "S3_system_ghg": s3.Cumulative_system_GHG,\
            "S4_system_ghg": s4.Cumulative_system_GHG})

# save csv Cumulative_system_GHG df
cumsys_ghg_s0_s4.to_csv("cumsys_ghg_s0_s4.csv", index=False)
                        #OJO: IF I RERUN THIS IT WILL OVERWRITE SAVED FILE WITH THIS NAME

# ONLY REPEAT ABOVE IF RESULTS ARE DIFFERENT IN THE FUTURE (rerun) OR IF I WANT
# TO GET THE COMPARISON OF OTHER METRICS (not LCUE, EI, Cumu sys costs or GHG)
# ACROSS 5 SCENARIOS. O sea no deberia porque correr este codigo otra vez a menos
# que sea para rehacer plots abajo

# Frome HERE onwards is where the 's0-s4_costs_ghgs_plots' Jupyter notebook starts
# Trial - LCUE: to plot and analyse one metric for all scenarios all 166 sites

lcue_s0_s4 = pd.read_csv("lcue_s0_s4.csv")
lcue_s0_s4.head()
lcue_s0_s4.tail()
lcue_s0_s4.columns
lcue_s0_s4.describe().round(3)


# Plot LCUEs of all scenarios for all 166 sites
sns.set(rc={"figure.dpi":300})
sns.set_context("notebook")
#sns.set_style("ticks") # with axis ticks, no background lines
sns.set_style("whitegrid") # no axis ticks, with background lines

# with catplot top and right axes spines are not shown, plot is larger vertically
g = sns.catplot(
    data= lcue_s0_s4, kind= "box", palette= "Set2")  # change to violin
g.set(xlabel= "Scenarios", ylabel= "LCUE ($/kWh)")
#g.set(ylim=(0, 5)) # to get rid of outlier
g.set_xticklabels(["S0", "S1", "S2", "S3", "S4"])
sns.despine(top=False, right=False)

# save the figure
plt.savefig("LCUE_s0-s4.png", facecolor="white", transparent=False, dpi=300, bbox_inches="tight")
plt.show()


# trial of a plot but not using this one
# if I use boxplot instead of catplot it shows top and right axes spines, plot is larger horizontally
g = sns.boxplot(
    data=lcue_s0_s4, palette="Set2")
g.set(xlabel= "Scenarios", ylabel="LCUE ($/kWh)")
g.set_xticklabels(["S0", "S1", "S2", "S3", "S4"])
#sns.despine()  # get rid of top and right axes spines


# to separate df by Institution type (by Clinics)
lcue_s0_s4_clinics = lcue_s0_s4[lcue_s0_s4.Institution != 'School']
# returns LCUE df of only clinics (18)
lcue_s0_s4_clinics.describe().round(3)

# Plot clinics LCUE
g = sns.catplot(
    data=lcue_s0_s4_clinics, kind= "box", palette= "Set2")  # change to violin
g.set(xlabel= "Scenarios", ylabel= "LCUE ($/kWh)")
#g.set(ylim=(0, 3)) # to get rid of outlier
g.set_xticklabels(["S0", "S1", "S2", "S3", "S4"])
g.set(title="Clinics LCUE")
sns.despine(top=False, right=False)

# to separate df by Institution type (by Schools)
lcue_s0_s4_schools = lcue_s0_s4[lcue_s0_s4.Institution != 'Clinic']
# returns LCUE df of only schools (148)
lcue_s0_s4_schools.describe().round(3)


# Plot schools LCUE
g = sns.catplot(
    data=lcue_s0_s4_schools, kind= "box", palette= "Set2")  # change to violin
g.set(xlabel= "Scenarios", ylabel= "LCUE ($/kWh)")
#g.set(ylim=(0, 3)) # to get rid of outlier
g.set_xticklabels(["S0", "S1", "S2", "S3", "S4"])
g.set(title="Schools LCUE")
#sns.despine(top=False, right=False)


# maybe plot them again but setting y-axis to NOT show outliers and to have same
# axis for both institutions (maybe same as plot with altogether, is the same so no)

# locate a site (outlier) to potentially drop it from df in the future
# taken from 'Jua udata.py'
lcue_s0_s4.loc[lcue_s0_s4["Site_name"] == "Muchuro_Primary_School"]  # to get row where site is
lcue_s0_s4.index[lcue_s0_s4["Site_name"] == "Muchuro_Primary_School"] #

# drop site (potential outlier)
lcue_s0_s4_ok = lcue_s0_s4.drop([121])

# do describe again of df without outlier
lcue_s0_s4_ok.describe()


# also works but df was the same as above and this is longer so I kept previous version (without .values)
#prueba = pd.DataFrame({"Site_name":s0.Site_name.values, "S0_LCUE":s0.LCUE.values,\
#            "S1_LCUE":s1.LCUE.values, "S2_LCUE":s2.LCUE.values, "S3_LCUE":s3.LCUE.values,\
#            "S4_LCUE":s4.LCUE.values})

# to check if df were the same:
# test.equals(prueba)

# quick way to check if plotting works
# sns.catplot(data=lcue_s0_s4, kind="box")
