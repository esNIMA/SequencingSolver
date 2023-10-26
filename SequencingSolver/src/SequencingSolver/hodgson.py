import numpy as np
from itertools import permutations


def hodgsonSolver(jobsData):
    """
    Solve a scheduling problem using the Hodgson algorithm and generate alternative job sequences.

    Args:
        jobsData (dict): A dictionary containing job data, where keys are job identifiers, and values are dictionaries
                        with the following format:
                        {
                            "processingtime": int,  # The time required to complete the job.
                            "duedate": int           # The due date for the job.
                        }

    Returns:
        None

    This function applies the Hodgson algorithm to schedule jobs based on their processing times and due dates. It
    attempts to minimize the number of overdue jobs. The algorithm generates and displays alternative job sequences
    that may lead to better scheduling results by permuting overdue jobs.

    The `jobsData` dictionary should be structured as follows:
    {
        "Job1": {"processingtime": 5, "duedate": 10},
        "Job2": {"processingtime": 4, "duedate": 8},
        "Job3": {"processingtime": 6, "duedate": 12}
    }

    The function will print and display various job sequences, both with and without permutations of overdue jobs,
    to provide insights into scheduling alternatives.

    Example usage:
    jobsData = {
        "Job1": {"processingtime": 5, "duedate": 10},
        "Job2": {"processingtime": 4, "duedate": 8},
        "Job3": {"processingtime": 6, "duedate": 12}
    }
    hodgsonSolver(jobsData)
    """
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
