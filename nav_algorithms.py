import numpy as np
import random


# Placeholder navigation function (straight line to the map edge)
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
        
        # Placeholder nav algorithm (go in straight line)
        pos[0] += 1
        X.append(pos.copy())

    # Return full path
    return X


# Return cartesian distance between points A and B
def distance(A, B):
    x = (A[0]-B[0])**2 + (A[1]-B[1])**2
    return np.sqrt(x) + random.random()*1e-4


# Convert 2D map into list of obstacles
def get_obstacles(img):
    return np.argwhere(img!=0)


# Calculate potential at given point
# Currently only 
def get_potential(img, pos):
    # Set APF object weights/charges
    c_goal = -.10
    c_breadcrumbs = 1
    c_obstacle = 4.0

    # Initialize potential
    potential = 0

    # Add effect of obstacles on potential
    obstacles = get_obstacles(img)
    for obstacle in obstacles:
        # Can replace with charge/distance if different obstacle types are given different charges
        potential += c_obstacle/distance(pos, obstacle)

    # Add effect of goal on potential
    #   Placeholder linear slope to origin
    potential += c_goal * np.sqrt(pos[0]**2 + pos[1]**2)

    return potential


# Get available moves from given position
#   Placeholder returns all adjacent positions
#   Can be adjusted to account for step size and/or direction
def get_moves(pos, dir, step_size=1):
    dir = np.multiply(dir,-1)
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
    moves = []
    for d in directions:
        if distance(dir, d) > 1:
            moves.append(np.add(pos, np.multiply(dir,step_size)))
    return moves


# Find adjacent point with lowest potential
def optimal_move(img, pos, dir, step_size=1):
    # Get list of available moves from current position
    moves = get_moves(pos, dir, step_size)

    # Find optimal move by minimizing potential
    optimal = [moves[0], get_potential(img,moves[0])]
    for move in moves:
        potential = get_potential(img, move)
        if potential < optimal[1]:
            optimal = [move, potential]
    
    # Return coordinates of optimal move
    return optimal[0]


# Find optimal path by following sequence of optimal moves
def pathfinder(img, pos, dir, step_size = 1, radius=-1):

    # Initial position and map dimensions
    pos = np.array(pos)
    dims = img.shape

    # Path followed
    X = [pos]

    while not np.any(
        [
            # Check that pos has not reached radius, if one is given
            (radius!=-1 and distance(pos, X[0]) >= radius),
            # Check that pos has not reached edge of map
            pos[0] <= 0,
            pos[0] >= dims[0],
            pos[1] <= 0,
            pos[1] >= dims[1]
        ]
    ):
        pos = optimal_move(img, pos, dir, step_size)
        X.append(pos)
        print(pos)

    return X


