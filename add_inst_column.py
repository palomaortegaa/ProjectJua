# Created on 3Mar23
# Imports csv with PJua scenarios modelling results and adds institution type
# as a column (school/clinic) to each site in df, exports csv and saves it

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
#pwd
cwd

# Imports/reads csv of each scenario
s0 = pd.read_csv("Simu_res_S0.csv")
s1 = pd.read_csv("Optim_res_unmet_0.csv")
s2 = pd.read_csv("Optim_res_unmet_0.01.csv")
s3 = pd.read_csv("Optim_res_unmet_0.05.csv")
s4 = pd.read_csv("Optim_res_unmet_0.1.csv")

# in case I want to check unmet_energy_fraction in each scenario is ok
s0["Unmet_energy_fraction"].describe()  # this is from the simulations Jua systems
s2["Unmet_energy_fraction"].describe()  # max should be 0.01
s3["Unmet_energy_fraction"].describe()  # max should be 0.05, etc.

# Add column with institution type to base scenario (S0, with impala/rhino system sizes)
s0['Institution'] = np.where(s0['Initial_PV_size']== 1.06, "School", "Clinic")

# to check it works
len(s0[s0["Institution"]=="Clinic"])  # should return 18 (clinics)
len(s0[s0["Institution"]=="School"])  # should return 148 (schools)

# extract Institution column from s0 (base scenario)
extracted_col = s0["Institution"]
print(extracted_col)

s1 = s1.join(extracted_col)  # add Institution column to s1
s2 = s2.join(extracted_col)  # add Institution column to s2, etc...
s3 = s3.join(extracted_col)
s4 = s4.join(extracted_col)


# Save csv for each scenario with Institution column added
s0.to_csv("Simu_res_S0_inst.csv", index=False)
s1.to_csv("Optim_res_unmet_0_inst.csv", index=False)
s2.to_csv("Optim_res_unmet_0.01_inst.csv", index=False)
s3.to_csv("Optim_res_unmet_0.05_inst.csv", index=False)
s4.to_csv("Optim_res_unmet_0.1_inst.csv", index=False)

# Note:
# both df below are the same except that the ones ending with "_inst.csv" have
# now that extra column with Institution type (school/clinic)
# "Simu_res_S0_inst.csv" and "Simu_res_S0.csv" -> are almost the same
# "Optim_res_unmet_0_inst.csv" and "Optim_res_unmet_0.csv" -> are almost the same  
