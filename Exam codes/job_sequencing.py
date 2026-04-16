# Function for Job Sequencing
def job_sequencing(jobs):
    # Sort jobs by profit (descending)
    jobs.sort(key=lambda x: x[2], reverse=True)

    max_deadline = max(jobs, key=lambda x: x[1])[1]
    slots = [-1] * max_deadline

    total_profit = 0

    for job in jobs:
        job_id, deadline, profit = job

        # Find a free slot (from deadline to 0)
        for j in range(deadline - 1, -1, -1):
            if slots[j] == -1:
                slots[j] = job_id
                total_profit += profit
                break

    return slots, total_profit


# Main program
n = int(input("Enter number of jobs: "))
jobs = []

for i in range(n):
    job_id = input("Enter job id: ")
    deadline = int(input("Enter deadline: "))
    profit = int(input("Enter profit: "))
    jobs.append((job_id, deadline, profit))

result, profit = job_sequencing(jobs)

print("Job sequence:", result)
print("Total profit:", profit)