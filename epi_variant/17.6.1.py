from typing import List

MPG = 20


# gallons[i] is the amount of gas in city i, and distances[i] is the
# distance city i to the next city.
def find_ample_city(gallons: List[int], distances: List[int]) -> int:
    tank = 0
    min_tank = float('inf')
    min_i = None
    for i in range(len(gallons)):
        if tank < min_tank:
            min_tank = tank
            min_i = i
        tank += gallons[i]
        tank -= distances[i] / MPG

    return min_i if tank >= 0 else -1


def find_ample_city_wrapper(gallons, distances):
    result = find_ample_city(gallons, distances)
    num_cities = len(gallons)
    tank = 0
    for i in range(num_cities):
        city = (result + i) % num_cities
        tank += gallons[city] * MPG - distances[city]
        if tank < 0 and result != -1:
            raise Exception('Out of gas on city {}'.format(i))


find_ample_city_wrapper([50, 20, 5, 30, 25, 10, 10], [900, 600, 200, 400, 600, 200, 100])
