"""
File: 
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

window = GWindow(600, 400)  # Creating a window
point_1 = 0  # The global variable record the position about the first point.
point_2 = 0  # The global variable record the position about the second point.
switch = 0  # The global variable will determine if this is the first or the second point.


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    global switch
    onmouseclicked(position_1)


def position_1(mouse):
    """
    The function will draw a line.
    :param mouse: The position where the mouse is
    :return: NA
    """
    global point_1, point_2, switch
    point = GOval(10, 10, x=mouse.x-5, y=mouse.y-5)
    point.filled = True
    window.add(point)
    if switch == 0:
        point_1 = point
        switch = 1
    else:
        point_2 = point
        line = GLine(point_1.x, point_1.y, point_2.x, point_2.y)
        window.add(line)
        window.remove(point_1)
        window.remove(point_2)
        switch = 0


if __name__ == "__main__":
    main()
