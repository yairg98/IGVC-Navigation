from environment import *
from navigator import *
from animator import *
import numpy as np

class Car:

    # Car class constructor
    def __init__(self, **car_config):

        # Define default attribute values
        defaults = {
            'pos': [0,0],       # Current position of car
            'dir': [1,0],       # Direction car is pointing
            'speed': 10,        # Current speed of car (m/s)
            'rad': 100,         # Radius of camera view (m)
            'lat': 0.1,         # Latency from sensing to steering actuation (s)
            'period': 1,        # Sampling and nav update period (s)
            'hist': []          # Path history of the car    
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
        
        # Calculate x and y movement of car
        theta = dist/r
        dx = r*np.cos(theta)
        dy = r*np.sin(theta)

        # Update pos and hist
        self.hist.append(self.pos.copy())
        self.pos = np.add(self.pos, [dx,dy])
        
        # Return new position
        return self.pos