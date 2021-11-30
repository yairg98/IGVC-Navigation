import numpy as np

def find_bins(bins, dx, dy, ds, p_rad):

    # Find range of obstructed angles
    dx += (1e-16 if dx==0 else 0) # Avoid division by zero
    theta = np.arctan2(dy, dx)
    theta1 = theta - p_rad/ds
    theta2 = theta + p_rad/ds

    # Find index of closest angle to each end of theta range
    arr = np.abs(np.asarray([bins-theta1, bins-theta2]))
    inds = np.argmin(arr, axis=1)

    # Return all bins in range
    return bins[inds[0] : inds[1]]