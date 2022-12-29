
# TODO: dynamic programming algorithm
def rodDP(rodList, pList):

    # initialize the tabulation table
    T = [[0 for _ in range(len(rodList)+1)] for _ in range(len(rodList)+1)]

    # base case
    for i in range(1, len(T)):
        T[i][0] = pList[i-1]

    for i in range(1, len(T)):
        for j in range(1, len(T[0])):
            if j >= i:
                T[i][j] = T[i][j-1]
            else:
                T[i][j] = max(T[i][j-1], pList[j-1] + max([val for val in T[i-j]]))

    return T[len(T)-1][len(T[0])-1]



if __name__ == '__main__':
    print(rodDP([1, 2, 3, 4, 5, 6, 7, 8], [1, 5, 8, 9, 10, 17, 17, 20]))
