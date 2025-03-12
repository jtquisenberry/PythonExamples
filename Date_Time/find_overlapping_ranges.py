def find_overlapping_intervals(intervals):
    """
    Finds all overlapping intervals in a list of time intervals.

    Args:
        intervals: A list of tuples, where each tuple represents a time interval
                   in the format (start_time, end_time).

    Returns:
        A list of tuples, where each tuple represents a pair of overlapping
        intervals.
    """
    overlapping_intervals = []
    for i in range(len(intervals)):
        for j in range(i + 1, len(intervals)):
            if intervals_overlap(intervals[i], intervals[j]):
                overlapping_intervals.append((intervals[i], intervals[j]))
    return overlapping_intervals
def intervals_overlap(interval1, interval2):
    """
    Checks if two time intervals overlap.

    Args:
        interval1: A tuple representing the first time interval (start_time, end_time).
        interval2: A tuple representing the second time interval (start_time, end_time).

    Returns:
        True if the intervals overlap, False otherwise.
    """
    start1, end1 = interval1
    start2, end2 = interval2
    return max(start1, start2) < min(end1, end2)