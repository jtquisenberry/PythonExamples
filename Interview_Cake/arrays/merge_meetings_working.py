def get_merged_meetings(meetings):
    if len(meetings) < 1:
        raise ValueError

    print('meetings', meetings)
    meetings.sort(key=lambda x: x[0])

    merged_meetings = [meetings[0]]

    for current_start, current_end in meetings[1:]:
        merged_start, merged_end = merged_meetings[-1]
        if current_start <= merged_end:
            merged_meetings[-1] = (merged_start, max(merged_end, current_end))
        else:
            merged_meetings.append((current_start, current_end))

    print('merged_meetings', merged_meetings)
    return merged_meetings









if __name__ == '__main__':
    meetings1 = [(5, 8), (1, 4), (6, 8)]
    meetings2 = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
    meetings3 = [(1, 8), (2, 5)]
    merged_meetings = get_merged_meetings(meetings1)
    merged_meetings = get_merged_meetings(meetings2)
    merged_meetings = get_merged_meetings(meetings3)