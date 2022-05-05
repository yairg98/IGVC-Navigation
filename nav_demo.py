import matplotlib.pyplot as plt
from environment import *
from navigator import *
from animator import *
from car import *
import time


if __name__ == '__main__':

    # Initialize environment from image
    filename = 'images/s_curve.jpeg'
    env = Environment(filename)

    # Configure car
    car_config = {
        'pos': [50,50],
        'dir': [1,0]
    }

    # Initialize car
    car = Car(**car_config)

    car.move_arc(r=10)
    plt.figure()
    plt.plot(np.transpose(car.hist))
    plt.show()

    # Uncomment one nav algorithm line below:
    # nav = StraightLineNav(env, car)
    # nav = KnnNav(env, car, step=25)

    # # Run nav algorithm
    # print("Running nav algorithm...")
    # path = nav.find_path()

    # Plot map and carview
    # print("Plotting map and carview...")
    # env.plot_map(path)
    # env.plot_carview(pos, (0,350), (0,350), 100)

    # # Instantiate animator
    # anim = Animator(env,path)

    # # Fullview animation test
    # print("Creating fullview animation...")
    # anim.fullview()

    # # Moving windown animation test
    # print("Creating moving window animation...")
    # anim.moving_window(rad=100)

    # # Carview animation test
    # print("Creating carview animation...")
    # anim.carview(rad=100)