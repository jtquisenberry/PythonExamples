def merge_ranges(meetings):
    if type(meetings) is not list:
        raise TypeError("meetings must be a list")

    if len(meetings) == 0:
        return meetings

    sorted_meetings = sorted(meetings, key=lambda x: x[0])

    merged_meetings = [(sorted_meetings[0][0], sorted_meetings[0][1])]

    for meeting in sorted_meetings:
        last_start = merged_meetings[-1][0]
        last_end = merged_meetings[-1][1]
        current_start = meeting[0]
        current_end = meeting[1]

        if current_start <= last_end:
            merged_meetings[-1] = (last_start, max(last_end, current_end))
        else:
            merged_meetings.append((current_start, current_end))

    return merged_meetings


if __name__ == '__main__':
    
        actual = merge_ranges([(1, 3), (2, 4)])
        expected = [(1, 4)]
        print(actual == expected)

        actual = merge_ranges([(5, 6), (6, 8)])
        expected = [(5, 8)]
        print(actual == expected)

        actual = merge_ranges([(1, 8), (2, 5)])
        expected = [(1, 8)]
        print(actual == expected)

        actual = merge_ranges([(1, 3), (4, 8)])
        expected = [(1, 3), (4, 8)]
        print(actual == expected)

        actual = merge_ranges([(1, 4), (2, 5), (5, 8)])
        expected = [(1, 8)]
        print(actual == expected)

        actual = merge_ranges([(5, 8), (1, 4), (6, 8)])
        expected = [(1, 4), (5, 8)]
        print(actual == expected)

        actual = merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
        expected = [(0, 1), (3, 8), (9, 12)]
        print(actual == expected)

        actual = merge_ranges([])
        expected = []
        print(actual == expected)

        try:
            merge_ranges(3)
        except Exception as e:
            print(e)
