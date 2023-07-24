# Created 30Mar23
# To calculate average load profile of Clinics based on one-year of data
# I then repeated it for schools
# All outputs are in Wh (raw data is in kWh but I converted it to Wh for hrly plots)
# check outputs with excel: 'avg_ut analysis PJua'
# previous version of this code: 'trial_heatmap.py'
# see also Jupyter files: 'pjua_hrly_plots_all, 'clinics_load_profile_utavg';
# 'prischools_load_profile_utavg'; 'secschools_load_profile_utavg'


import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np # maybe don't need this

cwd = os.getcwd()
cwd

os.chdir("/Users/po416/Library/CloudStorage/OneDrive-ImperialCollegeLondon/PhDOct2018/Projects (12Mar20)/Project Jua/Sites udata/Filled_files")
os.getcwd()


# Plot all means of Clinics (except Chilodi)
average_data = {}

filenames = {entry for entry in os.listdir(".") if entry.endswith(".csv") \
if ("Clinic" in entry) or ("clinic" in entry) or ("dispensary" in entry) \
or ("Dispensary" in entry) or ("Health" in entry) or ("health" in entry)}
for filename in filenames:
    data = pd.read_csv(filename, usecols = ["Timestamp","Consumption"])
    data["Timestamp"] = pd.to_datetime(data["Timestamp"],format="%d/%m/%Y %H:%M")
    data["Consumption"] *= 1000 # to convert to Wh
    # data['Consumption'].sum() # check totals if needed
    # Calculate average hourly utilisation
    hrly = data.groupby([data["Timestamp"].dt.hour]).Consumption.mean()
    average_data[filename.split("_gaps_filled")[0].replace("_", " ")] = hrly

# Creates df of Hour as index and sites as column, after calculating avg utilisation
results_frame = pd.DataFrame(average_data)

# Export df to check mean and std
results_frame.to_csv("clinics_avg_30Mar.csv")

# Setting to plot
sns.set(rc={"figure.dpi":300})
# sns.set_palette("colorblind", n_colors=len(filenames))
sns.set_context("notebook")
sns.set_style("whitegrid")

# Plot all sites together
plt.plot(results_frame)

# Plot it with format
plt.plot(results_frame, label=results_frame.columns)  # to do it with matplotlib
plt.xlabel("Hour of day")
plt.ylabel("Consumption (Wh)")
plt.xticks([0,3,7,11,15,19,23])
plt.xlim(0,23)
#plt.title("Clinics")
plt.legend(loc="upper center", bbox_to_anchor=(0.5, -0.15), ncol=2)
plt.show()

# improve: set different palette so colours don't repeat

# Calculate mean of sites
all_sites = results_frame.mean(axis=1)
# Convert to df
all_sites = pd.DataFrame(all_sites)
# Rename column name of df
all_sites.rename(columns = {0:"Mean"}, inplace = True)

# Calculate std of sites
all_sites["Std_dev"] = results_frame.std(axis=1)

# all_sites.round(2)  # to show in Jupyter &  to know peak utilisation

# Plot Mean consumption all sites
#sns.lineplot(data=hrly)
plt.plot(all_sites["Mean"])  # to do it with matplotlib
plt.xlabel("Hour of day")
plt.ylabel("Consumption (Wh)")
plt.xticks([0,3,7,11,15,19,23])
plt.xlim(0,23)
plt.title("Clinics")
plt.show()

# Reset index to be able to plot it
all_sites = all_sites.reset_index()

# Plot average and std dev hourly utilisation, with shaded area (after resetting index)
ax = plt.gca()
all_sites.plot(kind="line",x="Timestamp",y="Mean", color="tab:orange", ax=ax)
plt.fill_between(all_sites["Timestamp"], all_sites["Mean"] - all_sites["Std_dev"], all_sites["Mean"] + all_sites["Std_dev"], color="orange",
                 alpha=0.2) # alpha is to make shaded area lighter, save fig in PNG, PDF or SVG
