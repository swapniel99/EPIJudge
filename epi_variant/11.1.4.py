
def is_a_prefix(A, p):
    start = 0
    end = len(A)

    while start < end:
        mid = start + (end - start) // 2
        s = A[mid]
        if s.startswith(p):
            return True
        elif s < p:
            start = mid + 1
        else:
            end = mid

    return False


def main():
    s = 'sdnkla maskdm ajsdsk ksal ksadf sdaadd sdasdl fmsd'
    A = sorted(s.split())
    p = 'fms'
    print(A, p)
    print(is_a_prefix(A, p))


if __name__ == '__main__':
    main()
