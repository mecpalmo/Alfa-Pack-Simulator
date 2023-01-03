import numpy as np
from collections import Counter
from collections import OrderedDict
import matplotlib.pyplot as plt

def plotOccurances(eventList):
    eventsCounted = Counter(eventList) #counting occurances with collections
    eventDict = dict(eventsCounted) #converting result to a regular dictionary
    eventDict = OrderedDict(sorted(eventDict.items())) #sorting those dictionaries
    eventKeys = list(eventDict.keys()) #spliting dictionaries into single dimension lists
    eventValues = list(eventDict.values())
    plt.plot(eventKeys, eventValues)
    plt.grid()
    plt.xlabel("When acquired")
    plt.ylabel("Packs Acquired")
    plt.show()

def getMedian(eventList):
    eventList = sorted(eventList)
    return eventList[int(len(eventList)/2)]

#core values
WINRATE = 0.5
numOfMatches = 100000

#starting values
prob = 0.03
matches = 0

#list for data collection
wonPackProbs = []
wonPackMatches = []

#simulation
for i in range(0,numOfMatches):
    winResult = np.random.choice([True, False], size=1, p=[WINRATE, 1-WINRATE])
    matches += 1
    if(winResult[0]):
        packResult = np.random.choice([True, False], size=1, p=[prob, 1-prob])
        if(packResult[0]):
            wonPackProbs.append(prob)
            wonPackMatches.append(matches)
            matches = 0
            prob = 0.03
        else:
            prob += 0.03
    else:
        prob += 0.025

plotOccurances(wonPackProbs)
plotOccurances(wonPackMatches)

print(getMedian(wonPackProbs))
print(getMedian(wonPackMatches))