ax.get_legend().remove()
plt.xlabel("Hour of day")
plt.ylabel("Consumption (Wh)")
plt.xticks([0,3,7,11,15,19,23])
plt.xlim(0,23)
plt.title("Clinics")
plt.show()

# For another format style option
# sns.set(rc={"figure.dpi":300})
# sns.set_style("ticks")

# To calculate average daily utilisation (all is in Wh)
avg_daily = results_frame.sum().to_frame()

# Rename column name of df
avg_daily.rename(columns = {0:"Avg_daily"}, inplace = True)

# avg_daily  # to show in Jupyter
# Get stats of average daily values (all sites)
avg_daily.describe().round(2)
# this are values I used in draft to describe utilisation on an average day for all clinics

# To convert to kWh
avg_daily_kwh = avg_daily.div(1000)
avg_daily_kwh.round(2)  # to show in Jupyter


# To do it for secondary schools do the same as above but just change to
# colours for Secondary schools plot: "darkcyan" and "lightseagreen"
# Plot all means of Secondary Schools
average_data = {}
filenames = {entry for entry in os.listdir(".") if entry.endswith(".csv") \
if ("Secondary" in entry) or ("secondary" in entry)}
# and then the same .... etc
for filename in filenames:
    data = pd.read_csv(filename, usecols = ["Timestamp","Consumption"])
    data["Timestamp"] = pd.to_datetime(data["Timestamp"],format="%d/%m/%Y %H:%M")
    data["Consumption"] *= 1000 # to convert to Wh
    # data['Consumption'].sum() # check totals if needed
    # Calculate average hourly utilisation
    hrly = data.groupby([data["Timestamp"].dt.hour]).Consumption.mean()
    average_data[filename.split("_gaps_filled")[0].replace("_", " ")] = hrly

# Creates df of Hour as index and sites as column, after calculating avg utilisation
results_frame = pd.DataFrame(average_data)
# results_frame.to_csv("secondary_avg_31Mar.csv")


# To do it for Primary schools do the same as above but just change to
# colours for plots: "tab:blue" and "lightskyblue"
# Plot all means of Primary Schools
average_data = {}
filenames = {entry for entry in os.listdir(".") if entry.endswith(".csv") \
if ("Primary" in entry) or ("primary" in entry)}
# and then the same .... etc
for filename in filenames:
    data = pd.read_csv(filename, usecols = ["Timestamp","Consumption"])
    data["Timestamp"] = pd.to_datetime(data["Timestamp"],format="%d/%m/%Y %H:%M")
    data["Consumption"] *= 1000 # to convert to Wh
    # data['Consumption'].sum() # check totals if needed
    # Calculate average hourly utilisation
    hrly = data.groupby([data["Timestamp"].dt.hour]).Consumption.mean()
    average_data[filename.split("_gaps_filled")[0].replace("_", " ")] = hrly

# Creates df of Hour as index and sites as column, after calculating avg utilisation
results_frame = pd.DataFrame(average_data)

# results_frame.to_csv("primary_avg_31Mar.csv")  # this is what i then analysed in excel


# TESTS FOR PEACE OF MIND (to check code worked)
# to test the hourly utilisation of a specific site
boyani_test= pd.read_csv('Boyani_Dispensary_gaps_filled.csv', usecols = ["Timestamp","Consumption"])
                    # to check other sites just change csv name
boyani_test["Timestamp"] = pd.to_datetime(boyani_test["Timestamp"],format="%d/%m/%Y %H:%M")
boyani_test["Consumption"] *= 1000
boyani_test_hrly = boyani_test.groupby([boyani_test["Timestamp"].dt.hour]).Consumption.mean()
# values should be the same as those calculated for that site in 'results_frame' df

# Another way of making lineplot of mean consumption
# simple plot (before resetting index)
ax = plt.gca()
all_sites.plot(kind="line",y="Mean", use_index=True, color="coral", ax=ax)
plt.show()

# Another way of calculating the average daily utilisation but df is only one row
# and each site is a column so not ideal
df1 = results_frame.sum().to_frame().T


# std = data.groupby([data["Timestamp"].dt.hour]).Consumption.std()
