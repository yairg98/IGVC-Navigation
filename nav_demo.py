import matplotlib.pyplot as plt
from nav_imaging import *
from nav_algorithms import *
from nav_animations import *


if __name__ == '__main__':

    # Name of maze JPEG file    
    filename = 'maze.jpg'

    # Turn image into binarized 2D array
    img = get_image(filename)

    # Run simple_nav algorithm
    path = simple_nav(img, [30, 30])

    # Plot map and path returned by simple_nav
    # plot_map(img, path)

    # Plot carview_filter output
    X = np.transpose(carview_filter(img, [75,75], (50,100), (50,100), 1000))

    plt.figure()
    plt.scatter(X[0], X[1], zorder=1)
    plt.show()

    # Fullview animation test
    # fullview_animation(img, path)

    # Carview animation test
    # moving_window_animation(img, path, rad=50)