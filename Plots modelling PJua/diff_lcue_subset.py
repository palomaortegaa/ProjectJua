# Created 22 Apr 23
# To calculate % difference in LCUEs across scenarios (S1-S4 vs S0) BUT for subset only
# Includes 124 sites (including 3 sites with positive % difference)
# Last part of code is more for plots trials (ask Dani which one is best)
# check Jupyter notebook version for plots: 'diff_lcue_subset'
# plots to add in Ch. 4 analysis (on final draft but check with Dani first - this is AG plot)

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Move to path where csv is saved
path = "/Users/po416/Library/CloudStorage/OneDrive-ImperialCollegeLondon/PhDOct2018/Projects (12Mar20)/Project Jua/Modelling PJua analysis/Results_outputs"

cwd = os.getcwd()
cwd

os.chdir(path)
cwd  #pwd

# First remove sites with unmet energy fraction !=0
# List of sites with Unmet_energy_fraction of 0 in S0 (n=124) taken from 'subset_unmet0.py'
subset_list= ['AIC_Nadoto_Primary_School', 'AIC_Nayanaekaton_Primary_School',\
'A_IC_Gangani_Primary_School', 'Abagarse_Primary_School', 'Akadeli_Primary_School',\
'Akili_Primary_School', 'Bahero_Primary_School', 'Balaga_Primary_School',\
'Bomani_Primary_School', 'Boyani_Dispensary', 'Boyani_West_Primary_School',\
'Busa_Dispensary', 'Chidzaya_Primary_School', 'Chingombero_Dispensary',\
'Daaba_Primary_School', 'Dadachabasa_Primary_School', 'Dera_Tumaini_Primary_School',\
'Dighai_Primary_School', 'Dzendereni_Primary_School', 'Dzombo_Primary_School',\
'Ekoropus_Primary_School', 'Elsa_Primary_School', 'Fudumulo_Primary_School',\
'Galmadido_Primary_School', 'Gamachu_Primary_School', 'Garbatula_Primary_Boarding',\
'Gozani_Primary_School', 'Hawe_Wanje_Primary_School', 'Isiolo_Samburu_Complex_Dispensary',\
'Isiolo_Samburu_Complex_Primary_School', 'Jezazhomu_Primary_School', 'Jitegemee_Primary_School',\
'Kaalem_Primary_School', 'Kadunguni_Primary_School', 'Kalokoda_Primary_School',\
'Kaluweni_Primary_School', 'Karyaka_Primary_School', 'Kasuroi_Primary_School',\
'Kavunyalo_Dispensary', 'Kawala_Girls_Secondary_School', 'Kawalash_Primary_School',\
'Kibora_Primary_School', 'Kidomaya_Primary_School', 'Kikonde_Primary_School',\
'Kinna_Primary_School', 'Kithengwani_Primary_School', 'Kituoni_Primary_School',\
'Kizimbani_Primary_School', 'Kombola_primary_school', 'Konjora_Primary_School',\
'Kubimatamuka_Primary_School', 'KulaMawe_Primary_School', 'Kulalu_Primary_School',\
'Lakole_Primary_School', 'Lobei_Primary_School', 'Loruth_Primary_School',\
'Lunguma_Primary_School', 'Mabayani_Primary_School', 'Mabesheni_Dispensary',\
'Madibwani_Primary_School', 'Maendeleo_Primary_School', 'Mafisini_Primary_School',\
'Magale_Primary_School', 'Magodzoni_Primary_School', 'Maiyini_Primary_School',\
'Makamini_Dispensary', 'Malkadaka_Primary_School', 'Mama_Saleti_Primary_School',\
'Maphanga_Primary_School', 'Marafiki_Primary_School', 'Mataarba_Primary_School',\
'Matolani_Primary_School', 'Mawe_Mabomu_Primary_School', 'Mazola_Dispensary',\
'Mbararani_Primary_School', 'Mbilini_Primary_School', 'Mbulia_Dispensary',\
'Melikubwa_Primary_School', 'Merti_Muslim_Primary_School', 'Mikameni_Primary_School',\
'Mitangani_Primary_School', 'Mitangoni_Primary_School', 'Mitunguni_Primary_School',\
'Mlilo_Primary_School', 'Mlola_Primary_School', 'Mogore_Primary_School',\
'Mrima_Wa_Kuku_Primary_School', 'Mtsangatamu_Primary_School', 'Mtumwa_Dispensary',\
'Muchuro_Primary_School', 'Mugumoni_Primary_School', 'Munandanur_Primary_School',\
'Mwaluvuno_Primary_School', 'Mwamambi_Primary_School', 'Mwangani_Primary_School',\
'Mwangaza_Primary_School', 'Mwanza_Primary_School', 'Mwanzwani_Primary_School',\
'Mwele_Primary_School', 'Mwembe_Kati_Dispensary', 'Nabeiye_Primary_School',\
'Nagaa_Primary_School', 'Nakaalei_Primary_School', 'Nakitoekakumon_Primary_School',\
'Namakat_Primary_School', 'Naroo_Primary_School', 'Ndugu_Zangu_Integrated_Primary_School',\
'Ngoloko_Primary_School', 'Nyango_Primary_School', 'Paola_Katsuhanzala_Primary_School',\
'Sagalato_Primary_School', 'Saghaighu_dispensary', 'Sembe_Primary_School',\
'Shakahola_Dispensary', 'Shauri_Moyo_Primary_School', 'Silaloni_Primary_School',\
'Simanya_Primary_School', 'Tiwi_Boys_Secondary_school', 'Todonyang_Primary_School',\
'Uhuru_Primary_School', 'Vithunguni_Primary_School', 'Watala_Primary_School',\
'Ziwani_Primary_School', 'Ziyaradundo_Primary_School']


