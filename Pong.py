## Pong ##
import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [WIDTH/2, HEIGHT/2]
ball_vel = [3, -2]
paddle1_pos = [HEIGHT/2 - HALF_PAD_HEIGHT, HEIGHT/2 + HALF_PAD_HEIGHT]
paddle2_pos = [HEIGHT/2 - HALF_PAD_HEIGHT, HEIGHT/2 + HALF_PAD_HEIGHT]
paddle1_vel = 0
paddle2_vel = 0
score1 = 0
score2 = 0
