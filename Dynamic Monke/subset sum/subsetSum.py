
# TODO: dynamic programming algorithm
def subsetSumDP(set, sum):
    # initialize the tabulation table
    T = [[0 for _ in range(sum+1)] for _ in range(len(set)+1)]

    # base case
    for i in range(len(T)):
        T[i][0] = True

    # base case
    for j in range(1, len(T[0])):
        T[0][j] = False

    for i in range(1, len(T)):
        for j in range(1, len(T[0])):
            # recursive formula
            T[i][j] = T[i - 1][j - set[i - 1]] or T[i-1][j]

    # return the solution
    return T[len(T)-1][len(T[0])-1]


if __name__ == "__main__":
    print(subsetSumDP([1, 2, 5, 6, 9], 14))



