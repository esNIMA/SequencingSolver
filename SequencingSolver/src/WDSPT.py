import numpy as np
import matplotlib.pyplot as plt


def wdsptSolver(jobsData, r):
    def createInitialLists(jobsData):
        processingTimeArray = []
        weightArray = []
        for key in jobsData.keys():
            processingTimeArray.append(jobsData[key]["processingtime"])
        for key in jobsData.keys():
            weightArray.append(jobsData[key]["weight"])
        return [np.array(processingTimeArray), np.array(weightArray)]

    processingTimeArray, weightArray = createInitialLists(jobsData)

    def calculateCriteria(processingTimeArray, weightArray):
        criteria = np.divide(
            weightArray*(np.e**(-r*processingTimeArray)), 1-(np.e**(-r*processingTimeArray)))
        print(criteria)
        return criteria

    criteria = calculateCriteria(processingTimeArray, weightArray)

    def calculateSortedIndex(criteria):
        sortedIndex = []
        # Connect each index to the related criteria and sort by criteria value
        # Create a list of tuples (index, criteria)
        indexedCriteria = list(enumerate(criteria))
        # Sort by criteria value
        sortedCriteria = sorted(
            indexedCriteria, key=lambda x: x[1], reverse=True)
        for index, divisionResults in sortedCriteria:
            sortedIndex.append(index)
        print(sortedIndex)
        return sortedIndex

    sortedIndex = calculateSortedIndex(criteria)

    def calculateTotalCompletionTime(processingTimeArray, weightArray, sortedIndex):
        completionTime = np.cumsum(processingTimeArray[sortedIndex])
        totalWeightedCompletionTime = np.sum(
            weightArray*(1-(np.e**(-r*completionTime))))
        return totalWeightedCompletionTime

    totalWeightedCompletionTime = calculateTotalCompletionTime(
        processingTimeArray, weightArray, sortedIndex)

    print("Total weighted completion time:", totalWeightedCompletionTime)

    # Define a function to create a Gantt chart

    def createGanttChart(processingTimeArray, sortedIndex):
        n = len(processingTimeArray)
        start_times = np.zeros(n)
        end_times = np.zeros(n)

        for i in range(n):
            job_index = sortedIndex[i]
            if i == 0:
                start_times[i] = 0
            else:
                start_times[i] = end_times[i-1]
            end_times[i] = start_times[i] + processingTimeArray[job_index]

        fig, ax = plt.subplots(figsize=(10, 4))
        for i in range(n):
            job_index = sortedIndex[i]
            ax.barh(f"Job {job_index + 1}",
                    end_times[i] - start_times[i], left=start_times[i])

        ax.set_xlabel("Time")
        ax.set_ylabel("Jobs")
        ax.set_title("Gantt Chart")
        plt.grid(axis="x")
        plt.show()

    # Create the Gantt chart based on the sortedIndex
    createGanttChart(processingTimeArray, sortedIndex)
