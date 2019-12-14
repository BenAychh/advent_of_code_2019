from typing import Dict, List


def process_input(orbit_strings: List[str]) -> (Dict[str, List[str]], Dict[str, str]):
    orbits: Dict[str, List[str]] = {}
    back_map: Dict[str, str] = {}
    for orbit in orbit_strings:
        orbitor, orbitee = orbit.split(')')
        if orbitor not in orbits:
            orbits[orbitor] = []
        orbits[orbitor].append(orbitee)
        back_map[orbitee] = orbitor
    return orbits, back_map


def count_orbits(orbits: Dict[str, List[str]], center: str, depth: int) -> int:
    count = (1 * depth)
    if center not in orbits:
        return count
    for center in orbits[center]:
        count += count_orbits(orbits, center, depth + 1)
    return count


def get_distance(already_been_there: Dict[str, bool], orbits: Dict[str, List[str]], back_map: Dict[str, str], start: str, end: str, count: int) -> int:
    already_been_there[start] = True
    nearby_objects = []
    if start in orbits:
        nearby_objects = nearby_objects + orbits[start]
    if start in back_map:
        nearby_objects.append(back_map[start])
    if end in nearby_objects:
        return count
    for nearby in nearby_objects:
        if nearby not in already_been_there:
            distance_count = get_distance(already_been_there, orbits, back_map, nearby, end, count + 1)
            if distance_count is not None:
                return distance_count
    return None




if __name__ == '__main__':
    with open('input.txt') as f:
        raw_data: List[str] = []
        for line in f:
            raw_data.append(line.replace('\n', ''))
        orbits, back_map = process_input(raw_data)
        # print(count_orbits(orbits, 'COM', 0))
        print(get_distance({}, orbits, back_map, 'YOU', 'SAN', 0))
