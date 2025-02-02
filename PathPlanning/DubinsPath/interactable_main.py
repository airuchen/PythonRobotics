import sys
import pathlib

sys.path.append(str(pathlib.Path(__file__).parent.parent.parent))
import numpy as np
import matplotlib.pyplot as plt
import pygame
from utils.plot import plot_arrow
from dubins_path_planner import (
    plan_dubins_path,
)  # Ensure a valid Dubins path planner function is available
from practice import plot_lr_circle

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Dubins Path Interactive")

# Initial start position and heading
start_x, start_y = 1.0, 1.0
start_yaw = np.deg2rad(45.0)

# Fixed end position and heading
end_x, end_y = 0.0, 0.0
end_yaw = 0.0  # Always facing forward

boundery_x = 6
boundery_y = 6

curvature = 1.0
step_size = 0.5  # Step size for movement
curvature_step = 0.05
yaw_step = np.deg2rad(5)  # Step size for rotation


def update_plot():
    """Updates and plots the Dubins path."""
    plt.clf()
    path_x, path_y, path_yaw, mode, lengths = plan_dubins_path(
        start_x, start_y, start_yaw, end_x, end_y, end_yaw, curvature
    )

    plt.plot(path_x, path_y, label="".join(mode), linewidth=10)
    plot_lr_circle(start_x, start_y, start_yaw, 1 / curvature)
    plot_lr_circle(end_x, end_y, end_yaw, 1 / curvature)
    plot_arrow(start_x, start_y, start_yaw)
    plot_arrow(end_x, end_y, end_yaw)
    plt.legend()
    plt.grid(True)
    plt.axis("equal")
    plt.xlim(-boundery_x-1, boundery_x+1)
    plt.ylim(-boundery_y-1, boundery_y+1)
    # plt.draw()
    plt.pause(0.02)


# Initialize Matplotlib figure
plt.ion()  # Interactive mode
plt.figure()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:  # Press ESC to exit
        running = False
    if keys[pygame.K_k]:  # Move up
        start_y += step_size
    if keys[pygame.K_j]:  # Move down
        start_y -= step_size
    if keys[pygame.K_h]:  # Move left
        start_x -= step_size
    if keys[pygame.K_l]:  # Move right
        start_x += step_size
    if keys[pygame.K_q]:  # Rotate counterclockwise
        start_yaw += yaw_step
    if keys[pygame.K_e]:  # Rotate clockwise
        start_yaw -= yaw_step
    if keys[pygame.K_y]:  # Rotate counterclockwise
        curvature += curvature_step
    if keys[pygame.K_u]:  # Rotate clockwise
        curvature -= curvature_step

    if abs(start_x) > boundery_x:
        start_x = -boundery_x if start_x > 0 else boundery_x
    if abs(start_y) > boundery_y:
        start_y = -boundery_y if start_y > 0 else boundery_y

    update_plot()  # Update visualization

pygame.quit()
# plt.ioff()
# plt.show()
plt.close()  # Close the plot window
