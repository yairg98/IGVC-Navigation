from PIL import Image, ImageDraw
import numpy as np
from matplotlib import pyplot as plt


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
    if xlim == None:
        xrange = range(0,img.shape[0])
    else:
        x1 = max(0, xlim[0])
        x2 = min(img.shape[0], xlim[1])
        xrange = range(x1, x2)
    if ylim == None:
        yrange = range(0,img.shape[0])
    else:
        y1 = max(0, ylim[0])
        y2 = min(img.shape[1], ylim[1])
        yrange = range(y1, y2)
    
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


# Return list of bins corresponding to angles obstructed by given point
def find_angle_bins(bins, dx, dy, ds, p_rad):

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


# Apply filter to return only part of map visible to the car
def carview_filter(img, pos, xlim=None, ylim=None, resolution=1000, p_rad=1):

    # Get list of points
    X = img_to_scatterplot(img, xlim, ylim)

    # Create bins for each arc the snesor detects
    arcs = np.linspace(-np.pi, np.pi, resolution)
    bins = dict.fromkeys(arcs)

    # Save only the closest point to the car within each arc
    for p in X:

        # Get dx, dy, and ds
        dx = p[0] - pos[0]
        dy = p[1] - pos[1]
        ds = np.sqrt(dx**2 + dy**2)
        
        # Identify correct bin
        blocked_bins = find_angle_bins(arcs, dy, dx, ds, p_rad)
        
        # Add p to each necessary bin
        for b in blocked_bins:
            if bins[b] == None or ds < bins[b][1]:
                bins[b] = [p, ds]

        # Return new data:
        X = []
        for b in bins:
            if bins[b] != None:
                X.append(bins[b][0])
   
    return X