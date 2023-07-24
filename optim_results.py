# Code created 27Feb23
# To have main optimisation outputs in one same csv file per scenario criterion value
## see also 'simu_results_avg.py' for average results and dan.py for initial trial

# 1. General set up for code to work
import os
import json
import pandas as pd

path = "/Users/po416/Library/CloudStorage/OneDrive-ImperialCollegeLondon/PhDOct2018/Projects (12Mar20)/Project Jua/Optimisation_res"

cwd = os.getcwd()
cwd

os.chdir(path) # or put it the whole path
pwd # ensure is in the correct path. Sometimes if df doesn't work is bc it is on the wrong path
# then go to Step 2. (don't repeat Trial 1 & 2 below - only for testing purposes)

# Run it all in one go (or just once with all the variables I want)
# because if I reran it more than once, site_names will be duplicated and df won't be
# able to be created bc of different sizes of array


# Trial 1 - getting LCUE for all optimisation output results (returns 664 in total)
#site_name = []
#lcue = []
#unmet_energy_fraction = []  # to check which scenario it is

#for root, _, files in os.walk("."):
#    for filename in files:
#        if not filename.endswith(".json"):
#            continue
#        with open(os.path.join(root, filename), "r") as f:
#            data = json.load(f)
#        site_name.append(os.path.basename(root).split("_Optim")[0])
#        lcue.append(data["system_appraisals"]["iteration_0"]["criteria"]["lcue"])
#        unmet_energy_fraction.append(data["system_appraisals"]["iteration_0"]["criteria"]["unmet_energy_fraction"])

#optim_trial = pd.DataFrame({"Site_name": site_name, "LCUE": lcue, "Unmet_energy_fraction": unmet_energy_fraction})
# ok but it returns all 664 sites and I have to guess which scenario is depending on
# unmet_energy_fraction so do it separately
# namefile.to_csv("namefile.csv", index=False)

# Trial 2 - to get output results of other 3 scenarios (except "0.0") add line below
#for root, _, files in os.walk("."):
#    for filename in files:
#        if root.endswith("0.0"):  # <-- add this line
#            continue
#        if not filename.endswith(".json"):
#            continue
#        with open(os.path.join(root, filename), "r") as f:  # the rest is the same...

# Step 2. Get optimisation results for 0.0 scenario (extended version)
site_name = []
county = []

initial_pv = []
initial_storage = []
final_pv = []
final_storage = []

lcue = []
emissions_intensity = []
cumu_system_cost = []
cumu_system_ghg = []

blackouts = []
unmet_energy_fraction = []

for root, _, files in os.walk("."):
    for filename in files:
        if not root.endswith("0.0"):  # CHANGE DEPENDING ON SCENARIO! without "not" it returns results other 3 scenarios (except 0 unmet)
            continue
        if not filename.endswith(".json"):
            continue
        with open(os.path.join(root, filename), "r") as f:
            data = json.load(f)
        site_name.append(os.path.basename(root).split("_Optim")[0])
        county.append(os.path.dirname(root).split("_opt")[0]) # need to get rid of ./ doing it in excel atm
        initial_pv.append(data["system_appraisals"]["iteration_0"]["system_details"]["initial_pv_size"])
        initial_storage.append(data["system_appraisals"]["iteration_0"]["system_details"]["initial_storage_size"])
        final_pv.append(data["system_appraisals"]["iteration_0"]["system_details"]["final_pv_size"])
        final_storage.append(data["system_appraisals"]["iteration_0"]["system_details"]["final_storage_size"])
        lcue.append(data["system_appraisals"]["iteration_0"]["criteria"]["lcue"])
        emissions_intensity.append(data["system_appraisals"]["iteration_0"]["criteria"]["emissions_intensity"])
        cumu_system_cost.append(data["system_appraisals"]["iteration_0"]["cumulative_results"]["cumulative_system_cost"])
        cumu_system_ghg.append(data["system_appraisals"]["iteration_0"]["cumulative_results"]["cumulative_system_ghgs"])
        blackouts.append(data["system_appraisals"]["iteration_0"]["criteria"]["blackouts"])
        unmet_energy_fraction.append(data["system_appraisals"]["iteration_0"]["criteria"]["unmet_energy_fraction"])

optim_res_unmet_0 = pd.DataFrame({"Site_name": site_name, "County": county, \
                "Initial_PV_size": initial_pv, "Initial_storage_size": initial_storage, \
                "Final_PV_size": final_pv, "Final_storage_size": final_storage, \
                "LCUE": lcue, "Emissions_intensity": emissions_intensity, \
                "Cumulative_system_cost": cumu_system_cost, "Cumulative_system_GHG": cumu_system_ghg, \
                "Blackouts": blackouts, "Unmet_energy_fraction": unmet_energy_fraction})

# sanity check of unmet_energy_fraction value
optim_res_unmet_0.describe() # look at unmet_energy_fraction column, values must be all 0
# returned all 0 so OK!

# sort df by "Site_name" alphabetical order so all df (from different scenarios) have same order
optim_res_unmet_0_sorted = optim_res_unmet_0.sort_values("Site_name") # could be ("Site_name", inplace=False) but is the same

# delete ./ from county column
optim_res_unmet_0_sorted["County"] = optim_res_unmet_0_sorted["County"].str[2:]

# save csv sorted df
optim_res_unmet_0_sorted.to_csv("Optim_res_unmet_0.csv", index=False)
                            #OJO: IF I RERUN THIS IT WILL OVERWRITE SAVED FILE WITH THIS NAME

