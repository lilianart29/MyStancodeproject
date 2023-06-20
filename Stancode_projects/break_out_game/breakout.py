"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    global NUM_LIVES
    n = 0  # brick count
    graphics = BreakoutGraphics()
    vx = graphics.get__dx()
    vy = graphics.get__dy()
    # Add the animation loop here!
    while True:
        if graphics.switch and NUM_LIVES > 0:
            graphics.ball_move(vx, vy)
            a = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
            b = graphics.window.get_object_at(graphics.ball.x+graphics.ball.width, graphics.ball.y)
            c = graphics.window.get_object_at(graphics.ball.x + graphics.ball.height, graphics.ball.y)
            d = graphics.window.get_object_at(graphics.ball.x + graphics.ball.height, graphics.ball.y+ graphics.ball.height)
            if graphics.ball.x <= 0:
                vx = -vx
            elif graphics.ball.x >= graphics.window_width-graphics.ball.width:
                vx = -vx
            elif graphics.ball.y <= 0:
                vy = -vy
            elif graphics.ball.y > graphics.paddle.y:
                graphics.window.remove(graphics.ball)
                NUM_LIVES = NUM_LIVES - 1
                graphics.switch = False
                graphics.ball.x = graphics.window_width / 2 - graphics.ball.width
                graphics.ball.y = graphics.window_height / 2 - graphics.ball.height
                graphics.window.add(graphics.ball)
            elif a is not None and a is not graphics.paddle:
                graphics.window.remove(a)
                vy = -vy
                n +=1
            elif b is not None and b is not graphics.paddle:
                graphics.window.remove(b)
                vy = -vy
                n += 1
            elif c is not None and c is not graphics.paddle:
                graphics.window.remove(c)
                vy = -vy
                n += 1
            elif d is not None and d is not graphics.paddle:
                graphics.window.remove(d)
                vy = -vy
                n += 1
            elif d is not None and d is graphics.paddle:
                vy = -vy
            elif c is not None and c is graphics.paddle:
                vy = -vy
        if NUM_LIVES == 0 or n == graphics.brick_rows*graphics.brick_cols:
            break
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
