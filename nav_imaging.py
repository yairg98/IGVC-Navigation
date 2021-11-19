from PIL import Image, ImageDraw
import numpy as np
from matplotlib import pyplot as plt


# Return image as array or binary pixels
def get_image(filename):
    img = Image.open(filename).rotate(270)
    img = binarize_image(img)
    return img


# Binarize image (convert to black and white)
def binarize_image(img, threshold=200):
    img = img.convert("L")
    img_data = np.asarray(img)
    binarized_data = (img_data > threshold) * 255
    return binarized_data


# Convert img object into a list of points for a scatterplot
def get_scatter_data(img, xlim=None, ylim=None):
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
    X = np.transpose(get_scatter_data(img, xlim, ylim))
    path = np.transpose(path)

    # Plot map and path data as scatterplots
    plt.figure()
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.scatter(X[0], X[1], zorder=1)
    plt.scatter(path[0], path[1], zorder=2)
    plt.show()