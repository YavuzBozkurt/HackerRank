

def backtr(arr, pos, rec):

    if pos == len(arr) - 1:
        print(rec)
        rec.append(arr)
        return rec

    for s in ['p', 'q']:
        arr[pos + 1] = s
        rec = backtr(arr, pos + 1, rec)
        arr[pos + 1] = ''

    return rec

res = backtr(
    ['' for i in range(3)],
    -1,
    []
)
print(res)