import numpy as np
import matplotlib.pyplot as plt


def minimizeSumCjstDeadline(jobsData):
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

    while jobsData:
        candidateJobs = [(job, processingtime) for job, processingtime in jobsData.items(
        ) if jobsData[job]["deadline"] >= tau]
        if not candidateJobs:
            break

        candidateJobs.sort(key=lambda x: x[1], reverse=True)
        selected_job, processing_time = candidateJobs[0]

        reverseOptimalSequence.append(selected_job)
        gantt_data.append([selected_job, tau, tau + processing_time])

        tau -= processing_time
        jobsData.pop(selected_job)

    OptimalSequence = reverseOptimalSequence[::-1]
    print("The optimal sequence is:", OptimalSequence)

    gantt_data = {}
    current_time = 0

    for job in OptimalSequence:
        job_processing_time = jobsData[job]["processingtime"]
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
