def print_job_scheduling(arr, t):
    n = len(arr)

    # Sort all jobs according to decreasing order of profit
    # arr[i][0] is job ID, arr[i][1] is deadline, arr[i][2] is profit
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j][2] < arr[j + 1][2]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    # To keep track of free time slots
    result = [False] * t
    # To store result (Sequence of jobs)
    job = ['-1'] * t

    # Iterate through all given jobs
    for i in range(len(arr)):
        # Find a free slot for this job (Note that we start
        # from the last possible slot)
        for j in range(min(t - 1, arr[i][1] - 1), -1, -1):
            # Free slot found
            if result[j] is False:
                result[j] = True
                job[j] = arr[i][0]
                break

    print("\nFollowing is maximum profit sequence of jobs:")
    print([j for j in job if j != '-1'])


if __name__ == '__main__':
    # Job ID, Deadline, Profit
    arr = [['a', 2, 100],
           ['b', 1, 19],
           ['c', 2, 27],
           ['d', 1, 25],
           ['e', 3, 15]]

    print("Given Jobs (Job ID, Deadline, Profit):")
    for job in arr:
        print(job)

    # Calculate maximum deadline
    max_deadline = max(job[1] for job in arr)
    
    print_job_scheduling(arr, max_deadline)
