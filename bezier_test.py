import bezier
from bezier.hazmat.curve_helpers import get_curvature, evaluate_hodograph
import numpy as np
import matplotlib.pyplot as plt

# Define path
path = [[50, 50], [50, 75], [75, 75], [100, 75], [125, 75], [150, 75], [175, 75], [200, 75], [200, 100], [200, 125], [225, 125], [225, 150], [225, 175], [225, 200], [225, 225], [225, 250], [225, 275], [225, 300], [225, 325], [250, 325], [250, 350], [275, 350], [300, 350], [325, 350], [350, 350], [375, 350], [375, 325], [375, 300], [375, 275], [375, 250], [375, 225], [375, 200], [375, 175], [375, 150], [375, 125], [375, 100], [375, 75], [400, 75], [425, 75], [425, 50], [450, 50], [475, 50], [500, 50], [525, 50], [525, 75], [550, 75], [550, 100], [575, 100], [575, 125], [575, 150], [575, 175], [575, 200], [600, 200], [600, 225], [600, 250], [600, 275], [600, 300], [600, 325], [600, 350], [600, 375], [600, 400], [575, 400], [575, 425], [575, 450], [550, 450], [525, 450], [525, 475], [500, 475], [475, 475], [450, 475], [425, 475], [400, 475], [375, 475], [350, 475], [325, 475], [300, 475], [275, 475], [250, 475], [225, 475], [200, 475], [175, 475], [175, 500], [150, 500], [150, 525], [150, 550], [175, 550], [175, 575], [200, 575], [225, 575], [250, 575], [275, 575], [300, 575], [325, 575], [350, 575], [375, 575], [400, 575], [425, 575], [450, 575], [475, 575], [500, 575], [525, 575], [550, 575], [575, 575], [600, 575], [625, 575], [650, 575], [675, 575], [700, 575], [725, 575], [750, 575], [750, 550], [775, 550], [800, 550], [800, 525], [775, 525], [775, 500], [800, 500], [800, 475], [775, 475], [775, 450], [775, 425], [775, 400], [775, 375], [775, 350], [775, 325], [775, 300], [775, 275], [775, 250], [775, 225], [800, 225], [825, 225], [850, 225], [875, 225], [900, 225]]
path = path[:58]
path = np.transpose(path)

path[0] = np.multiply(path[0],1.5)

# Create curve
curve3 = bezier.Curve.from_nodes(path)

# Plot path and curve
fig, ax = plt.subplots(figsize=(12,9))
ax.set_aspect(1)
ax.set_xlim(15,950)
ax.set_ylim(15,380)
ax.scatter(path[0],path[1])
curve3.plot(num_pts=1000, ax=ax, color='r')

# Calculate curvature
S = [0.02, 0.2, 0.45, .6, .9]
T = [curve3.evaluate_hodograph(s) for s in S]
K = [get_curvature(curve3.nodes,T[i],S[i]) for i in range(len(S))]

# Position of each point
P = np.squeeze([curve3.evaluate(s) for s in S])

# Center of circle corresponding to each point/radius
C = [t / np.sqrt(np.sum(t**2)) for t in T]
C = [[c[1],-c[0]] for c in C]

ax.scatter(P.T[0],P.T[1],color='black',zorder=5)

theta = np.linspace(0, 2*np.pi, 150)
for i in range(0,len(K)):
    r = 1/K[i]
    a = r * np.cos(theta) + P[i][0] - C[i][0]*r
    b = r * np.sin(theta) + P[i][1] - C[i][1]*r
    ax.plot(a,b,zorder=-1,linestyle='--')

plt.show()
# plt.savefig("bezier_test.jpg", dpi=200)