import numpy as np


# Return cartesian distance between points A and B
def distance(A, B):
    x = (A[0]-B[0])**2 + (A[1]-B[1])**2
    return np.sqrt(x)


# Return list of coordinates adjacent to current pos, given a direction
def adjacent(pos, dir=[0,0]):
    # List of coordinates to return
    coords = []
    
    # List of all straight and diagonal directions
    directions = [
        [-1,-1],
        [0,-1],
        [1,1],
        [-1,0],
        [1,0],
        [-1,-1],
        [1,-1],
        [1,-1]
    ]
    
    # Placeholder - should eventually filter by direction
    for d in directions:
        coords.append(np.add(pos,d))

    return coords


# Find optimal next step given a position and direction
def step(img, pos, dir=[0,0]):
    # Get available moves (adjacent spaces given optional step size and direction)
    coords = adjacent(pos)

    # Find the set of coordinates with the lowest potantial
    for p in coords:
        pass


# Find optimal path from current pos to given radius or edge of map
def pathfinder(img, pos, radius=-1):
    # Initial position and map dimensions
    pos = np.array(pos)
    dims = img.shape

    # Path followed
    X = [pos]

    while not np.any(
        [
            # Check that pos has not reached radius, if one is given
            (radius==-1 or distance(pos, X[0]) >= radius),
            # Check that pos has not reached edge of map
            pos[0] <= 0,
            pos[0] >= dims[0],
            pos[1] <= 0,
            pos[1] >= dims[1]
        ]
    ):
        pass