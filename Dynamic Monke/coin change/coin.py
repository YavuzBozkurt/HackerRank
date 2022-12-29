

# TODO: dynamic programming algorithm
def coinDP(coins, sum):
    # initialize the tabulation table
    T = [[0 for _ in range(sum + 1)] for _ in range(len(coins) + 1)]

    # base case
    for i in range(len(T)):
        T[i][0] = 1

    # traverse over the tabulation table
    for i in range(1, len(T)):
        for j in range(1, len(T[0])):

            # if coin value > current sum, then # ways to make it to sum is number of ways making it
            # without that coin
            if coins[i - 1] > j:
                T[i][j] = T[i - 1][j]

            # if coin value <= current sum, then # ways to make it to sum is number of ways making it
            # without the coin + number of ways with the coin
            else:
                T[i][j] += T[i - 1][j]
                T[i][j] += T[i][j - coins[i - 1]]

    # return the solution
    return T[len(T) - 1][len(T[0]) - 1]


if __name__ == '__main__':
    print(coinDP([2], 4))
    print(coinDP([1, 2, 3], 4))




