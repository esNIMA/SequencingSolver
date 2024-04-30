import numpy as np
import matplotlib.pyplot as plt
from timeit import timeit

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
    if not isinstance(jobsData, dict):
        raise ValueError("jobsData must be a dictionary.")
    
    if not jobsData:
        raise ValueError("jobsData cannot be empty.")

    # Error handling for missing or incorrect values in jobsData
    missing_values = [job_id for job_id, data in jobsData.items() if "processingtime" not in data or "duedate" not in data]
    if missing_values:
        raise ValueError(f"Missing values for job(s): {', '.join(missing_values)}")

    invalid_values = [job_id for job_id, data in jobsData.items() if not isinstance(data.get("processingtime", None), int) or not isinstance(data.get("duedate", None), int)]
    if invalid_values:
        raise ValueError(f"Invalid values for job(s): {', '.join(invalid_values)}")
    
    @timeit
    def extract_data(jobsData):
        processingTimes = np.array([data["processingtime"] for data in jobsData.values()])
        dueDates = np.array([data["duedate"] for data in jobsData.values()])
        optimalSequence = np.argsort(dueDates) + 1
        return processingTimes, optimalSequence

    # Extract processing times and find optimal sequence
    processingTimes, optimalSequence = extract_data(jobsData)

    # Define a function to create a Gantt chart
    @timeit
    def createGanttChart(processingTimes, optimalSequence):
        n = len(processingTimes)
        start_times = np.zeros(n)
        end_times = np.zeros(n)

        for i, job_index in enumerate(optimalSequence - 1):
            if i == 0:
                start_times[i] = 0
            else:
                start_times[i] = end_times[i - 1]
            end_times[i] = start_times[i] + processingTimes[job_index]

        fig, ax = plt.subplots(figsize=(10, 4))
        for i, job_index in enumerate(optimalSequence - 1):
            ax.barh(f"Job {job_index + 1}",
                    end_times[i] - start_times[i], left=start_times[i])

        ax.set_xlabel("Time")
        ax.set_ylabel("Jobs")
        ax.set_title("Gantt Chart (Optimal Sequence)")
        plt.grid(axis="x")
        plt.show()


    # Create the Gantt chart based on the optimal sequence
    createGanttChart(processingTimes, optimalSequence)


jobsData = {
    "Job1": {"processingtime": 5, "duedate": 10},
    "Job2": {"processingtime": 4, "duedate": 8},
    "Job3": {"processingtime": 6, "duedate": 12},
    "Job4": {"processingtime": 3, "duedate": 9},
    "Job5": {"processingtime": 7, "duedate": 11},
    "Job6": {"processingtime": 2, "duedate": 7},
    "Job7": {"processingtime": 8, "duedate": 15},
    "Job8": {"processingtime": 5, "duedate": 14},
    "Job9": {"processingtime": 4, "duedate": 10},
    "Job10": {"processingtime": 6, "duedate": 13},
    "Job11": {"processingtime": 3, "duedate": 8},
    "Job12": {"processingtime": 7, "duedate": 16}
}

EDDsolver(jobsData)
