import numpy as np
import matplotlib.pyplot as plt


def EDDsolver(jobsData):
    """
    Solve the Early Due Date (EDD) scheduling problem and create a Gantt chart for the optimal sequence of jobs.

    Args:
        jobsData (dict): A dictionary containing job data, where keys are job identifiers, and values are dictionaries
                        with the following format:
                        {
                            "processingtime": int,  # The time required to complete the job.
                            "duedate": int           # The due date for the job.
                        }

    Returns:
        None

    This function takes a dictionary of job data, where each job is represented by a unique identifier and has associated
    processing time and due date. It computes the optimal job sequence based on the earliest due date (EDD) rule and
    generates a Gantt chart to visualize the schedule.

    The `jobsData` dictionary should be structured as follows:
    {
        "Job1": {"processingtime": 5, "duedate": 10},
        "Job2": {"processingtime": 4, "duedate": 8},
        ...
    }

    The Gantt chart is displayed using Matplotlib and provides a graphical representation of the job schedule in the
    optimal sequence.

    Example usage:
    jobsData = {
        "Job1": {"processingtime": 5, "duedate": 10},
        "Job2": {"processingtime": 4, "duedate": 8},
        "Job3": {"processingtime": 6, "duedate": 12}
    }
    EDDsolver(jobsData)
    """
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
