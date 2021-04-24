"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
This is a breakout game.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			 # Number of attempts


def main():
    life_count = 0
    graphics = BreakoutGraphics()
    print("TotalLife:" + str(graphics.sum_bricks))

    # Add animation loop here!
    face_vx = face_vy = 1
    rate_dx = graphics.getter_dx()
    rate_dy = graphics.getter_dy()

    while life_count != NUM_LIVES:
        # Update
        graphics.ball.move(rate_dx, rate_dy)
        graphics.ball_tracker_paddle()

        # When the ball out of the window, update the number of the life.
        if graphics.dead == 1:
            life_count += 1
            graphics.dead = 0

        # Check
        graphics.ball_tracker_bricks()

        # the ball touch the bricks
        if graphics.remove_succ == 1:
            face_vy = face_vy * -1
            if graphics.ball.x <= 0 or graphics.ball.x >= graphics.window.width - graphics.ball.width:
                face_vx = face_vx * -1
            graphics.remove_succ = 0

        # The ball is not touch the bricks
        else:
            # Checking if the ball touch the right side or the left side of the window
            if graphics.ball.x <= 0 or graphics.ball.x >= graphics.window.width - graphics.ball.width:
                face_vx = face_vx * -1

            # Checking if the ball touch the paddle
            if graphics.paddle_touch == 1:
                graphics.paddle_touch = 0
                face_vy = face_vy * -1

            # Checking if the ball touch the top of the window
            elif graphics.ball.y <= 0:
                face_vy = face_vy * -1

        # Updating the rate of dx and the rate of dy speeds
        rate_dx = graphics.getter_dx() * face_vx
        rate_dy = graphics.getter_dy() * face_vy

        # Checking if the game is over
        if graphics.bricks_remove == graphics.sum_bricks:
            print("YOU WIN in breakout.py")
            break

        # Pause
        pause(FRAME_RATE)

    print("GAME OVER_checking point")




if __name__ == '__main__':
    main()
