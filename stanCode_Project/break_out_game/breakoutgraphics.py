"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle_touch = 0  # (0:untouch paddle; 1: touch paddle)

        # self.paddle = GRect(paddle_width, paddle_height)
        self.paddle = GRect(paddle_width, paddle_height)  # Test width "430"
        self.paddle.filled = True
        self.window.add(self.paddle, x=(window_width-paddle_width)/2, y=window_height-paddle_offset)

        # Center a filled ball in the graphical window
        self.ball_radius = ball_radius
        self.remove_succ = 0  # (0: untouch bricks; 1: touch bricks)
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, x=(window_width-ball_radius)/2, y=(window_height-ball_radius)/2)

        # Default initial velocity for the ball
        self.__dy = INITIAL_Y_SPEED
        self.__dx = random.randint(1, MAX_X_SPEED+1)
        if random.random() > 0.5:
            self.__dx = -self.__dx

        # Initialize our mouse listeners
        self.switch = 0  # This variable controls if the game start or not. (1:start, 0: unstart)
        onmouseclicked(self.click_m)
        onmousemoved(self.move_m)

        # Draw bricks
        self.sum_bricks = brick_rows * brick_cols
        self.bricks_remove = 0  # record how many bricks were removed
        brick_spacing = (window_width - (brick_width*brick_rows))/(brick_rows-1)
        position_height = brick_offset
        for i in range(brick_cols):
            position_width = 0
            for j in range(brick_rows):
                bricks = GRect(brick_width, brick_height)
                bricks.filled = True
                self.window.add(bricks, x=position_width, y=position_height)
                position_width += (brick_spacing + brick_width)
            position_height += (brick_spacing + brick_height)

        # The following variables are used to control user's life or die
        self.dead = 0  # (0: still life; 1: die)

    def click_m(self, mouse):
        """
         This method process when the mouse click.
         :param mouse: shows where the place of mouse
         :return: NA
        """
        if self.switch == 0:
            self.switch = 1
        else:
            pass

    def move_m(self,mouse):
        """
        This method will track where the mouse, and the paddle will follow the mouse
        :param mouse: shows where the place of the mouse
        :return: NA
        """
        if mouse.x >= self.paddle.width/2 and mouse.x <= self.window.width-(self.paddle.width/2):
            self.paddle.x = mouse.x - self.paddle.width/2

    def getter_dx(self):
        """
        The method will give the class user the variable, self.__dx.
        :return: if the game is processing, return the speed of x
        :return: if the game is stop, the speed of x is 0.
        """
        if self.switch == 1:
            return self.__dx
        return 0

    def getter_dy(self):
        """
        The method will give the class user the variable, self.__dy.
        :return: if the game is processing, return the speed of y
        :return: if the game is stop, the speed of y is 0.
        """
        if self.switch == 1:
            return self.__dy
        return 0

    def ball_tracker_bricks(self):
        """
        This method is charge of the following situation.
        1. When the ball touch the bricks.
        2. When the ball remove all the bricks.
        :return: if the situation is true, removing the ball.
        """
        ball_tracker_x = [self.ball.x, self.ball.x+2*self.ball_radius]
        ball_tracker_y = [self.ball.y, self.ball.y+2*self.ball_radius]

        for x in ball_tracker_x:
            for y in ball_tracker_y:
                ball_may = self.window.get_object_at(x=x, y=y)
                if ball_may is not self.paddle:
                    if ball_may is not None:
                        self.remove_succ = 1

                        # When the ball remove the bricks, adding one to the recorder
                        # The the brick remove recoder == the number of all bricks → stop the game
                        self.bricks_remove += 1
                        print(str(self.bricks_remove))
                        if self.bricks_remove == self.sum_bricks:
                            self.window.remove(self.ball)
                            # reset the ball on the middle of the window
                            self.window.add(self.ball, x=(self.window.width - self.ball.width) / 2,
                                            y=(self.window.height - self.ball.height) / 2)
                            print('YOU WIN in breakoutgraphics.py')

                        return self.window.remove(ball_may)

    def ball_tracker_paddle(self):
        """
        This method is charge of the following situation.
        1. When the ball touch paddle.
        2. When the ball below the bottom of the window.
        :return: NA
        """
        ball_tracker_x = [self.ball.x, self.ball.x+2*self.ball_radius]
        ball_tracker_y = [self.ball.y, self.ball.y+2*self.ball_radius]

        # When the ball touch the paddle.
        for x in ball_tracker_x:
            for y in ball_tracker_y:
                paddle_may = self.window.get_object_at(x=x, y=y)
                if paddle_may is self.paddle:
                    self.paddle_touch = 1

                    """
                    這行是時為了解決反彈的時候球黏在板子上，研判原因應該是板子快速的滑入，導致球的偵測點卡在板子上下。
                    我強制球碰到板子後會先跳到板子以上，才開始走反彈的code。
                    請問有什麼其他方法可以解決球的偵測點卡在板子上的問題??因為我強制讓球跳到板子以上，看起來會微微奇怪。
                    """
                    self.ball.y = self.paddle.y-self.ball.height
                    return

        # Checking if the ball below the bottom of the window
        if self.ball.y > self.window.height:
            self.dead = 1
            self.switch = 0  # restart the mouse click function
            self.window.remove(self.ball)

            # reset the ball on the middle of the window
            self.window.add(self.ball, x=(self.window.width - self.ball.width) / 2,
                            y=(self.window.height - self.ball.height) / 2)

