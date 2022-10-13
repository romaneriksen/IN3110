"""
Timing our filter implementations.

Can be executed as `python3 -m instapy.timing`

For Task 6.
"""

import time
import instapy 
from . import get_filter, io
from typing import Callable
import numpy as np


def time_one(filter_function: Callable, *arguments, calls: int = 3) -> float:
    """Return the time for one call

    When measuring, repeat the call `calls` times,
    and return the average.

    Args:
        filter_function (callable):
            The filter function to time
        *arguments:
            Arguments to pass to filter_function
        calls (int):
            The number of times to call the function,
            for measurement
    Returns:
        time (float):
            The average time (in seconds) to run filter_function(*arguments)
    """
    time_sum = 0
    # run the filter function `calls` times
    for i in range(calls):
        start = time.time()
        filter_function(*arguments)
        slutt = time.time() - start
        time_sum += slutt
    
    # return the _average_ time of one call
    return time_sum/calls


def make_reports(filename: str = "test/rain.jpg", calls: int = 3):
    """
    Make timing reports for all implementations and filters,
    run for a given image.

    Args:
        filename (str): the image file to use
    """

    # load the image
    image = io.read_image(filename)
    # print the image name, width, height
    title_timing_report = "Image: {}, width: {}, height: {}".format(filename, image.shape[0], image.shape[1])
    print(title_timing_report)

    # List to store the the entries for the timing-report.txt
    lines = []
    lines.append(title_timing_report)

    # iterate through the filters
    filter_names = ["color2gray", "color2sepia"]
    for filter_name in filter_names:
        # get the reference filter function
        # time the reference implementation
        reference_time = time_one(get_filter(), image)
        reference_time_report = f"Reference (pure Python) filter time {filter_name}: {reference_time:.3}s ({calls=})"
        print(reference_time_report)
        lines.append("\n"+reference_time_report)

        # iterate through the implementations
        implementations = ["numpy", "numba"]
        for implementation in implementations:
            # time the filter
            filter_time = time_one(get_filter(implementation=implementation), image)
            # compare the reference time to the optimized time
            speedup = ((reference_time - filter_time)/reference_time)*100
            filter_time_report = f"Timing: {implementation} {filter_name}: {filter_time:.3}s ({speedup=:.2f}x)"
            print(filter_time_report)
            lines.append(filter_time_report)

    # Write the timing result to the timing-report.txt file
    with open("timing-report.txt", "w") as f:
        for line in lines:
            f.write(line)
            f.write("\n")


if __name__ == "__main__":
    # run as `python -m instapy.timing`
    make_reports()
