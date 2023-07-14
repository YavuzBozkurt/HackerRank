


# TODO greedy algorithm
# NOTE: greedy choice is to connect first 2 shortest ropes
#       at every iteration
def connect(ropes):
    # single or no rope, no connections needed
    if len(ropes) <= 1:
        return 0
    # to store costs incurred while connecting ropes
    costs = []
    # sort the ropes
    ropes.sort()
    # connecting first two ropes
    cost = ropes[0] + ropes[1]
    costs.append(cost)
    # if there are more ropes to connect, then do so
    if len(ropes) > 2:
        for i in range(2, len(ropes)):
            cost += ropes[i]
            costs.append(cost)
    return sum(costs)

# driver program
if __name__ == '__main__':
    ropes = [4, 3, 2, 6]
    print(connect(ropes))