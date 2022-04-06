from navigator import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Animator:

    # Constructor for Animator class
    def __init__(self, env, car):
        self.env = env
        # self.path = car.path
        self.path = car # temporary line until Car class is completed

    # Animation of car movement through complete, fixed-frame map
    def fullview(self):
        
        env = self.env
        path = self.path

        # Create figure and axes
        fig = plt.figure(figsize=(7,7))
        ax = fig.add_axes([0,0,1,1])
        ax.set_xlim([0, env.img.shape[0]])
        ax.set_ylim([0, env.img.shape[1]])

        # Initialize scatterplot data
        X = np.transpose(env.as_scatterplot())
        pos = path[0]

        # Generate initial map and car scatterplots
        map_scat = ax.scatter(X[0], X[1], color='black')
        car_scat = ax.scatter([pos[0]], [pos[1]], color='red')

        # Internal function to update animation frame by frame
        def update(i):
            pos = path[i]
            car_scat.set_offsets(pos)

        # Construct and save the animation using the update function
        animation = FuncAnimation(fig, update, frames=range(len(path)), interval=10)
        animation.save("fullview_animation.mp4")

    # Animation of car movement in car-fixed reference frame w/ given radius
    def moving_window(self, rad):
        
        env = self.env
        path = self.path

        # Create figure and axes
        fig = plt.figure(figsize=(7,7))
        ax = fig.add_axes([0,0,1,1])
        ax.set_xlim([0, env.img.shape[0]])
        ax.set_ylim([0, env.img.shape[1]])

        # Initialize scatterplot data
        X = np.transpose(env.as_scatterplot())
        pos = path[0]

        # Generate initial map and car scatterplots
        map_scat = ax.scatter(X[0], X[1], color='black')
        car_scat = ax.scatter([pos[0]], [pos[1]], color='red')

        # Internal function to update animation frame by frame
        def update(i):
            pos = path[i]
            car_scat.set_offsets(pos)
            ax.set_xlim(pos[0]-rad, pos[0]+rad)
            ax.set_ylim(pos[1]-rad, pos[1]+rad)

        # Construct and save the animation using the update function
        animation = FuncAnimation(fig, update, frames=range(len(path)), interval=10)
        animation.save("moving_window_animation.mp4")

    # Animation of observable part of map from car perspective
    def carview(self, rad):

        env = self.env
        path = self.path

        # Find window limits
        pos = path[0]
        xlim = (pos[0]-rad, pos[0]+rad)
        ylim = (pos[1]-rad, pos[1]+rad)

        # Create figure and axes
        fig = plt.figure(figsize=(7,7))
        ax = fig.add_axes([0,0,1,1])
        ax.set_xlim([0, env.img.shape[0]])
        ax.set_ylim([0, env.img.shape[1]])

        # Generate map with initial data
        X = env.lidar_filter(pos, xlim, ylim)
        map_scat = ax.scatter(X[0], X[1], color='black')
        car_scat = ax.scatter([pos[0]], [pos[1]], color='red')

        # Internal function to update animation frame by frame
        def update(i):
            pos = path[i]
            xlim = (pos[0]-rad, pos[0]+rad)
            ylim = (pos[1]-rad, pos[1]+rad)
            X = env.lidar_filter(pos, xlim, ylim)
            map_scat.set_offsets(X)
            car_scat.set_offsets(pos)
            ax.set_xlim(xlim[0], xlim[1])
            ax.set_ylim(ylim[0], ylim[1])

        # Construct and save the animation using the update function
        animation = FuncAnimation(fig, update, frames=len(path), interval=10)
        animation.save("carview_animation.mp4")
        