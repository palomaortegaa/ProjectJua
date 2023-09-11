# Created 13 Apr 23
# To calculate utilisation rate of S0 results (simulations) - all is in kWh
# Walks through csv of S0 and calculates cumulative values of: dumped energy,
# total energy used and res supplied. Creates a df with Site name and county
# Adds Institution type as a column (based on another csv imported)
# Formats df so it has the same format as previous ones (sorted alphabetical, etc)
# Exports this csv created: "Simu_res_S0_inst.csv"
# Second part of this code is Jupyter version of plots & analysis of csv created
# Separates by institution type too
# check Jupyter notebook version for plots: 'ut_rate_S0'
# plots to add in Ch. 4 analysis


import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Move to path where csv are saved
path = "/Users/po416/Library/CloudStorage/OneDrive-ImperialCollegeLondon/PhDOct2018/Projects (12Mar20)/Project Jua/Resultados_simu"

cwd = os.getcwd()
cwd

os.chdir(path)
cwd  #pwd

# Walks through 'Resultados_simu' folder and opens csv files to calculate cumulative
# values of simulation results (dumped energy, total energy used, res supplied)
site_name = []
county = []

cumu_dumped = []

cumu_total_used = []
cumu_res_supplied = []


for root, _, files in os.walk("."):
    for filename in files:
        if not filename.endswith(".csv"):
            continue
        with open(os.path.join(root, filename), "r") as f:
            data = pd.read_csv(f)
        site_name.append(os.path.basename(root).split("_Simulation")[0])
        county.append(os.path.dirname(root).split("_simu")[0])
        cumu_dumped.append(data["Dumped energy (kWh)"].sum())
        cumu_total_used.append(data["Total energy used (kWh)"].sum())
        cumu_res_supplied.append(data["Renewables energy supplied (kWh)"].sum())

# Create df from values/variables extracted from CLOVER csv outputs
results_frame = pd.DataFrame({"Site_name": site_name, "County": county, \
    "Cumu_dumped_energy": cumu_dumped,\
    "Cumu_total_energy_used": cumu_total_used,\
    "Cumu_res_supplied": cumu_res_supplied})

# Calculates utilisation rate in %
results_frame["Ut_rate"]= (results_frame["Cumu_total_energy_used"]/results_frame["Cumu_res_supplied"])*100

# Formatting the df to be same as previous dfs generated
# delete ./ from county column, could do it in any order (delete first, sort later or the other way round as above)
results_frame["County"] = results_frame["County"].str[2:]

# sort df by "Site_name" alphabetical order so all df (from different scenarios) have same order
results_frame_sorted = results_frame.sort_values("Site_name")

# Add column to df with institution name, but first change path
pwd
path2= "/Users/po416/Library/CloudStorage/OneDrive-ImperialCollegeLondon/PhDOct2018/Projects (12Mar20)/Project Jua/Modelling PJua analysis/Results_outputs"
os.chdir(path2)
pwd

# import csv to copy Institutions column
s0_inst = pd.read_csv("Simu_res_S0_inst.csv")

# Add column to df of avg dumped energy per site SORTED BY NAME
results_frame_sorted["Institution"] = s0_inst["Institution"].values

# save csv sorted df
results_frame_sorted.to_csv("S0_utilisation_rate.csv", index=False)

# Plot it as it is
import seaborn as sns

sns.histplot(data=results_frame_sorted, x="Ut_rate")
plt.xticks(np.arange(0, 110, 10))
plt.show()

# Set style in Seaborn to plot
sns.set(rc={"figure.dpi":300})
sns.set_context("notebook")  # change to paper maybe? I prefer notebook style i think...
sns.set_style("ticks") # with axis ticks, no background lines
# sns.set_style("whitegrid")

# Plot all sites (delete binwidth to get sns default)
ax = sns.histplot(data=results_frame_sorted, x="Ut_rate", color="darkorange", binwidth=5) # kde=True
ax.set_xticks(np.arange(0, 100, 10))  # looks better than (0, 110, 10)
ax.set(xlabel= "Utilisation rate (%)", ylabel= "Number of institutions")
# ax.set(title="All sites")
plt.show()



# Reimport csv to plot utilisation rate (JUPYTER VERSION STARTS HERE)
os.chdir("/Users/po416/Library/CloudStorage/OneDrive-ImperialCollegeLondon/PhDOct2018/Projects (12Mar20)/Project Jua/Modelling PJua analysis/Results_outputs/Plots modelling PJua")
pwd

S0_utilisation_rate = pd.read_csv("S0_utilisation_rate.csv")
S0_utilisation_rate.describe().round(2)

# Plot all sites (delete binwidth to get sns default)
ax = sns.histplot(data=S0_utilisation_rate, x="Ut_rate", color="darkorange", binwidth=5) # kde=True
ax.set_xticks(np.arange(0, 100, 10))  # looks better
ax.set(xlabel= "Utilisation rate (%)", ylabel= "Number of institutions")
# ax.set(title="All sites")
plt.show()

# Separate df by Institution type (Clinics) (when I reimport it to plot)
s0_utrate_clinics = S0_utilisation_rate[S0_utilisation_rate.Institution != 'School']
# returns df of only clinics (18)
s0_utrate_clinics.describe().round(2)

# Plot Clinics as it is (delete binwidth to get sns default - try with "forestgreen" too)
sns.histplot(data=s0_utrate_clinics, x="Ut_rate", color="darkgreen", binwidth=3) # or binwidth= 2, kde=True

# Plot Clinics (delete binwidth to get sns default - try with "forestgreen" too)
ax=sns.histplot(data=s0_utrate_clinics, x="Ut_rate", color="darkgreen") # kde=True
ax.set_xticks(np.arange(0, 100, 10))  # looks better than extending axis to 100
ax.set(xlabel= "Utilisation rate (%)", ylabel= "Number of institutions")
ax.set(title="Clinics")
plt.show()


# Separate df by Institution type (Schools) (when I reimport it to plot)
s0_utrate_schools = S0_utilisation_rate[S0_utilisation_rate.Institution != 'Clinic']
# returns df of only schools (148)
s0_utrate_schools.describe().round(2)

# Plot Schools as it is (delete binwidth to get sns default)
sns.histplot(data=s0_utrate_schools, x="Ut_rate", color="maroon", binwidth=5) # or binwidth= 3, kde=True

# Plot Schools (delete binwidth to get sns default)
ax=sns.histplot(data=s0_utrate_schools, x="Ut_rate", color="darkred") # kde=True
ax.set_xticks(np.arange(0, 100, 10))  # looks better
ax.set(xlabel= "Utilisation rate (%)", ylabel= "Number of institutions")
ax.set(title="Schools")
plt.show()


# code deleted
# COLUMN_NAME: str = "Dumped energy (kWh)"
# average_data = {}

# ut_rate = []
# ut_rate.append(cum_total_used/cumu_res_supplied)

# plt.xticks([0, 100, 25])
