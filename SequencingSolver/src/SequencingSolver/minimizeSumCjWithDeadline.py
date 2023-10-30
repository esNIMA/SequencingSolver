import numpy as np
import matplotlib.pyplot as plt


def minimizeSumCjstDeadline(jobsData):
    """
    Solve a scheduling problem to minimize the sum of completion times (Cj) while meeting job deadlines.

    Args:
        jobsData (dict): A dictionary containing job data, where keys are job identifiers, and values are dictionaries
                        with the following format:
                        {
                            "processingtime": int,  # The time required to complete the job.
                            "deadline": int           # The job's deadline.
                        }

    Returns:
        None

    This function applies an algorithm to schedule jobs with the goal of minimizing the sum of completion times (Cj)
    while ensuring that job deadlines are met. It computes the optimal job sequence and generates a Gantt chart to
    visualize the schedule.

    The `jobsData` dictionary should be structured as follows:
    {
        "Job1": {"processingtime": 5, "deadline": 10},
        "Job2": {"processingtime": 4, "deadline": 8},
        "Job3": {"processingtime": 6, "deadline": 12}
    }

    The function will print the optimal job sequence and create a Gantt chart to represent the job schedule.

    Example usage:
    jobsData = {
        jobsData = {
        1: {"processingtime": 4, "deadline": 10},
        2: {"processingtime": 6, "deadline": 12},
        3: {"processingtime": 2, "deadline": 14},
        4: {"processingtime": 4, "deadline": 18},
        5: {"processingtime": 2, "deadline": 18},
}
    }
    minimizeSumCjstDeadline(jobsData)
    """
    def createInitialLists(jobsData):
        processingTimeArray = []
        deadlineArray = []
        for key in jobsData.keys():
            processingTimeArray.append(jobsData[key]["processingtime"])
        for key in jobsData.keys():
            deadlineArray.append(jobsData[key]["deadline"])
        return [np.array(processingTimeArray), np.array(deadlineArray)]

    reverseOptimalSequence = []
    processingTimeArray, deadlineArray = createInitialLists(jobsData)
    k = len(jobsData)
    tau = sum(processingTimeArray[:k + 1])
    gantt_data = []
    dataCopy=jobsData.copy()
    while jobsData!={}:
        candidateJobs=[]
        for job in jobsData.keys():
            if jobsData[job]["deadline"] >=tau:
                candidateJobs.append((job,jobsData[job]["processingtime"]))
        print("Candidate jobs",sorted(candidateJobs, key=lambda x: x[1], reverse=True))
        reverseOptimalSequence.append(sorted(candidateJobs, key=lambda x: x[1], reverse=True)[0][0])
        tau= tau - sorted(candidateJobs, key=lambda x: x[1], reverse=True)[0][1]
        jobsData.pop(sorted(candidateJobs, key=lambda x: x[1], reverse=True)[0][0])
        print("tau",tau)
        print("reverseOptimalSequence",reverseOptimalSequence)
    OptimalSequence = reverseOptimalSequence[::-1]
    print("The optimal sequence is:", OptimalSequence)

    gantt_data = {}
    current_time = 0

    for job in OptimalSequence:
        job_processing_time = dataCopy[job]["processingtime"]
        gantt_data[job] = (current_time, current_time + job_processing_time)
        current_time += job_processing_time

    # Create a Gantt chart
    fig, ax = plt.subplots()
    for job, (start, end) in gantt_data.items():
        ax.barh(job, end - start, left=start, color='b',
                edgecolor='k', align='center')

    ax.set_xlabel('Time')
    ax.set_ylabel('Job')
    ax.set_yticks(OptimalSequence)
    ax.set_yticklabels(OptimalSequence)
    plt.show()