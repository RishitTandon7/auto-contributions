# Greedy Interval Scheduling
# This code implements the greedy algorithm for interval scheduling
# The idea is to sort the intervals by their end time and then schedule them greedily

def schedule_intervals(intervals):
    # Sort the intervals by their end time
    intervals.sort(key=lambda x: x[1])

    # Initialize the current time and the scheduled intervals
    current_time = 0
    scheduled_intervals = []

    # Iterate over the sorted intervals
    for start, end in intervals:
        # If the current interval starts after the current time, schedule it
        if start >= current_time:
            scheduled_intervals.append((start, end))
            current_time = end

    return scheduled_intervals

# Example usage
intervals = [(1, 3), (2, 4), (3, 5), (6, 8), (7, 9)]
scheduled_intervals = schedule_intervals(intervals)
print("Scheduled Intervals:", scheduled_intervals)
print("Total Time:", sum(end for start, end in scheduled_intervals))