# TO GET OTHER OPTIMISATION SCENARIOS RESULTS (0.1)
# Repeat 1. and 2. but using "0.1" for unmet_energy scenario of 0.1:
if not root.endswith("0.1"):  # change in line 72 above

# Change variable name of df to save values (avoid floats)
# this is for scenario using 0.1 unmet_energy_fraction
optim_res_unmet_1 = pd.DataFrame({"Site_name": site_name, "County": county, \
                "Initial_PV_size": initial_pv, "Initial_storage_size": initial_storage, \
                "Final_PV_size": final_pv, "Final_storage_size": final_storage, \
                "LCUE": lcue, "Emissions_intensity": emissions_intensity, \
                "Cumulative_system_cost": cumu_system_cost, "Cumulative_system_GHG": cumu_system_ghg, \
                "Blackouts": blackouts, "Unmet_energy_fraction": unmet_energy_fraction})

# sanity check of unmet_energy_fraction value
optim_res_unmet_1.describe() # look at unmet_energy_fraction column, values must be all 0
# max value is 0.1 so OK!

# delete ./ from county column, could do it in any order (delete first, sort later or the other way round as above)
optim_res_unmet_1["County"] = optim_res_unmet_1["County"].str[2:]

# sort df by Site_name alphabetical order
optim_res_unmet_1_sorted = optim_res_unmet_1.sort_values("Site_name")

# save csv sorted data
optim_res_unmet_1_sorted.to_csv("Optim_res_unmet_0.1.csv", index=False)
                                #OJO: IF I RERUN THIS IT WILL OVERWRITE SAVED FILE WITH THIS NAME

# TO GET OTHER OPTIMISATION SCENARIOS RESULTS (0.05)
# Repeat 1. and 2. but using "0.05" for unmet_energy scenario of 0.05:
if not root.endswith("0.05"):  # change in line 72 above

# Change variable name of df to save values (avoid floats)
# this is for scenario using 0.1 unmet_energy_fraction
optim_res_unmet_05 = pd.DataFrame({"Site_name": site_name, "County": county, \
                "Initial_PV_size": initial_pv, "Initial_storage_size": initial_storage, \
                "Final_PV_size": final_pv, "Final_storage_size": final_storage, \
                "LCUE": lcue, "Emissions_intensity": emissions_intensity, \
                "Cumulative_system_cost": cumu_system_cost, "Cumulative_system_GHG": cumu_system_ghg, \
                "Blackouts": blackouts, "Unmet_energy_fraction": unmet_energy_fraction})

# sanity check of unmet_energy_fraction value
optim_res_unmet_05.describe() # look at unmet_energy_fraction column, values must be all 0
# max value is 0.05 so OK!

# delete ./ from county column, could do it in any order (delete first, sort later or the other way round as above)
optim_res_unmet_05["County"] = optim_res_unmet_05["County"].str[2:]

# sort df by Site_name alphabetical order
optim_res_unmet_05_sorted = optim_res_unmet_05.sort_values("Site_name")

# save csv sorted data
optim_res_unmet_05_sorted.to_csv("Optim_res_unmet_0.05.csv", index=False)
                            #OJO: IF I RERUN THIS IT WILL OVERWRITE SAVED FILE WITH THIS NAME

# TO GET OTHER OPTIMISATION SCENARIOS RESULTS (0.01)
# Repeat 1. and 2. but using "0.01" for unmet_energy scenario of 0.01:
if not root.endswith("0.01"):  # change in line 72 above

# Change variable name of df to save values (avoid floats)
# this is for scenario using 0.01 unmet_energy_fraction
optim_res_unmet_01 = pd.DataFrame({"Site_name": site_name, "County": county, \
                "Initial_PV_size": initial_pv, "Initial_storage_size": initial_storage, \
                "Final_PV_size": final_pv, "Final_storage_size": final_storage, \
                "LCUE": lcue, "Emissions_intensity": emissions_intensity, \
                "Cumulative_system_cost": cumu_system_cost, "Cumulative_system_GHG": cumu_system_ghg, \
                "Blackouts": blackouts, "Unmet_energy_fraction": unmet_energy_fraction})

# sanity check of unmet_energy_fraction value
optim_res_unmet_01.describe() # look at unmet_energy_fraction column, values must be all 0
# max value is 0.01 so OK!

# delete ./ from county column, could do it in any order (delete first, sort later or the other way round as above)
optim_res_unmet_01["County"] = optim_res_unmet_01["County"].str[2:]

# sort df by Site_name alphabetical order
optim_res_unmet_01_sorted = optim_res_unmet_01.sort_values("Site_name")

# save csv sorted data
optim_res_unmet_01_sorted.to_csv("Optim_res_unmet_0.01.csv", index=False)
                        #OJO: IF I RERUN THIS IT WILL OVERWRITE SAVED FILE WITH THIS NAME

# SUMMARY OF WHAT THIS CODE DOES
# This code walks through the ‘Optimisation_res’ folder, creates 12 lists to save results,
# and reads the json files of the folders ending with the optimisation criterion specified
# (0.0, 0.01, 0.05, 0.1). It then saves the key variables in a df per scenario, sorts the
# sites in alphabetical order (per ‘Site_name’ column), deletes the typo (./) on ‘County’
# column and exports the df to csv.
# If I ever need to rerun it, ENSURE that I change line 72 of code for each of the other
# three scenarios:
    # if not root.endswith(“0.0”):  # change to 0.01, 0.05, 0.1 depending on scenario
