import numpy as np


# Navigate road using the right-hand rule
def simple_nav(img, pos):
    # Initial position and map dimensions
    pos = np.array(pos)
    dims = img.shape

    # Path followed
    X = [pos]

    # Set exit condition (reaching edge of map)
    while not np.any([
        pos[0] <= 0,
        pos[0] >= dims[0]-80,
        pos[1] <= 0,
        pos[1] >= dims[1]]
    ):
        # TODO: add right-hand nav algorithm here
        
        # Placeholder nav algorithm (go in straight line)
        pos[0] += 1
        X.append(pos.copy())

    # Return full path
    return X