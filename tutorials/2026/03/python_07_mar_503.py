# Greedy Interval Scheduling
# This algorithm solves the interval scheduling problem by sorting the intervals by their end time and then selecting the earliest one

def find_interval_start_end_time(intervals):
    # Create a list of tuples containing the start and end times of the intervals
    interval_times = [(start, end) for start, end in intervals]

    # Sort the intervals based on their end time
    interval_times.sort(key=lambda x: x[1])

    # Return the sorted interval times
    return interval_times

def greedy_interval_scheduling(intervals):
    # Find the start and end times of the intervals
    interval_start_end_time = find_interval_start_end_time(intervals)

    # Initialize an empty list to store the selected intervals
    selected_intervals = []

    # Initialize the earliest end time to negative infinity
    earliest_end_time = float('-inf')

    # Iterate over the sorted interval times
    for start, end in interval_start_end_time:
        # If the start time of the current interval is greater than or equal to the earliest end time
        if start >= earliest_end_time:
            # Add the current interval to the selected intervals
            selected_intervals.append((start, end))
            # Update the earliest end time to the end time of the current interval
            earliest_end_time = end

    # Return the selected intervals
    return selected_intervals

# Example usage
intervals = [(1, 3), (2, 4), (5, 7), (6, 8)]
selected_intervals = greedy_interval_scheduling(intervals)
print("Selected Intervals:", selected_intervals)

# Run the example