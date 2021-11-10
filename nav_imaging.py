from PIL import Image, ImageDraw
import numpy as np
from matplotlib import pyplot as plt


# Return image as array or binary pixels
def get_image(filename):
    img = Image.open(filename)
    img = binarize_image(img)
    return img


# Binarize image (convert to black and white)
def binarize_image(img, threshold=200):
    img = img.convert("L")
    img_data = np.asarray(img)
    binarized_data = (img_data > threshold) * 255
    return binarized_data


def get_scatter_data(img):
    # Get plot limits
    xmax = img.shape[0]
    ymax = img.shape[1]
    
    # Convert img data to list of scatterplot coordinates
    X = []
    for i in range(xmax):
        for j in range(ymax):
            if img[i,j] == 0:
                X.append([i,j])
    return X


def plot_map(img, path=[]):
    # Get plot limits
    xmax = img.shape[0]
    ymax = img.shape[1]

    # Get and format data for scatterplot
    X = np.transpose(get_scatter_data(img))
    path = np.transpose(path)

    # Plot map and path data as scatterplots
    plt.figure()
    plt.xlim([0,xmax])
    plt.ylim([ymax,0])
    plt.scatter(X[0], X[1], zorder=1)
    plt.scatter(path[0], path[1], zorder=2)
    plt.show()