print(subset_list)    # should be 124 in this case (124 sites with unmet of 0 in S0)

# Imports/reads csv of LCUE of S0-S4 (created with another code)
data = pd.read_csv("lcue_s0_s4.csv")

# Creates new df including only subset of sites on subset_list:
data_subset = data[data["Site_name"].isin(subset_list)]
# data_subset # to show in Jupyter
# data_subset.describe().round(2)

# Define function to calculate percentage change
def percentage_change(col1, col2):
    return ((col2 - col1) / col1) * 100


# Create new pandas DataFrame from copy of original df
perchange = data_subset[["Site_name", "County", "Institution"]].copy()

# Add columns with calculated values of percentage change vs S0
perchange["S1_S0"] = percentage_change(data_subset["S0_LCUE"], data_subset["S1_LCUE"]).round(2)
perchange["S2_S0"] = percentage_change(data_subset["S0_LCUE"], data_subset["S2_LCUE"]).round(2)
perchange["S3_S0"] = percentage_change(data_subset["S0_LCUE"], data_subset["S3_LCUE"]).round(2)
perchange["S4_S0"] = percentage_change(data_subset["S0_LCUE"], data_subset["S4_LCUE"]).round(2)

# To see how the data looks, here it shows the % change in LCUEs of S1-S4 vs S0
perchange.describe().round(2)

# To check sites with positive cost difference
perchange.loc[(perchange["S1_S0"] >= 0)] # can check for S2_S0, etc. but they have no positive values
# another way of doing it:
# perchange[perchange["S1_S0"] > 0]

# Import library to plot and set style in Seaborn
import seaborn as sns

sns.set(rc={"figure.dpi":300})
sns.set_context("notebook")  # change to paper maybe? I prefer notebook style i think...
sns.set_style("ticks") # with axis ticks, no background lines
# sns.set_style("whitegrid")


# Define my Set2 custom palette without S0 color
colors = ["#fc8d62", "#8da0cb", "#e78ac3", "#a6d854"]

# Final version of plot (for now)
fig,ax = plt.subplots(1,1)
sns.kdeplot(data=perchange.S1_S0, color=colors[0],label="S1", ax=ax) # fill=True
sns.kdeplot(data=perchange.S2_S0, color=colors[1],label="S2", ax=ax) # fill=True
sns.kdeplot(data=perchange.S3_S0, color=colors[2],label="S3", ax=ax) # fill=True
sns.kdeplot(data=perchange.S4_S0, color=colors[3],label="S4", ax=ax) # fill=True
plt.xlabel("Percentage difference (%)")
plt.legend(frameon=False)


# Another way but it is wrong (i think) as it takes density calculating 664 in total instead of 166 in each
sns.kdeplot(data=perchange, palette=colors) # bw_adjust=1

# And another
sns.kdeplot(data=perchange, x="S1_S0", bw_adjust=1) # or bw_adjust=1.5


# Prueba 1 - rari
fig,ax = plt.subplots(1,1)
sns.kdeplot(data=perchange.S1_S0, bw_adjust=1.5, color=colors[0],label="S1", ax=ax) # fill=True
sns.kdeplot(data=perchange.S2_S0, bw_adjust=1.5, color=colors[1],label="S2", ax=ax) # fill=True
sns.kdeplot(data=perchange.S3_S0, bw_adjust=1.5, color=colors[2],label="S3", ax=ax) # fill=True
sns.kdeplot(data=perchange.S4_S0, bw_adjust=1.5, color=colors[3],label="S4", ax=ax) # fill=True
plt.xlabel("Percentage difference (%)")
plt.legend(frameon=False)


# Prueba 2 - another way of doing final plot for now
fig,ax = plt.subplots(1,1)
sns.kdeplot(data=perchange, x="S1_S0", color=colors[0],label="S1", ax=ax) # fill=True
sns.kdeplot(data=perchange, x="S2_S0", color=colors[1],label="S2", ax=ax) # fill=True
sns.kdeplot(data=perchange, x="S3_S0", color=colors[2],label="S3", ax=ax) # fill=True
sns.kdeplot(data=perchange, x="S4_S0", color=colors[3],label="S4", ax=ax) # fill=True
plt.xlabel("Percentage difference (%)")
plt.legend(frameon=False)
