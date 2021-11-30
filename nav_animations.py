from nav_imaging import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Animation of car movement through complete, fixed-frame map
def fullview_animation(img, path):
    
    # Create figure and axes
    fig = plt.figure(figsize=(7,7))
    ax = fig.add_axes([0,0,1,1])
    ax.set_xlim([0, img.shape[0]])
    ax.set_ylim([0, img.shape[1]])

    # Initialize scatterplot data
    X = np.transpose(img_to_scatterplot(img))
    pos = path[0]

    # Generate initial map and car scatterplots
    map_scat = ax.scatter(X[0], X[1], color='black')
    car_scat = ax.scatter([pos[0]], [pos[1]], color='red')

    # Internal function to update animation frame by frame
    def update(i):
        pos = path[i]
        car_scat.set_offsets(pos)

    # Construct and save the animation using the update function
    # TODO: Consider returning animation object and saving separately
    animation = FuncAnimation(fig, update, frames=range(len(path)), interval=10)
    animation.save("fullview_animation.mp4")


# Animation of car movement in car-fixed reference frame w/ given radius
def moving_window_animation(img, path, rad):
    
    # Create figure and axes
    fig = plt.figure(figsize=(7,7))
    ax = fig.add_axes([0,0,1,1])
    ax.set_xlim([0, img.shape[0]])
    ax.set_ylim([0, img.shape[1]])

    # Initialize scatterplot data
    X = np.transpose(img_to_scatterplot(img))
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
    # TODO: Consider returning animation object and saving separately
    animation = FuncAnimation(fig, update, frames=range(len(path)), interval=10)
    animation.save("carview_animation.mp4")


# Animation of observable part of map from car perspective
def carview_animation(img, path, rad, resolution):
    
    # 1. Convert to scatterplot data format
    # 2. 
    
    pass

# Animation of mapping progress showing "discovered" areas only
def mapping_animation(img, path, rad, res):
    pass