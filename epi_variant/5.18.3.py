
# Time O(p) Space O(p) for set
def spiral_coodrinates(p):
    if p == 0:
        return list()

    res = [(0, 0)]
    p -= 1

    if p == 1:
        return res

    directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    res_set = set(res)
    dir = 3

    coord = (0, 0)
    for _ in range(p):
        next_dir = (dir + 1) % 4
        next_dir_d = directions[next_dir]
        next_dir_coord = (coord[0] + next_dir_d[0], coord[1] + next_dir_d[1])
        if next_dir_coord not in res_set:
            res.append(next_dir_coord)
            res_set.add(next_dir_coord)
            dir = next_dir
            coord = next_dir_coord
        else:
            dir_d = directions[dir]
            dir_coord = (coord[0] + dir_d[0], coord[1] + dir_d[1])
            res.append(dir_coord)
            res_set.add(dir_coord)
            coord = dir_coord

    return res


def main():
    p = 10
    res = spiral_coodrinates(p)
    print(res)


if __name__ == '__main__':
    main()
