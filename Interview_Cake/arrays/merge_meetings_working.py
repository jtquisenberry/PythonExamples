def merge_ranges(meetings):

    meetings.sort(key=lambda x: x[0])
    merged_meetings = []
    last_start = meetings[0][0]
    last_end = meetings[0][1]

    for meeting in meetings:
        current_start, current_end = meeting
        if current_start <= last_end:
            last_end = max(current_end, last_end)
        else:
            merged_meetings.append((last_start, last_end))
            last_start = current_start
            last_end = current_end

    merged_meetings.append((last_start, last_end))
    return merged_meetings

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