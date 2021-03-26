import heapq, itertools


def kth_largest_element(arr, k):
    minheap = list()

    for x in itertools.islice(arr, k):
        heapq.heappush(minheap, x)

    res = [minheap[0]]

    for x in arr:
        heapq.heappushpop(minheap, x)
        res.append(minheap[0])

    return res


def main():
    arr = [2, 4, 5, 2, 5, 7, 3, 56, 2, 5, 6, 3, 4, 56]
    k = 4
    res = kth_largest_element(iter(arr), k)
    print(res)


if __name__ == '__main__':
    main()
