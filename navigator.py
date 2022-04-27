import numpy as np
import random
from environment import *
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt
import bezier
from bezier.hazmat.curve_helpers import get_curvature


# Navigator parent class (abstract class)
class Navigator:

    # Navigator constructor
    def __init__(self, env, car):
        self.env = env
        self.car = car

    # Return cartesian distance between points A and B
    def distance(self, A, B):
        x = (A[0]-B[0])**2 + (A[1]-B[1])**2
        # Subtract very small random value so that no two distances are equal
        return np.sqrt(x) - random.random()*1e-4

    # Convert 2D map into list of obstacles
    # TODO: Add option to provide specific window
    def get_obstacles(self):
        return np.argwhere(self.env.img==0)

    # Abstract function - implemented by specific navigator
    def find_path(self):
        raise NotImplementedError("Must override this method")


# StraightLineNav finds straight-line path in given direction
class StraightLineNav(Navigator):

    # StraightLineNav constructor - inherits Navigator class
    def __init__(self, env, car):
        Navigator.__init__(self, env, car)

    # Placeholder navigation function (straight line to the map edge)
    def find_path(self, step=[1,0]):
        # Initial position and map dimensions
        pos = self.car.pos
        dims = self.env.img.shape

        # Path followed
        X = []

        # Set exit condition (reaching edge of map)
        while not np.any([
            pos[0] <= 0,
            pos[0] >= dims[0],
            pos[1] <= 0,
            pos[1] >= dims[1]]
        ):
            X.append(pos.copy())
            pos = np.asarray(np.add(pos, step))

        # Return full path
        return X


# SimpleNav follows right-hand wall
class SimpleNav(Navigator):

    # SimpleNav constructor - inherits Navigator class
    def __init__(self,env,car):
        Navigator.__init__(self, env, car)

    def find_path(self):
        # Initial position and map dimensions
        pos = self.car.pos
        dims = self.env.img.shape

        # Path followed
        X = []

        # List of possible directions (up,down,left,right)
        dirs = [[1,0],[0,-1],[-1,0],[0,1]]

        d = dirs.index(self.car.dir)

        # Set part 1 exit condition (reaching edge of map)
        while not np.any([
            pos[0] <= 0,
            pos[0] >= dims[0],
            pos[1] <= 0,
            pos[1] >= dims[1]]
        ):
            # Continue going straight until hitting a wall
            if self.env.img[pos[0], pos[1]] != 0:
                X.append(pos.copy())
                next_step = np.asarray(np.add(pos, dirs[d]))
                pos = np.asarray(next_step)

            # After hitting wall continue to part 2
            else:
                break

        # Set part 2 exit condition (edge of map or max length)
        while not np.any([
            pos[0] <= 0+1,
            pos[0] >= dims[0]-1,
            pos[1] <= 0+1,
            pos[1] >= dims[1]-1,
            len(X) > 5000 ]
        ):

            X.append(pos.copy())
            for i in range(1,-3,-1):
                next_step = np.asarray(np.add(pos, dirs[(d+i)%4]))
                if self.env.img[next_step[0], next_step[1]] != 0:
                    pos = np.asarray(next_step)
                    d = (d+i)%4
                    break

        # Return full path
        return X


# KnnNav finds the path that maximizes distance from obstacles 
class KnnNav(Navigator):
    
    # SimpleNav constructor - inherits Navigator class
    def __init__(self,env,car,step=1):
        Navigator.__init__(self, env, car)
        self.knn = NearestNeighbors(n_neighbors=1)
        self.knn.fit(self.get_obstacles())
        self.step = step

    # Find path of greatest absolute distance from nearest obstacle
    def find_path(self, n_steps=5000):

        X = []
        prev = self.car.path
        pos = self.car.pos
        dims = self.env.img.shape
        dirs = [
            [1,0],[0,-1],[-1,0],[0,1]]
        dirs = list(np.multiply(dirs,self.step))

        # Exit condition: edge of map or max path length
        while not np.any([
            pos[0] <= 0,
            pos[0] >= dims[0],
            pos[1] <= 0,
            pos[1] >= dims[1],
            len(X) > n_steps ]
        ):

            # Add position to path
            X.append(pos.copy())

            # List of adjacent positions
            positions = [list(np.add(pos, dir)) for dir in dirs]

            # List of distances between each position and nearest obstacle
            distances = list(np.squeeze(self.knn.kneighbors(positions))[0])

            # List of boolean indicators for whether position has been visited
            unvisited = [0 if (p in X) or (p in prev) else 1 for p in positions]

            i = np.argmax(np.multiply(distances, unvisited))
            pos = positions[i]

        return X
