

def longestCommonSubsequence(text1: str, text2: str) -> str:
    m, n = len(text1), len(text2)

    cache = list()
    for _ in range(m + 1):
        cache.append([0] * (n + 1))

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                cache[i][j] = 1 + cache[i - 1][j - 1]
            else:
                cache[i][j] = max(cache[i][j - 1], cache[i - 1][j])

    i = m
    j = n
    res = list()
    while i > 0 and j > 0:
        if text1[i - 1] == text2[j - 1]:
            res.append(text1[i - 1])
            i -= 1
            j -= 1
        elif cache[i - 1][j] > cache[i][j - 1]:
            i -= 1
        else:
            j -= 1

    res.reverse()
    return ''.join(res)


print(longestCommonSubsequence('Carthosea', 'Orchestra'))
