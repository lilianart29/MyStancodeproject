"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10      # Number of rows of bricks
BRICK_COLS = 10      # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)
        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'Black'
        self.window.add(self.paddle, x=(self.window_width-self.paddle.width)/2, y=self.window_height-paddle_offset)
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, x= self.window_width/2-ball_radius, y=self.window_height/2-ball_radius)
        # Initialize our mouse listeners
        onmousemoved(self.paddle_move)
        self.switch = False
        onmouseclicked(self.start)
        # Draw bricks#
        self.brick_cols = BRICK_COLS
        self.brick_rows = BRICK_ROWS
        for i in range(self.brick_cols):
            for m in range(self.brick_rows):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                if m <2:
                    self.brick.fill_color = "red"
                    self.window.add(self.brick, x=0 + i * (brick_width + brick_spacing),
                                    y=brick_offset + m * (brick_height + brick_spacing))
                elif 2 <= m <4:
                    self.brick.fill_color = "orange"
                    self.window.add(self.brick, x=0 + i * (brick_width + brick_spacing),
                                    y=brick_offset + m * (brick_height + brick_spacing))
                elif 3< m <= 5 :
                    self.brick.fill_color = "yellow"
                    self.window.add(self.brick, x=0+i*(brick_width+brick_spacing), y=brick_offset+m*(brick_height+brick_spacing))
                elif 5< m <= 7 :
                    self.brick.fill_color = "green"
                    self.window.add(self.brick, x=0 + i * (brick_width + brick_spacing),
                                    y=brick_offset + m * (brick_height + brick_spacing))
                elif 7< m <= 9:
                    self.brick.fill_color = "blue"
                    self.window.add(self.brick, x=0 + i * (brick_width + brick_spacing),
                                    y=brick_offset + m * (brick_height + brick_spacing))
                elif m > 9:
                    self.brick.fill_color = "pink"
                    self.window.add(self.brick, x=0 + i * (brick_width + brick_spacing),
                                    y=brick_offset + m * (brick_height + brick_spacing))
        # self.hp = GLabel('HP=',x=0,y=50)
        # self.hp.font = '-40'
        # self.window.add(self.hp)

    def paddle_move(self, mouse, paddle_offset= PADDLE_OFFSET , paddle_width= PADDLE_WIDTH):
        if mouse.x+paddle_width/2 >= self.window_width:
            self.paddle.x = self.window_width-paddle_width
            self.paddle.y = self.window_height-paddle_offset
        elif mouse.x-paddle_width/2 <= 0:
            self.paddle.x = 0
            self.paddle.y = self.window_height-paddle_offset
        else:
            self.paddle.x = mouse.x-paddle_width/2
            self.paddle.y = self.window_height-paddle_offset

    # Default initial velocity for the ball
    @staticmethod
    def get__dx():
        return random.randint(1, MAX_X_SPEED)

    @staticmethod
    def get__dy():
        return INITIAL_Y_SPEED

    def start(self, a):
        self.switch = True

    def ball_move(self, __dx, __dy):
        if self.ball.x == self.window_width / 2 - self.ball.width and self.ball.y == self.window_height / 2 - self.ball.width:
            if (random.random() > 0.5):
                __dx = -__dx
        self.ball.x = self.ball.x + __dx
        self.ball.y += __dy









