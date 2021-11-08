import numpy as np
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt


# Return image as array or binary pixels
def get_image(filename):
    im = Image.open(filename)
    im = binarize_image(im)
    return im


# Binarize image (convert to black and white)
def binarize_image(im, threshold=200):
    im = im.convert("L")
    im_data = np.asarray(im)
    binarized_data = (im_data > threshold) * 255
    return binarized_data


def plot_map(im, path=[]):
    # Get plot limits
    xmax = im.shape[0]
    ymax = im.shape[1]

    # Create scatter plot data from image
    X = []
    for i in range(xmax):
        for j in range(ymax):
            if im[i,j] == 0:
                X.append([i,j])
    
    X = np.transpose(X)
    path = np.transpose(path)

    # Plot map and path data as scatterplots
    plt.figure()
    plt.xlim([0,xmax])
    plt.ylim([ymax,0])
    plt.scatter(X[0], X[1], zorder=1)
    plt.scatter(path[0], path[1], zorder=2)
    plt.show()


# Navigate road using the right-hand rule
def simple_nav(im, pos):
    # Initial position and map dimensions
    pos = np.array(pos)
    dims = im.shape

    # Path followed
    X = [pos]

    # Set exit condition (reaching edge of map)
    while not np.any([
        pos[0] == 0,
        pos[0] == dims[0],
        pos[1] == 0,
        pos[1] == dims[1]]
    ):
        # TODO: add right-hand nav algorithm here
        
        # Placeholder nav algorithm (go in straight line)
        pos[0] += 1
        X.append(pos.copy())

    # Return full path
    return X


if __name__ == '__main__':
    
    filename = 'maze.jpg'
    im = get_image(filename)

    # Test simple_nav
    path = simple_nav(im, [30, 30])
    plot_map(im, path)




# Start with simplest maze-solver: keep wall on left side
# Then implement basic A* algorithm
# Incorporate lane-following and obstacle avoidance heuristic function