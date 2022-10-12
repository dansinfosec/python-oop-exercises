# pygame demo 0 - window only
# 1 - Import packages
import pygame
from pygame.locals import *
import sys

# 2 - Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Load assets: image(s), sound(s), etc.

# 5 - Initialize variables

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end the program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # 8 - Do any "per frame" actions
        # In this part we eventually check for let's say colliding elements
        # any code you want to run in the frame

        # 9 - Clear the window
        # On each iteration through the loop, our program must redraw everything
        # We can use a background image or whatever but we use a black background for now
        window.fill(BLACK)

        # 10 - Draw all window elements
        # Here we will place code to draw everything we want to show in our window
        # In real programs things are drawn in the order they appear in the code,
        # in layers from backmost to frontmost Natural mapping equivalent to Photoshop

        # 11 - Update the window
        # This line tells pygame to take all the drawing we've included and show it in the window.
        # When you tell pygame to update it takes the contents of this off-screen buffer created in 8,9
        # And puts them in the real window

        pygame.display.update()

        # 12 - Slow things down a bit
        # Computers are very fast, and if the loop continnued to the next iteration right away without pausing
        # the program might run faster than the desired framerate
        # The line in this section tellls pygame to wait untill a given amount of time has elapsed
        # in order to make the frames of our program run at the framerate we specified
        # This is important to ensure our program runs at a consistent rate,
        # independent of the speed of the computer on which it's running

        clock.tick(FRAMES_PER_SECOND)
