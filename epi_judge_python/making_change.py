from test_framework import generic_test


def change_making(cents: int) -> int:
    COINS = [100, 50, 25, 10, 5, 1]

    res = 0
    i = 0
    while cents > 0:
        res += cents // COINS[i]
        cents %= COINS[i]
        i += 1
    return res


if __name__ == '__main__':
    exit(generic_test.generic_test_main('making_change.py', 'making_change.tsv', change_making))
