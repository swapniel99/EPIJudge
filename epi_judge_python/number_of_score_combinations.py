from typing import List

from test_framework import generic_test


def num_combinations_for_final_score(final_score: int, individual_play_scores: List[int]) -> int:
    cache = [0] * (final_score + 1)
    cache[0] = 1
    for play_score in individual_play_scores:
        for score in range(play_score, final_score + 1):
            cache[score] += cache[score - play_score]
    return cache[-1]


if __name__ == '__main__':
    exit(generic_test.generic_test_main('number_of_score_combinations.py', 'number_of_score_combinations.tsv', num_combinations_for_final_score))
