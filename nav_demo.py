import matplotlib.pyplot as plt
import time
from nav_imaging import *
from nav_algorithms import *
from nav_animations import *


if __name__ == '__main__':

    # Image and sim setup
    filename = 'maze.jpg'
    img = get_image(filename)
    pos = [30,30]

    # Run simple_nav algorithm
    path = simple_nav(img, pos)

    # Plot map and path returned by simple_nav
    # plot_map(img, path)

    # Plot carview_filter output
    X = np.transpose(carview_filter(img, pos, (0,350), (0,350), 1000))
    plt.figure()
    plt.scatter(X[0], X[1], zorder=1)
    plt.scatter(pos[0], pos[1], zorder=2)
    plt.show()

    # Fullview animation test
    # fullview_animation(img, path)

    # Carview animation test
    # moving_window_animation(img, path, rad=50)