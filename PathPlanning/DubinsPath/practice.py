import sys
import pathlib

sys.path.append(str(pathlib.Path(__file__).parent.parent.parent))

from math import sin, cos, atan2, sqrt, acos, pi, hypot
from utils.angle import angle_mod, rot_mat_2d
import matplotlib.pyplot as plt
import numpy as np


class Pose:
    def __init__(self, x, y, theta):
        self.x = x
        self.y = y
        self.theta = theta

def create_circle_pose(x, y, yaw, min_turning_radius, offset_angle):
    return Pose(
        x + min_turning_radius * cos(yaw + offset_angle),
        y + min_turning_radius * sin(yaw + offset_angle),
        yaw
    )

def plot_circle(pose, radius, color="gray"):
    circle = plt.Circle((pose.x, pose.y), radius, color=color, fill=False)
    ax = plt.gca()
    ax.add_patch(circle)

def plot_lr_circle(x, y, yaw, min_turning_radius):
    right_circle_pose = create_circle_pose(x, y, yaw, min_turning_radius, pi / 2)
    left_circle_pose = create_circle_pose(x, y, yaw, min_turning_radius, -pi / 2)

    plot_circle(right_circle_pose, min_turning_radius)
    plot_circle(left_circle_pose, min_turning_radius)