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

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]
    if direction == "RIGHT":
        ball_vel = [random.randrange(2,4), -random.randrange(1,3)]
    elif direction == "LEFT":
        ball_vel = [-random.randrange(2,4), -random.randrange(1,3)]
        
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    spawn_ball("LEFT")
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # bounce off ball
    if ball_pos[1] >= HEIGHT - 1 - BALL_RADIUS or ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]

    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")

    # determine whether ball and gutter 'collide'
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        # determine whether paddle and ball collide    
        if ball_pos[1] >= paddle1_pos[0] and ball_pos[1] <= paddle1_pos[1]:
            ball_vel[0] = - 1.1 * ball_vel[0]
        else:
            score2 += 1
            spawn_ball("RIGHT")
    elif ball_pos[0] >= WIDTH - 1 - BALL_RADIUS - PAD_WIDTH:
        # determine whether paddle and ball collide    
        if ball_pos[1] >= paddle2_pos[0] and ball_pos[1] <= paddle2_pos[1]:
            ball_vel[0] = - 1.1 * ball_vel[0]
        else:
            score1 += 1
            spawn_ball("LEFT")

    # update paddle's vertical position, keep paddle on the screen
    if paddle2_pos[0] + paddle2_vel >= 0 and paddle2_pos[1] + paddle2_vel <= HEIGHT:
        paddle2_pos[0] += paddle2_vel
        paddle2_pos[1] += paddle2_vel
    if paddle1_pos[0] + paddle1_vel >=0 and paddle1_pos[1] + paddle1_vel <= HEIGHT:
        paddle1_pos[0] += paddle1_vel
        paddle1_pos[1] += paddle1_vel
   
    # draw paddles
    canvas.draw_line((0, paddle1_pos[0]), (0, paddle1_pos[1]), 2*PAD_WIDTH, "White")
    canvas.draw_line((WIDTH, paddle2_pos[0]), (WIDTH, paddle2_pos[1]), 2*PAD_WIDTH, "White")

    # draw scores
    canvas.draw_text(str(score1), (200,100), 50, "White")
    canvas.draw_text(str(score2), (400,100), 50, "White")

def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 3
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -3
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -3
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel	= 3
    
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel	= 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

# restart game
frame.add_button("Restart", new_game)

# start frame
new_game()
frame.start()
