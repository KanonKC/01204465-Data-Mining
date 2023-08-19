import pandas as pd
import matplotlib.pyplot as plt

def convertToSecond(hhmmss):
    h,m,s = [int(i) for i in hhmmss.split(':')]
    return (h*60+m)*60+s

def periodOfDay(hhmmss):
    h,m,s = [int(i) for i in hhmmss.split(':')]
    return h

dataset = pd.read_excel('data.xlsx')

# Interested fields: Entry Time
entryTime = dataset["Entry Time"].astype(str)
completedTime = dataset["Completion Time"].astype(str)

# Calculate distance between entry time and post consult time

dataset["Period of Day"] = entryTime.apply(periodOfDay)

entryTime = entryTime.apply(convertToSecond)
completedTime = completedTime.apply(convertToSecond)
dataset["Waiting Time"] = completedTime - entryTime

# Average waiting time group by hour of the day
averageWaitingTime = dataset.groupby("Period of Day")["Waiting Time"].mean()
print(averageWaitingTime)

# Create Bar Chart
plt.bar(averageWaitingTime.index, averageWaitingTime)
plt.xlabel("Financial Class")
plt.ylabel("Average Waiting Time (s)")
plt.xticks(averageWaitingTime.index)
plt.show()

# Create Box Plot
# dataset.boxplot(column="Waiting Time", by="Period of Day")
# plt.xlabel("Financial Class")
# plt.ylabel("Waiting Time (s)")

# plt.show()

# # Create new excel for waiting time and financial class
# newDataset = pd.DataFrame()
# newDataset["Waiting Time"] = dataset["Waiting Time"]
# newDataset.to_excel("financialType.xlsx", index=False)