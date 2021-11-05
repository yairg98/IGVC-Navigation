import numpy as np
from PIL import Image, ImageDraw


# Path to roadmap image file
roadmap_jpg = 'C:/Users/yairg/OneDrive/Documents/Python Scripts/images/maze.jpg'
# Initial location of car
pos = (0, 0)
# Radius of viewing window
rad = 25


def main():
    # Open roadmap image
    im = Image.open(roadmap_jpg)
    im = binarize_image(im)


# Binarize image (convert to black and white)
def binarize_image(im, threshold=200):
    im = im.convert("L")
    im_data = np.asarray(im)
    binarized_data = (im_data > threshold) * 255
    return Image.fromarray(binarized_data)


# Start with simplest maze-solver: turn right when hitting a wall
# Then implement basic A* algorithm
# Incorporate lane-following and obstacle avoidance heuristic function