import collections
import copy
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

WHITE, BLACK = range(2)

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))


def search_maze(maze: List[List[int]], s: Coordinate, e: Coordinate) -> List[Coordinate]:
    m, n = len(maze), len(maze[0])

    def maze_helper(c: Coordinate):
        path.append(c)
        maze[c.x][c.y] = 2
        if c == e:
            ret = True
        else:
            nbcs = [(c.x + 1, c.y), (c.x - 1, c.y), (c.x, c.y + 1), (c.x, c.y - 1)]
            nbcs = map(lambda tup: Coordinate(tup[0], tup[1]), nbcs)
            nbcs = filter(lambda p: 0 <= p.x < m and 0 <= p.y < n and maze[p.x][p.y] == 0, nbcs)
            ret = any(map(maze_helper, nbcs))
        if not ret:
            del path[-1]
        return ret

    path = list()
    maze_helper(s)
    return path


def path_element_is_feasible(maze, prev, cur):
    if not ((0 <= cur.x < len(maze)) and
            (0 <= cur.y < len(maze[cur.x])) and maze[cur.x][cur.y] == WHITE):
        return False
    return cur == (prev.x + 1, prev.y) or \
           cur == (prev.x - 1, prev.y) or \
           cur == (prev.x, prev.y + 1) or \
           cur == (prev.x, prev.y - 1)


@enable_executor_hook
def search_maze_wrapper(executor, maze, s, e):
    s = Coordinate(*s)
    e = Coordinate(*e)
    cp = copy.deepcopy(maze)

    path = executor.run(functools.partial(search_maze, cp, s, e))

    if not path:
        return s == e

    if path[0] != s or path[-1] != e:
        raise TestFailure('Path doesn\'t lay between start and end points')

    for i in range(1, len(path)):
        if not path_element_is_feasible(maze, path[i - 1], path[i]):
            raise TestFailure('Path contains invalid segments')

    return True


if __name__ == '__main__':
    exit(generic_test.generic_test_main('search_maze.py', 'search_maze.tsv', search_maze_wrapper))
