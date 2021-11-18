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

    # # Plot map and path returned by simple_nav
    # plot_map(img, path)

    # Fullview animation test
    fullview_animation(img, path)
