from collections import deque

def find_consecutive_runs(values, run_length=3, step=1):
    """
    Find all runs of three consecutive numbers that increase or decrease by one. Return the start
    indices of the first element in each run. If there are no consecutive runs, None will be
    returned.

    Example: [1, 2, 3, 5, 10, 9, 8, 9, 10, 11, 7, 8, 7] returns [0, 4, 6, 7]

    :param values: A list of integer values to check for consecutive runs.
    :ptype values: list
    :param run_length: The run length to check for.
    :ptype run_length: int
    :param step: The increment or decrement step size in run.
    :ptype step: int
    :return: A list of index values corresponding to where runs begin within the values list.
    :raises: ValueError when run_length is <= 1 or step is < 1
    :rtype: list or None
    """
    run_indices = []
    previous_element = None
    start_indices = deque()
    '''
    direction values:
        -1: current run is decreasing
        0:  current run is just starting
        1:  current run is increasing
    '''
    direction = 0

    if run_length <= 1:
        raise ValueError("Runs of 1 or less are not allowed.")
    if step < 1:
        raise ValueError("Step of less than 1 is not allowed.")

    for index, value in enumerate(values):
        # The value is part of an increasing run
        if value - step == previous_element:
            if direction == -1:
                temp = start_indices.pop()
                start_indices.clear()
                start_indices.append(temp)
            direction = 1
            start_indices.append(index)
        # The value is part of a decreasing run
        elif value + step == previous_element:
            if direction == 1:
                temp = start_indices.pop()
                start_indices.clear()
                start_indices.append(temp)
            direction = -1
            start_indices.append(index)
        # The value is not yet part of a run
        else:
            start_indices.clear()
            start_indices.append(index)
            direction = 0

        # If the number of indices in start_indices is equal to the expected run_length then the
        # first index is the start of a run and should be returned
        if len(start_indices) >= run_length:
            run_indices.append(start_indices.popleft())
        previous_element = value
    if not run_indices:
        run_indices = None
    return run_indices
