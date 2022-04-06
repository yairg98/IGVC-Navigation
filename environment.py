from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

class Environment:

    def __init__(self, filename, threshold=200):
        
        # Import, rotate, and format the envirinment map image
        self.img = np.asarray(
            Image.open(filename)\
                .transpose(Image.ROTATE_270)\
                .convert("L")
        )
        # Binarize the image
        self.img = (self.img > threshold) * 255
        print(self.img.shape)


    # Return image as array or binary pixels
    def get_image(self):
        return self.img


    # Convert img object into a list of points for a scatterplot
    def as_scatterplot(self, xlim=None, ylim=None):
        
        img = self.img
        
        # Get plot limits
        if xlim == None:
            xrange = range(0,img.shape[0])
        else:
            x1 = max(0, xlim[0])
            x2 = min(img.shape[0], xlim[1])
            xrange = range(x1, x2)
        if ylim == None:
            yrange = range(0,img.shape[0])
        else:
            y1 = max(0, ylim[0])
            y2 = min(img.shape[1], ylim[1])
            yrange = range(y1, y2)

        print(xrange)
        print(yrange)

        # Convert img data to list of scatterplot coordinates
        X = []
        for i in xrange:
            for j in yrange:
                if img[i,j] == 0:
                    X.append([i,j])
        return X


    # Plot the input map as a scatterplot
    def plot_map(self, path=[], xlim=None, ylim=None):

        img = self.img

        # Get plot limits
        xlim = [0, img.shape[0]] if xlim==None else xlim
        ylim = [0, img.shape[1]] if ylim==None else ylim

        # Get and format data for scatterplot
        X = np.transpose(self.as_scatterplot(xlim, ylim))
        path = np.transpose(path)

        # Plot map and path data as scatterplots
        plt.figure()
        plt.xlim(xlim)
        plt.ylim(ylim)
        plt.scatter(X[0], X[1], zorder=1, s=1)
        plt.scatter(path[0], path[1], zorder=2,s=1)
        plt.savefig("fullview.png")


    # Return list of bins corresponding to angles obstructed by given point
    def find_angle_bins(self, bins, dx, dy, ds, p_rad):

        # Find range of obstructed angles
        dx += (1e-16 if dx==0 else 0) # Avoid division by zero
        theta = np.arctan2(dy, dx)
        theta1 = theta - p_rad/ds
        theta2 = theta + p_rad/ds

        # Find index of closest angle to each end of theta range
        arr = np.abs(np.asarray([bins-theta1, bins-theta2]))
        inds = np.argmin(arr, axis=1)

        # Return all bins in range
        return bins[inds[0] : inds[1]]


    # Apply filter to return only part of map visible to the car
    def lidar_filter(self, pos, xlim=None, ylim=None, resolution=100, p_rad=1):

        # Get list of points
        X = self.as_scatterplot(xlim, ylim)

        # Create bins for each arc the snesor detects
        arcs = np.linspace(-np.pi, np.pi, resolution)
        bins = dict.fromkeys(arcs)

        # Save only the closest point to the car within each arc
        for p in X:

            # Get dx, dy, and ds
            dx = p[0] - pos[0]
            dy = p[1] - pos[1]
            ds = np.sqrt(dx**2 + dy**2)
            
            # Identify correct bin
            blocked_bins = self.find_angle_bins(arcs, dy, dx, ds, p_rad)
            
            # Add p to each necessary bin
            for b in blocked_bins:
                if bins[b] == None or ds < bins[b][1]:
                    bins[b] = [p, ds]

            # Return new data:
            X = []
            for b in bins:
                if bins[b] != None:
                    X.append(bins[b][0])
    
        return X


    # Plot carview of map
    def plot_carview(self,pos,xlim=None,ylim=None,resolution=100,p_rad=1):
        X = np.transpose(self.lidar_filter(pos,xlim,ylim,resolution,p_rad))
        plt.figure()
        plt.scatter(X[0], X[1], zorder=1)
        plt.scatter(pos[0], pos[1], zorder=2)
        plt.xlim(np.min(X), np.max(X))
        plt.ylim(np.min(X), np.max(X))
        plt.savefig("carview.png")