
from datetime import datetime

# TODO: auxiliary
def check(trainPrev, trainNext):
    # collision avoidance condition
    if trainPrev[2] <= trainNext[1]:
        return True
    return False


# TODO: auxiliary
# NOTE: convert time into minutes relative to 00:00, return the rendered plan
def render(plans):
    for train in plans:
        for i in range(1, 2+1):
            t = datetime.strptime(train[i], "%H:%M")
            ref = datetime.strptime("00:00", "%H:%M")
            tDiff = t - ref
            tPassed = tDiff.total_seconds() / 60
            train[i] = tPassed
    return plans


# TODO greedy algorithm
# NOTE greedy choice lemma is as same as activity selection problem,
#      but per platform here
#      greedily select the earliest departure time trains such that 
#      no two trains collide (i.e. a platform cannot have 2 trains at a time)
def stopTrain(plans):
    # set the variables and stop count
    stops = 0
    platforms, finals = \
        {}, {}
    
    for train in plans:
        if train[3] not in platforms.keys():
            # platforms is where trains will be in sorted order
            # finals is for storing the answers
            platforms[train[3]], finals[train[3]] = \
                [], []
    
    # add the trains in the plan according to platform no.
    for train in plans:
        if train[3] in platforms.keys():
            platforms[train[3]].append(train)

    # sort trains according to departure time 
    for p in platforms.keys():
        platforms[p].sort(key=lambda t: t[2])


    for p in platforms.keys():
            # per platform, at least 1 train can visit during the day
            # (because the platform visit exists for the day)
            finals[p].append(platforms[p][0])

            # greedily schedule trains such that no collision happens
            for i in range(1, len(platforms[p])):
                if check(finals[p][len(finals[p])-1], platforms[p][i]):
                    # no collision, schedule the train for this platform
                    finals[p].append(platforms[p][i])

            # update number of stops in the station 
            stops += len(finals[p])
    return stops, finals

# GeeksForGeeks validated answer
# exercise link: https://www.geeksforgeeks.org/maximum-trains-stoppage-can-provided/
# driver program 
if __name__ == '__main__':
    plans = [
        [1, '10:00', '10:30', 1],
        [2, '10:10', '10:30', 1],
        [3, '10:00', '10:20', 2],
        [4, '10:30', '12:30', 2],
        [5, '12:00', '12:30', 3],
        [6, '09:00', '10:05', 1]
    ]
    plans = render(plans)
    stoppages, schedules = stopTrain(plans)
    print(stoppages)
    for p in schedules.keys():
        print(schedules[p])

