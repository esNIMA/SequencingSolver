import numpy as np
import matplotlib.pyplot as plt


def lclSolver(jobsData):
    """
    Solve a scheduling problem using the Lowest Cost Last (LCL) algorithm and create a Gantt chart for the optimal sequence.

    Args:
        jobsData (dict): A dictionary containing job data, where keys are job identifiers, and values are dictionaries
                        with the following format:
                        {
                            "processingtime": int,  # The time required to complete the job.
                            "successors": set,      # A set of job identifiers that depend on this job.
                            "hFunction": function  # A function for computing the h value.
                        }

    Returns:
        None

    This function applies the Lowest Cost Last (LCL) algorithm to schedule jobs based on their dependencies and
    h-values. It generates an optimal job sequence and creates a Gantt chart to visualize the schedule.

    The `jobsData` dictionary should be structured as follows:
    {
        "Job1": {"processingtime": 5, "successors": {"Job2"}, "hFunction": some_function},
        "Job2": {"processingtime": 4, "successors": set(), "hFunction": some_function},
        "Job3": {"processingtime": 6, "successors": {"Job1", "Job2"}, "hFunction": some_function}
    }

    The `hFunction` for each job computes a value to determine the job's priority.

    The function will print the optimal job sequence and display a Gantt chart to visualize the schedule.

    Example usage:
    jobsData = {
        "Job1": {"processingtime": 5, "successors": {"Job2"}, "hFunction": some_function},
        "Job2": {"processingtime": 4, "successors": set(), "hFunction": some_function},
        "Job3": {"processingtime": 6, "successors": {"Job1", "Job2"}, "hFunction": some_function}
    }
    lclSolver(jobsData)
    """
    def createInitialSets(jobsData):
        jobsUniversalSet = set(jobsData.keys())
        jobsComplementarySet = jobsUniversalSet.copy()
        jobsSet = jobsUniversalSet - jobsComplementarySet
        jobsWithNoSuccessors = [
            key for key, value in jobsData.items() if not value["successors"]]
        return [jobsUniversalSet, jobsComplementarySet, jobsSet, jobsWithNoSuccessors]

    def findMinimumH(jobsData, jobsWithNoSuccessors):
        minimumHList = []
        for j in jobsWithNoSuccessors:
            h_value = jobsData[j]["hFunction"](
                jobsComplementarySet, jobsData, j)
            # Store both j and the corresponding h value
            minimumHList.append((j, h_value))
        if not minimumHList:
            return None  # Handle the case where minimumHList is empty
        min_index, min_value = min(
            enumerate(minimumHList), key=lambda x: x[1][1])
        # min_index contains the index of the minimum value, min_value contains the (j, h) pair
        return jobsWithNoSuccessors[min_index]

    def updateJobsList(jobsUniversalSet, jobsComplementarySet, jobsSet, jobsWithNoSuccessors, reversedOptimalList, jobsData, removedJob):
        jobsComplementarySet = jobsComplementarySet-set(reversedOptimalList)
        jobsSet = jobsUniversalSet-jobsComplementarySet
        for key in jobsData.keys():
            if removedJob in jobsData[key]["successors"]:
                jobsData[key]["successors"] = jobsData[key]["successors"] - \
                    {removedJob}
        jobsWithNoSuccessors = [
            key for key, value in jobsData.items() if not value["successors"]]
        for job in reversedOptimalList:
            if job in jobsWithNoSuccessors:
                jobsWithNoSuccessors.remove(job)
        return [jobsComplementarySet, jobsSet, jobsWithNoSuccessors]

    def plotSequence(jobsData):
        # Calculate start and end times for each job in the optimal sequence
        start_times = []
        end_times = []
        current_time = 0
        colors = []  # List to store unique colors
        for job in OptimalList:
            processing_time = jobsData[job]["processingtime"]
            start_times.append(current_time)
            end_times.append(current_time + processing_time)
            current_time += processing_time

            # Assign a unique color to each job
            colors.append(plt.cm.viridis(len(start_times) / len(OptimalList)))

        # Plot the Gantt chart with different colors for each bar
        plt.figure(figsize=(10, 4))
        for i in range(len(OptimalList)):
            plt.barh(i, end_times[i] - start_times[i],
                     left=start_times[i], height=0.6, color=colors[i])
        plt.yticks(range(len(OptimalList)), [
                   f"Job {job}" for job in OptimalList])
        plt.xlabel("Time")
        plt.title("Gantt Chart")
        plt.grid(axis="x")
        plt.show()

    reversedOptimalList = []
    jobsUniversalSet, jobsComplementarySet, jobsSet, jobsWithNoSuccessors = createInitialSets(
        jobsData=jobsData)
    for itr in jobsData.keys():
        removedJob = findMinimumH(
            jobsData, jobsWithNoSuccessors=jobsWithNoSuccessors)
        reversedOptimalList.append(removedJob)
        print(f"Iteration {itr}:", reversedOptimalList)
        jobsComplementarySet, jobsSet, jobsWithNoSuccessors = updateJobsList(
            jobsUniversalSet, jobsComplementarySet, jobsSet, jobsWithNoSuccessors, reversedOptimalList, jobsData, removedJob)
    OptimalList = reversedOptimalList[::-1]
    print("The Optimal Sequence is:", OptimalList)
    plotSequence(jobsData)
