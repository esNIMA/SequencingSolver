# SequencingSolver

A Python package for solving various sequencing problems by Nima Mahmoodian.

## How to install the library?

To run the library, you need Numpy and Matplotlib to be installed. Then in the command line, run the following command:

**Linux/Mac:**
```bash
python3 -m pip install SequencingSolver
```
**Windows:**

For Windows, use the following command in the command prompt:
```bash
py -m pip install SequencingSolver
```
## How to use the library?

in version 1.0.2 of the library, there are currently six optimization algorithms: WSPT, WDSPT, EDD, Hodgson, LCL, and minimizeSumCjStDeadline. 
for using any solver, all you need to do is to pass the correct form of data structure (which I call jobsData) to the corresponding solver. 

Let's take a quick look at each. 

# WSPT Solver
Solves a scheduling problem using the Weighted Shortest Processing Time (WSPT) algorithm and create a Gantt chart.

  **Args:**
        jobsData (dict): A dictionary containing job data, where keys are job identifiers, and values are dictionaries
                        with the following format:
                        {
                            "processingtime": int,  # The time required to complete the job.
                            "weight": int            # The weight of the job.
                        }
it returns the optimal sequence and the corresponding Gantt chart. 
    
**Example usage:**
```bash
    jobsData = {
        "Job1": {"processingtime": 5, "weight": 10},
        "Job2": {"processingtime": 4, "weight": 8},
        "Job3": {"processingtime": 6, "weight": 12}
    }
    wsptSolver(jobsData)
 ```
# WDSPT Solver
Solve a scheduling problem using the Weighted Discounted Shortest Processing Time (WDSPT) algorithm and create a Gantt chart.

  **Args:**
        jobsData (dict): A dictionary containing job data, where keys are job identifiers, and values are dictionaries
                        with the following format:
                        {
                            "processingtime": int,  # The time required to complete the job.
                            "weight": int            # The weight of the job.
                        }
        r (float): A discount factor for adjusting the criteria calculation.
  it returns the optimal sequence and the corresponding Gantt chart. 

   **Example usage:**
   ```bash
    jobsData = {
        "Job1": {"processingtime": 5, "weight": 10},
        "Job2": {"processingtime": 4, "weight": 8},
        "Job3": {"processingtime": 6, "weight": 12}
    }
    wdsptSolver(jobsData, r=0.1)
```

# EDD Solver
    Solve the Early Due Date (EDD) scheduling problem and create a Gantt chart for the optimal sequence of jobs.

  **Args:**
        jobsData (dict): A dictionary containing job data, where keys are job identifiers, and values are dictionaries
                        with the following format:
                        {
                            "processingtime": int,  # The time required to complete the job.
                            "duedate": int           # The due date for the job.
                        }

**Example usage:**
```bash
    jobsData = {
        "Job1": {"processingtime": 5, "duedate": 10},
        "Job2": {"processingtime": 4, "duedate": 8},
        "Job3": {"processingtime": 6, "duedate": 12}
    }
```

# Hodgson Solver
Solve a scheduling problem using the Hodgson algorithm and generate alternative job sequences.

**Args:**
        jobsData (dict): A dictionary containing job data, where keys are job identifiers, and values are dictionaries
                        with the following format:
                        {
                            "processingtime": int,  # The time required to complete the job.
                            "duedate": int           # The due date for the job.
                        }
    **Example usage:**
```bash
    jobsData = {
        "Job1": {"processingtime": 5, "duedate": 10},
        "Job2": {"processingtime": 4, "duedate": 8},
        "Job3": {"processingtime": 6, "duedate": 12}
    }
    hodgsonSolver(jobsData)
 ```
# LCL Solver
Solve a scheduling problem using the Lowest Cost Last (LCL) algorithm and create a Gantt chart for the optimal sequence.

  **Args:**
        jobsData (dict): A dictionary containing job data, where keys are job identifiers, and values are dictionaries
                        with the following format:
                        {
                            "processingtime": int,  # The time required to complete the job.
                            "successors": set,      # A set of job identifiers that depend on this job.
                            "hFunction": function  # A function for computing the h value.
                        }
  **important note**
  You must always pass jobsComplementarySet, jobsData, and j to the h calculator function. No matter wether it uses them or not. 

   **Example usage:**
```bash
    jobsData = {
        "Job1": {"processingtime": 5, "successors": {"Job2"}, "hFunction": some_function},
        "Job2": {"processingtime": 4, "successors": set(), "hFunction": some_function},
        "Job3": {"processingtime": 6, "successors": {"Job1", "Job2"}, "hFunction": some_function}
    }
    lclSolver(jobsData)
```

# minimizeSumCjStDeadline

Solve a scheduling problem to minimize the sum of completion times (Cj) while meeting job deadlines.

**Args:**
        jobsData (dict): A dictionary containing job data, where keys are job identifiers, and values are dictionaries
                        with the following format:
                        {
                            "processingtime": int,  # The time required to complete the job.
                            "deadline": int           # The job's deadline.
                        }
This function applies an algorithm to schedule jobs with the goal of minimizing the sum of completion times (Cj)
while ensuring that job deadlines are met. It computes the optimal job sequence and generates a Gantt chart to visualize the schedule.
The function will print the optimal job sequence and create a Gantt chart to represent the job schedule.

**Example usage:**
```bash
    jobsData = {
        "Job1": {"processingtime": 5, "deadline": 10},
        "Job2": {"processingtime": 4, "deadline": 8},
        "Job3": {"processingtime": 6, "deadline": 12}
    }
    minimizeSumCjstDeadline(jobsData)
```
