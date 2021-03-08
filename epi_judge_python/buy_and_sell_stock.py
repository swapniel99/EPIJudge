from typing import List

from test_framework import generic_test


# # Divide and Conquer
# # Time O(n), Space O(log n)
# def buy_and_sell_stock_once(prices: List[float]) -> float:
#     def helper(start, end):
#         if start + 1 == end:
#             return 0, prices[start], prices[start]
#         else:
#             leftr, leftmin, leftmax = helper(start, start + (end - start) // 2)
#             rightr, rightmin, rightmax = helper(start + (end - start) // 2, end)
#             return max(leftr, rightr, rightmax - leftmin), min(leftmin, rightmin), max(leftmax, rightmax)
#     return helper(0, len(prices))[0]


# Time O(n), Space O(1)
def buy_and_sell_stock_once(prices: List[float]) -> float:
    buy = float('inf')
    profit = 0
    for p in prices:
        if p < buy:
            buy = p
        else:
            profit = max(profit, p - buy)
    return profit


if __name__ == '__main__':
    exit(generic_test.generic_test_main('buy_and_sell_stock.py', 'buy_and_sell_stock.tsv', buy_and_sell_stock_once))
