import operator
# TODO: dynamic programming algorithm
def JSDP(jobs):

    # sort the jobs according to their starting time
    jobsSorted = []
    for i in range(len(jobs)):
        tuple = min(jobs, key=operator.itemgetter(1))
        jobsSorted.append(tuple)
        jobs = [job for job in jobs if job != tuple]


    # initialization of the tabulation table
    PJS = [0 for _ in range(len(jobsSorted))]

    # base case
    PJS[0] = jobsSorted[0][2]

    # find the latest job
    latestJob = -1
    endTime = -1
    for i in range(len(PJS)-1):

        # find the latest job before the current job
        for j in range(len(jobsSorted)):
            if endTime < jobsSorted[j][1] < jobsSorted[i + 1][0]:
                endTime = jobsSorted[j][1]
                latestJob = j

            # recursive formula
            PJS[i+1] = max(PJS[latestJob] + jobsSorted[i+1][2], PJS[latestJob])

    # return the solution
    return max(PJS)


# driver code
if __name__ == "__main__":
    jobs = [(2, 5, 6), (1, 3, 5), (4, 9, 20), (6, 11, 9), (8, 12, 13)]
    print(JSDP(jobs))
