import matplotlib.pyplot as plt
from environment import *
from navigator import *
from animator import *
from car import *
import time


if __name__ == '__main__':

    # Setup
    filename = 'images/drawn_map.jpeg'
    env = Environment(filename)
    pos = [50,50]
    goal = [380,380]
    dir = [1,0]
    car = Car(pos, goal, dir)

    # Uncomment one nav algorithm line below:
    # nav = StraightLineNav(env, car)
    nav = AStarNav(env, car, step=25)

    # # Run nav algorithm
    print("Running nav algorithm...")
    path = nav.find_path()

    # Plot map and carview
    print("Plotting map and carview...")
    env.plot_map(path)
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