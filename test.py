"""
Generate a random 2D test for MHT.
"""
import numpy as np
import time
from openmht import OpenMHT


def get_test_detections():
    """
    :return: An array of randomly-generated detections (ijk) for each frame.
    """
    frame_count = 2
    # dimensionality = 2
    dimensionality = 3

    # Truth values for 3 objects
    # truth_values = [[0, 0], [10, 10], [15, 15]]
    truth_values = [[0, 0, 0], [10, 10, 10]]
    detections = np.zeros((frame_count, len(truth_values), dimensionality))
    for i in range(len(truth_values)):
        detections[:, i] = np.random.normal(truth_values[i], 0.1, size=(frame_count, dimensionality))

    print("Detections: {}".format(detections[::-1]))
    return detections


if __name__ == "__main__":
    start = time.time()

    test_points = get_test_detections()
    mht = OpenMHT(test_points)
    mht.run()
    print(mht)

    end = time.time()
    elapsed_seconds = end - start
    print("Elapsed time (s) {0:.2f}".format(elapsed_seconds))

    elapsed_formatted = time.strftime('%H:%M:%S', time.gmtime(elapsed_seconds))
    print(elapsed_formatted)
