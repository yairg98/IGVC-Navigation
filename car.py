from turtle import pos
from environment import *
from navigator import *
from animator import *
import numpy as np

class Car:

    # Car class constructor
    def __init__(self, **car_config):

        # Define default attribute values
        defaults = {
            'pos': [0,0],   # Current position of car
            'theta': 0,     # Direction car is pointing (radians from horizontal)
            'speed': 25,    # Current speed of car (m/s)
            'rad': 100,     # Radius of camera view (m)
            'lat': 0.1,     # Latency from sensing to steering actuation (s)
            'period': 1,    # Sampling and nav update period (s)
            'path_res': 1,  # Max distance between points on recorded path
            'hist': []      # Path history of the car    
        }

        # Set all attributes to default values
        for key in defaults:
            setattr(self, key, defaults[key])

        # Overwrite provided attributes from car_config
        for key in car_config:
            setattr(self, key, car_config[key])
    

    # Move car forward one step along arc
    def move_arc(self, r):
        
        # Distance car moves in a single step
        dist = self.speed * self.period

        # Break distance up into increments of length 'path_res'
        increments = np.linspace(
            0, dist, num=int(dist//self.path_res), endpoint=True)
        
        # Calculate x and y movement of car
        x0 = self.pos[0] - r*np.cos(self.theta - np.pi/2)
        y0 = self.pos[0] - r*np.sin(self.theta - np.pi/2)
        print(f"{x0},{y0}")
        for d in increments:
            theta = d/r - np.pi/2
            x = x0 + r*np.cos(self.theta + theta)
            y = y0 + r*np.sin(self.theta + theta)

            # Update pos and hist
            self.hist.append(self.pos.copy())
            self.pos = [x,y]
        
        # Return new position
        return self.pos