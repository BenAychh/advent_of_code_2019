from day_06 import count_orbits, process_input, get_distance


def test_problem_1_explanation():
    data = ['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L']
    orbits, back_map = process_input(data)
    assert count_orbits(orbits, 'COM', 0) == 42

def test_problem_2_explanation():
    data = ['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L', 'K)YOU', 'I)SAN']
    orbits, back_map = process_input(data)
    assert get_distance({}, orbits, back_map, 'YOU', 'SAN', 0) == 4
