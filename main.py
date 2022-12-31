import numpy as np
from collections import Counter
from collections import OrderedDict
import matplotlib.pyplot as plt

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

#counting occurances with collections
probsCounted = Counter(wonPackProbs)
matchesCounted = Counter(wonPackMatches)

#converting result to a regular dictionary
probsDict = dict(probsCounted)
matchesDict = dict(matchesCounted)

#sorting those dictionaries
probsDict = OrderedDict(sorted(probsDict.items()))
matchesDict = OrderedDict(sorted(matchesDict.items()))

#spliting dictionaries into single dimesion lists
probsKeys = list(probsDict.keys())
probsValues = list(probsDict.values())
matchesKeys = list(matchesDict.keys())
matchesValues = list(matchesDict.values())

#ploting results with those lists
plt.plot(probsKeys, probsValues)
plt.show()

plt.plot(matchesKeys, matchesValues)
plt.show()

#creating a list from a counter of all ordered occurences to see the median
probsListComplete = sorted(probsCounted.elements())
matchesListComplete = sorted(matchesCounted.elements())

#printing the median
print(probsListComplete[int(len(probsListComplete)/2)])
print(matchesListComplete[int(len(matchesListComplete)/2)])

#the median allows us to see at what point, half of packs are obtained after that point
# and half of packs are obtained before that point