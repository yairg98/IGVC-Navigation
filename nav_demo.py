import matplotlib.pyplot as plt
from environment import *
from navigator import *
from animator import *
from car import *


if __name__ == '__main__':

    # Image and sim setup
    filename = 'maze.jpg'
    env = Environment(filename)
    pos = [30,30]
    goal = [380,380]
    dir = [1,0]
    car = Car(pos, goal, dir)

    # Run simple_nav algorithm
    print("Starting simple_nav...")
    # nav = StraightLineNav(env, car)
    nav = SimpleNav(env, car)
    path = nav.find_path()
    # path = pathfinder(env.img, pos, dir, step_size=5)

    # Plot map and path returned by simple_nav
    # print("Starting plot_map...")
    # env.plot_map(path)

    # Plot carview_filter output
    # X = np.transpose(env.carview_filter(pos, (0,350), (0,350), 100))
    # plt.figure()
    # plt.scatter(X[0], X[1], zorder=1)
    # plt.scatter(pos[0], pos[1], zorder=2)
    # plt.show()


    anim = Animator(env,path)

    # Fullview animation test
    print("Creating fullview animation...")
    anim.fullview()

    # Moving windown animation test
    print("Creating moving window animation...")
    anim.moving_window(rad=50)

    # Carview animation test
    print("Creating carview animation...")
    anim.carview(rad=100)