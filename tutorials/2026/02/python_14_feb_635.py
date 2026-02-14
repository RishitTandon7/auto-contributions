def greedy_interval_scheduling(events):
    # Sort the events based on their end time
    events.sort(key=lambda x: x[1])

    # Initialize the start and end times of the selected interval
    start = events[0][0]
    end = events[0][1]

    # Iterate over the sorted events
    for event in events[1:]:
        # If the current event starts after the last selected interval ends, 
        # update the end time of the last selected interval and the start time of the current event
        if event[0] >= end:
            end = event[1]
            start = event[0]

    return (start, end)


# Test the function with some example events
events = [(1, 5), (2, 3), (4, 6), (7, 8)]
print("Original Events: ", events)

selected_interval = greedy_interval_scheduling(events)
print("Selected Interval: ", selected_interval)