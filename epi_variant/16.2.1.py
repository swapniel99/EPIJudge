
# Time O(mn), Space O(min(m, n))
def levenshtein_distance(A: str, B: str) -> int:
    if len(A) < len(B):
        A, B = B, A

    m, n = len(A), len(B)
    cache = list(range(n + 1))

    for i in range(1, m + 1):
        prev = cache[0]
        cache[0] = i
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:
                cache[j], prev = prev, cache[j]
            else:
                cache[j], prev = 1 + min(prev, cache[j], cache[j - 1]), cache[j]

    return cache[-1]
