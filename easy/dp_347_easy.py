input_1 = """1 3
2 3
4 5
"""
input_2 = """2 4
3 6
1 3
6 8
"""
input_3 = """6 8
5 8
8 9
5 7
4 7
"""
input_4 = """15 18
13 16
9 12
3 4
17 20
9 11
17 18
4 5
5 6
4 5
5 6
13 16
2 3
15 17
13 14
"""


def lights(visitors):
    timetable = [int(t) for t in visitors.strip().split()]
    num_hours = max(timetable)
    # False - lights are off, True - ligths are on
    hours = [0] * num_hours
    for i in range(0, len(timetable), 2):
        entered = timetable[i]
        left = timetable[i+1]
        for k in range(entered, left):
            hours[k] = 1

    return sum(hours)

print("should be 3:", lights(input_1))
print("should be 7:", lights(input_2))
print("should be 5:", lights(input_3))
print("bonus:", lights(input_4))
