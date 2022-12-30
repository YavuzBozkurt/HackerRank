
# TODO: dynamic programming algorithm
def SDP(arr):

    # initializing tabulation table
    T = [[False for _ in range(sum(arr))] for _ in range(len(arr))]

    # base case
    for j in range(len(T[0])):
        if j+1 in arr:
            T[0][j] = True

    for i in range(1, len(T)):
        for j in range(len(T[0])):
            # recursive formula
            T[i][j] = T[i-1][j] or len([k+1 for k in range(len(T[0])) if T[i-1][k] and (j-k+1) in arr ]) >= 1

    # trivially a sum of 0 is always obtainable
    print(0)

    # print the other obtainable sums
    for j in range(len(T[len(T)-1])):
        if T[len(T)-1][j]:
            print(j+1)

    return True


if __name__ == '__main__':
    arr = [1, 2, 3]
    print(SDP(arr))
