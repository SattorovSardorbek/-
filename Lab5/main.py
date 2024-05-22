def kmp(text, word):
    n = len(text)
    m = len(word)
    if m > n:
        return -1

    prefix = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and word[i] != word[j]:
            j = prefix[j - 1]
        if word[i] == word[j]:
            j += 1
        prefix[i] = j

    j = 0
    for i in range(n):
        while j > 0 and text[i] != word[j]:
            j = prefix[j - 1]
        if text[i] == word[j]:
            j += 1
        if j == m:
            return i - m + 1
    return -1

def BM(a, t):
    S = set()
    M = len(t)
    d = {}
    for i in range(M - 2, -1, -1):
        if t[i] not in S:
            d[t[i]] = M - i - 1
            S.add(t[i])

    if t[M - 1] not in S:
        d[t[M - 1]] = M

    d['*'] = M
    N = len(a)

    if N >= M:
        i = M - 1
        while (i < N):
            k = 0
            j = 0
            flBreak = False
            for j in range(M - 1, -1, -1):
                if a[i - k] != t[j]:
                    if j == M - 1:
                        off = d[a[i]] if d.get(a[i], False) else d['*']
                    else:
                        off = d[t[j]]

                    i += off
                    flBreak = True
                    break

                k += 1

            if not flBreak:
                print(f"образ найден по индексу {i - k + 1}")
                break
        else:
            print("образ не найден")
    else:
        print("образ не найден")


N = 4
def getInvCount(arr):
    arr1 = []
    for y in arr:
        for x in y:
            arr1.append(x)
    arr = arr1
    inv_count = 0
    for i in range(N * N - 1):
        for j in range(i + 1, N * N):
            if (arr[j] and arr[i] and arr[i] > arr[j]):
                inv_count += 1

    return inv_count

def findXPosition(puzzle):
    for i in range(N - 1, -1, -1):
        for j in range(N - 1, -1, -1):
            if (puzzle[i][j] == 0):
                return N - i

def isSolvable(puzzle):
    invCount = getInvCount(puzzle)

    if (N & 1):
        return ~(invCount & 1)

    else:
        pos = findXPosition(puzzle)
        if (pos & 1):
            return ~(invCount & 1)
        else:
            return invCount & 1

puzzle = [
    [12, 1, 10, 2, ],
    [7, 11, 4, 14, ],
    [5, 0, 19, 15, ],
    [8, 13, 6, 3, ], ]
res = isSolvable(puzzle)
if res:
    print(True)
else:
    print(False)

print(kmp("Sardorbek", "bek"))
print(BM("Sardorbek", "bek"))


