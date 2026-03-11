# Greedy Interval Scheduling
#=====================================

def greedy_interval_scheduling(intervals):
    """
    Greedily select the maximum interval that ends at the end of the last selected interval.

    Args:
        intervals (list): A list of intervals, where each interval is a tuple (start, end).

    Returns:
        list: A list of selected intervals.
    """
    # Sort the intervals by their end time
    intervals.sort(key=lambda x: x[1])

    # Initialize the result with the first interval
    result = [intervals[0]]

    # Iterate over the remaining intervals
    for interval in intervals[1:]:
        # Check if the current interval can be scheduled after the last selected interval
        if interval[0] >= result[-1][1]:
            # Add the current interval to the result
            result.append(interval)

    return result

# Example usage
intervals = [(1, 3), (2, 4), (5, 7), (6, 8), (9, 11), (12, 14)]
selected_intervals = greedy_interval_scheduling(intervals)
print("Selected intervals:", selected_intervals)