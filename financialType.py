import pandas as pd
import matplotlib.pyplot as plt

def convertToSecond(hhmmss):
    h,m,s = [int(i) for i in hhmmss.split(':')]
    return (h*60+m)*60+s

dataset = pd.read_excel('data.xlsx')
# dataset = dataset.head(30)

# Interested fields: Financial Class, Entry Time, Post-Consultation Time
financialClass = dataset["Financial Class"]
entryTime = dataset["Entry Time"].astype(str)
completedTime = dataset["Completion Time"].astype(str)

# Calculate distance between entry time and post consult time
entryTime = entryTime.apply(convertToSecond)
completedTime = completedTime.apply(convertToSecond)
dataset["Waiting Time"] = completedTime - entryTime

averageWaitingTime = dataset.groupby("Financial Class")["Waiting Time"].mean()

# Create Bar Chart
plt.bar(averageWaitingTime.index, averageWaitingTime)
plt.xlabel("Financial Class")
plt.ylabel("Average Waiting Time (s)")
plt.show()

# Create Box Plot
dataset.boxplot(column="Waiting Time", by="Financial Class")
plt.xlabel("Financial Class")
plt.ylabel("Waiting Time (s)")
plt.show()

# Create new excel for waiting time and financial class
newDataset = pd.DataFrame()
newDataset["Financial Class"] = financialClass
newDataset["Waiting Time"] = dataset["Waiting Time"]
newDataset.to_excel("financialType.xlsx", index=False)