import numpy as np
import matplotlib.pyplot as plt


def EDDsolver(jobsData):
    def createInitialLists(jobsData):
        processingTimeArray = []
        duedateArray = []
        for key in jobsData.keys():
            processingTimeArray.append(jobsData[key]["processingtime"])
        for key in jobsData.keys():
            duedateArray.append(jobsData[key]["duedate"])
        return [np.array(processingTimeArray), np.array(duedateArray)]

    processingTimeArray, duedateArray = createInitialLists(jobsData)

    def sortDuedates(duedateArray):
        sortedIndex = np.argsort(duedateArray)
        return sortedIndex

    sortedIndex = sortDuedates(duedateArray)
    optimalSequence = [job_index + 1 for job_index in sortedIndex]
    print("the optimal sequence is:", optimalSequence)

    # Define a function to create a Gantt chart

    def createGanttChart(processingTimeArray, optimalSequence):
        n = len(processingTimeArray)
        start_times = np.zeros(n)
        end_times = np.zeros(n)

        for i in range(n):
            job_index = optimalSequence[i] - 1
            if i == 0:
                start_times[i] = 0
            else:
                start_times[i] = end_times[i - 1]
            end_times[i] = start_times[i] + processingTimeArray[job_index]

        fig, ax = plt.subplots(figsize=(10, 4))
        for i in range(n):
            job_index = optimalSequence[i] - 1
            ax.barh(f"Job {job_index + 1}",
                    end_times[i] - start_times[i], left=start_times[i])

        ax.set_xlabel("Time")
        ax.set_ylabel("Jobs")
        ax.set_title("Gantt Chart (Optimal Sequence)")
        plt.grid(axis="x")
        plt.show()

    # Create the Gantt chart based on the optimal sequence
    createGanttChart(processingTimeArray, optimalSequence)
