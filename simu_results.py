# Code created 2Mar23
# To have main simulation outputs in one same csv file (for S0 scenario, same format as S1-S4)
# this is for scenario 0 so simulation of impala/rhino system with fixed inverter size (13_Feb_2.csv)
## see also 'simu_results_cumu.py', 'simu_results_avg.py' for cumu and avg results
## dan.py for initial trial

# 1. General set up for code to work
import os
import json
import pandas as pd

path = "/Users/po416/Library/CloudStorage/OneDrive-ImperialCollegeLondon/PhDOct2018/Projects (12Mar20)/Project Jua/Resultados_simu"

cwd = os.getcwd()
cwd

os.chdir(path) # or put the whole path
pwd # ensure is in the correct path. Sometimes if df doesn't work is bc it is on the wrong path

# Run it all in one go (or just once with all the variables I want)
# because if I reran it more than once, site_names will be duplicated and df won't be
# able to be created bc of different sizes of array

site_name = []
county = []

initial_pv = []
initial_storage = []
final_pv = []
final_storage = []

lcue = []
emissions_intensity = []
cumu_system_cost = []
cumu_system_ghgs = []

blackouts = []
unmet_energy_fraction = []


for root, _, files in os.walk("."):
    for filename in files:
        if not filename.endswith(".json"):
            continue
        with open(os.path.join(root, filename), "r") as f:
            data = json.load(f)
        site_name.append(os.path.basename(root).split("_Simulation")[0])
        county.append(os.path.dirname(root).split("_simu")[0])
        initial_pv.append(data["simulation_1"]["initial_pv_size"])
        initial_storage.append(data["simulation_1"]["initial_storage_size"])
        final_pv.append(data["simulation_1"]["final_pv_size"])
        final_storage.append(data["simulation_1"]["final_storage_size"])
        lcue.append(data["simulation_1"]["system_appraisal"]["criteria"]["lcue"])
        emissions_intensity.append(data["simulation_1"]["system_appraisal"]["criteria"]["emissions_intensity"])
        cumu_system_cost.append(data["simulation_1"]["system_appraisal"]["cumulative_results"]["cumulative_system_cost"])
        cumu_system_ghgs.append(data["simulation_1"]["system_appraisal"]["cumulative_results"]["cumulative_system_ghgs"])
        blackouts.append(data["simulation_1"]["system_appraisal"]["technical_appraisal"]["blackouts"])
        unmet_energy_fraction.append(data["simulation_1"]["system_appraisal"]["technical_appraisal"]["unmet_energy_fraction"])

simu_res_S0 = pd.DataFrame({"Site_name": site_name, "County": county, \
                "Initial_PV_size": initial_pv, "Initial_storage_size": initial_storage, \
                "Final_PV_size": final_pv, "Final_storage_size": final_storage, \
                "LCUE": lcue, "Emissions_intensity": emissions_intensity, \
                "Cumulative_system_cost": cumu_system_cost, "Cumulative_system_GHG": cumu_system_ghgs, \
                "Blackouts": blackouts, "Unmet_energy_fraction": unmet_energy_fraction})

# to see stats of all simulation results
simu_res_S0.describe()

# sort df by "Site_name" alphabetical order so all df (from different scenarios) have same order
simu_res_S0_sorted = simu_res_S0.sort_values("Site_name") # could be ("Site_name", inplace=False) but is the same

# delete ./ from county column
simu_res_S0_sorted["County"] = simu_res_S0_sorted["County"].str[2:]

# save csv sorted df
simu_res_S0_sorted.to_csv("Simu_res_S0.csv", index=False)
                        #OJO: IF I RERUN THIS IT WILL OVERWRITE SAVED FILE WITH THIS NAME

# to get stats values using describe, returns min, mean, std, max, etc of columns for all 166 sites aggregated
simu_res_S0_sorted.describe()
simu_res_S0_sorted["LCUE"].describe()
simu_res_S0_sorted["Emissions_intensity"].describe()
simu_res_S0_sorted["Cumulative_system_cost"].describe()
simu_res_S0_sorted["Cumulative_system_GHG"].describe()
simu_res_S0_sorted["Unmet_energy_fraction"].describe()

# trials of plots - not very good plots but just testing 
simu_res_S0_sorted.plot(kind="box")

import seaborn as sns
sns.catplot(data=simu_res_S0_sorted, kind="box")
