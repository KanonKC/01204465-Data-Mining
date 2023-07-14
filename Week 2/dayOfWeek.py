import pandas as pd
import matplotlib.pyplot as plt

def convertToSecond(hhmmss):
    h,m,s = [int(i) for i in hhmmss.split(':')]
    return (h*60+m)*60+s

dataset = pd.read_excel('data.xlsx')
# dataset = dataset.head(30)

# Interested fields: Day of Week, Entry Time, Post-Consultation Time
dataset["Day of Week"] = dataset["Date"].dt.day_name()
entryTime = dataset["Entry Time"].astype(str)
completedTime = dataset["Completion Time"].astype(str)
dataset
# Calculate distance between entry time and post consult time
entryTime = entryTime.apply(convertToSecond)
completedTime = completedTime.apply(convertToSecond)
dataset["Waiting Time"] = completedTime - entryTime

averageWaitingTime = dataset.groupby("Day of Week")["Waiting Time"].mean()
averageWaitingTime = averageWaitingTime.reindex(["Sunday","Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"])

# Create Bar Chart
plt.bar(averageWaitingTime.index, averageWaitingTime)
plt.xlabel("Day of Week")
plt.ylabel("Average Waiting Time (s)")
plt.show()

# Create Box Plot
# dataset.boxplot(column="Waiting Time", by="Day of Week")
# plt.xlabel("Day of Week")
# plt.ylabel("Waiting Time (s)")
# plt.show()

# Create new excel for waiting time and Day of Week
# newDataset = pd.DataFrame()
# newDataset["Day of Week"] = financialClass
# newDataset["Waiting Time"] = dataset["Waiting Time"]
# newDataset.to_excel("financialType.xlsx", index=False)