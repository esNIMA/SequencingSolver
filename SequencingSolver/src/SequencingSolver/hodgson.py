import numpy as np
from itertools import permutations


def hodgsonSolver(jobsData):
    def createInitialLists(jobsData):
        overdueJobs = []
        processingTimeArray = []
        duedateArray = []
        jobsSequence = []
        for key in jobsData.keys():
            processingTimeArray.append(jobsData[key]["processingtime"])
        for key in jobsData.keys():
            duedateArray.append(jobsData[key]["duedate"])
        return [np.array(processingTimeArray), np.array(duedateArray), overdueJobs, jobsSequence]

    processingTimeArray, duedateArray, overdueJobs, jobsSequence = createInitialLists(
        jobsData)
    k = 1

    def sortDuedates(duedateArray):
        sortedIndex = np.argsort(duedateArray)
        return list(sortedIndex)
    print("k =", k)
    sortedIndex = sortDuedates(duedateArray)
    print("sortedIndex", sortedIndex)
    processingTimeArray = processingTimeArray[sortedIndex]
    print("processingTimeArray:", processingTimeArray)
    duedateArray = duedateArray[sortedIndex]
    print("duedateArray:", duedateArray)

    while k <= len(jobsData):
        if sum(processingTimeArray[:k]) <= duedateArray[k-1]:
            jobsSequence.append(sortedIndex[k-1])
        else:
            processingTimeArray = processingTimeArray[processingTimeArray != (
                max(processingTimeArray[:k]))]
            overdueJobs.append(sortedIndex[k-1])
        print("finalJobsSequence", jobsSequence)
        print("overdueJobs", overdueJobs)
        k = k+1
    for perm in permutations(overdueJobs):
        finalJobsSequnece = jobsSequence.copy()
        finalJobsSequnece.extend(list(perm))
        print("Final Jobs Sequnece(s)", np.array(finalJobsSequnece)+1)
