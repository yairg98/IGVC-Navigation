
'''
Temp file for old code that may still be useful for reference
'''


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
    dirs = [[1,0],[1,-1],[0,-1],[-1,-1],
                [-1,0],[-1,1],[0,1],[1,1]]
    moves = []
    for d in dirs:
        if distance(dir, d) > 1:
            move = np.add(pos, np.multiply(d,step_size))
            moves.append(move)
    return moves


# Find adjacent point with lowest potential
def optimal_move(img, pos, dir, step_size=1):
    # Get list of available moves from current position
    moves = get_moves(pos, dir, step_size)

    # Find optimal move by minimizing potential
    optimal = [moves[0], get_potential(img,moves[0])]
    for move in moves:
        potential = get_potential(img, move)
        print(potential)
        if potential < optimal[1]:
            optimal = [move, potential]
    
    # Return coordinates of optimal move
    print("***"+str(optimal)+"***")
    return optimal[0]


# Find optimal path by following sequence of optimal moves
def pathfinder(img, pos, dir, step_size = 1, radius=-1):

    plt.figure()
    plt.ion()

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
        plt.scatter(pos[0],pos[1])
        plt.show()
        plt.pause(0.001)

    return X
