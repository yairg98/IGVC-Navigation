from PIL import Image, ImageDraw
import numpy as np
from matplotlib import pyplot as plt
from helper_methods import *


# Return image as array or binary pixels
def get_image(filename, threshold=200):
    img = Image.open(filename).rotate(270)
    img = img.convert("L")
    img_data = np.asarray(img)
    binarized_data = (img_data > threshold) * 255
    return binarized_data


# Convert img object into a list of points for a scatterplot
def img_to_scatterplot(img, xlim=None, ylim=None):
    # Get plot limits
    xrange = range(0,img.shape[0]) if xlim==None else range(xlim[0], xlim[1])
    yrange = range(0,img.shape[1]) if ylim==None else range(ylim[0], ylim[1])
    
    # Convert img data to list of scatterplot coordinates
    X = []
    for i in xrange:
        for j in yrange:
            if img[i,j] == 0:
                X.append([i,j])
    return X


# Plot the input map as a scatterplot
def plot_map(img, path=[], xlim=None, ylim=None):
    # Get plot limits
    xlim = [0, img.shape[0]] if xlim==None else xlim
    ylim = [0, img.shape[1]] if ylim==None else ylim

    # Get and format data for scatterplot
    X = np.transpose(img_to_scatterplot(img, xlim, ylim))
    path = np.transpose(path)

    # Plot map and path data as scatterplots
    plt.figure()
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.scatter(X[0], X[1], zorder=1)
    plt.scatter(path[0], path[1], zorder=2)
    plt.show()


# Apply filter to return only part of map visible to the car
def carview_filter(img, pos, xlim, ylim, res):

    # Get list of points
    X = img_to_scatterplot(img, xlim, ylim)

    # Create bins for each arc the snesor detects
    arcs = np.linspace(-np.pi, np.pi, res)
    bins = dict.fromkeys(arcs)

    # Save only the closest point to the car within each arc
    for p in X:

        print(p)
        
        # Get dx, dy, and ds
        dx = p[0] - pos[0]
        dy = p[1] - pos[1]
        ds = np.sqrt(dx**2 + dy**2)

        print([dx,dy,ds])
        
        # Identify correct bin
        dx += (1e-16 if dx==0 else 0) # Avoid division by zero
        theta = np.arctan(dy/dx)
        b = find_bin(arcs, theta)
        print([theta, b])
        
        # Add p to bin, if necessary
        if bins[b] == None or ds < bins[b][1]:
            bins[b] = [p, ds]

        # Return new data:
        X = [p[0] for p in bins.items()]
    return X