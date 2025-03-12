def merge_overlapping_intervals(intervals):
    """Merges overlapping time intervals."""
    sorted_intervals = sorted(intervals)
    merged_intervals = []
    for interval in sorted_intervals:
        if not merged_intervals or interval[0] > merged_intervals[-1][1]:
            merged_intervals.append(interval)
        else:
            merged_intervals[-1] = (merged_intervals[-1][0], max(merged_intervals[-1][1], interval[1]))
    return merged_intervals

def check_overlap(interval1, interval2):
    """Checks if two time intervals overlap."""
    return interval1[1] >= interval2[0] and interval2[1] >= interval1[0]

def max_overlapping_intervals(intervals):
    """Finds the maximum number of overlapping intervals."""
    events = []
    for start, end in intervals:
        events.append((start, 1))  # 1 for start event
        events.append((end, -1))   # -1 for end event
    events.sort()
    count = 0
    max_count = 0
    for _, event_type in events:
        count += event_type
        max_count = max(max_count, count)
    return max_count

# Example usage
intervals = [(1, 3), (2, 6), (8, 10), (15, 18)]
merged_intervals = merge_overlapping_intervals(intervals)
print("Merged intervals:", merged_intervals)  # Output: [(1, 6), (8, 10), (15, 18)]

intervals2 = [(1, 5), (3, 7), (2, 4), (6, 8), (6, 8)]
max_overlap = max_overlapping_intervals(intervals2)
print("Max overlapping intervals:", max_overlap)  # Output: 3