import numpy as np
import matplotlib.pyplot as plt


def wdsptSolver(jobsData, r):
    """
    Solve a scheduling problem using the Weighted Discounted Shortest Processing Time (WDSPT) algorithm and create a Gantt chart.

    Args:
        jobsData (dict): A dictionary containing job data, where keys are job identifiers, and values are dictionaries
                        with the following format:
                        {
                            "processingtime": int,  # The time required to complete the job.
                            "weight": int            # The weight of the job.
                        }
        r (float): A discount factor for adjusting the criteria calculation.

    Returns:
        None

    This function applies the Weighted Discounted Shortest Processing Time (WDSPT) algorithm to schedule jobs based on their
    processing times and weights, with the consideration of a discount factor 'r'. It calculates the optimal job sequence and
    generates a Gantt chart to visualize the schedule.

    The `jobsData` dictionary should be structured as follows:
    {
        "Job1": {"processingtime": 5, "weight": 10},
        "Job2": {"processingtime": 4, "weight": 8},
        "Job3": {"processingtime": 6, "weight": 12}
    }

    The `r` parameter adjusts the importance of the discount factor in the criteria calculation.

    The function computes the WDSPT criteria for each job, sorts them, and creates a Gantt chart to represent the schedule.

    Example usage:
    jobsData = {
        "Job1": {"processingtime": 5, "weight": 10},
        "Job2": {"processingtime": 4, "weight": 8},
        "Job3": {"processingtime": 6, "weight": 12}
    }
    wdsptSolver(jobsData, r=0.1)
    """
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
