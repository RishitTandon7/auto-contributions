# Greedy Interval Scheduling
================================

## Overview

Greedy interval scheduling is a problem in computer science where we have a set of intervals, each with a start and end time. We need to select the maximum number of non-overlapping intervals such that the total duration is minimized. This problem can be solved using the greedy algorithm.

## Code

```python
def greedy_interval_scheduling(intervals):
    # Sort the intervals based on their end time
    intervals.sort(key=lambda x: x[1])
    
    # Initialize the result with the first interval
    result = [intervals[0]]
    
    # Iterate over the remaining intervals
    for current_interval in intervals[1:]:
        # Get the last selected interval
        last_selected_interval = result[-1]
        
        # If the current interval does not overlap with the last selected interval, add it to the result
        if current_interval[0] >= last_selected_interval[1]:
            result.append(current_interval)
    
    return result

# Test the function
intervals = [(1, 4), (3, 5), (0, 6), (5, 7), (7, 9)]
print(greedy_interval_scheduling(intervals))