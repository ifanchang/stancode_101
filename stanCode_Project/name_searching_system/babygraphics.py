"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
# YEARS = [1900,1960,1970,1980]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    data_num = len(YEARS)
    space = (width - GRAPH_MARGIN_SIZE - GRAPH_MARGIN_SIZE) / data_num
    if YEARS.index(year_index) != 0:
        return YEARS.index(year_index) * space + GRAPH_MARGIN_SIZE
    else:
        return GRAPH_MARGIN_SIZE


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################

    # Lower horizontal line
    canvas.create_line(GRAPH_MARGIN_SIZE,CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                      CANVAS_WIDTH-GRAPH_MARGIN_SIZE,CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)

    # Upper horizontal line
    canvas.create_line(GRAPH_MARGIN_SIZE,GRAPH_MARGIN_SIZE,
                      CANVAS_WIDTH-GRAPH_MARGIN_SIZE,GRAPH_MARGIN_SIZE)

    # Vertical line and Add word
    for year in YEARS:
        x_coordinate = get_x_coordinate(CANVAS_WIDTH, year)
        canvas.create_text(x_coordinate, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=year, anchor=tkinter.NW)
        canvas.create_line(x_coordinate, 0, x_coordinate, CANVAS_HEIGHT)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################
    rank_space = float(((CANVAS_HEIGHT - GRAPH_MARGIN_SIZE) - GRAPH_MARGIN_SIZE) / 1000)
    name_num = 0
    for name in lookup_names:
        if name in name_data:
            name_year_rank_first = [0, 0]
            name_year_rank_second = [0, 0]
            for year in YEARS:
                year = str(year)
                if year in name_data[name]:
                    rank = name_data[name][year]
                    x_coordinate = get_x_coordinate(CANVAS_WIDTH, int(year))
                    print_word = name + " " + str(rank)

                    # Add one data information on the canvas
                    canvas.create_text(x_coordinate+TEXT_DX, GRAPH_MARGIN_SIZE + ((int(rank) - 1) * rank_space),
                                       text=print_word, anchor=tkinter.SW, fill=COLORS[name_num % len(COLORS)])

                    # Draw a short line of the data on the canvas
                    if name_year_rank_first[0] == 0:
                        name_year_rank_first = [x_coordinate, GRAPH_MARGIN_SIZE + ((int(rank) - 1) * rank_space)]
                    else:
                        name_year_rank_second = [x_coordinate, GRAPH_MARGIN_SIZE + ((int(rank) - 1) * rank_space)]
                        draw_the_baby_line(canvas, name_year_rank_first, name_year_rank_second, name_num % len(COLORS))
                        name_year_rank_first = name_year_rank_second

                else:
                    x_coordinate = get_x_coordinate(CANVAS_WIDTH, int(year))
                    print_word = name + " " + "*"
                    canvas.create_text(x_coordinate, GRAPH_MARGIN_SIZE + ((int(1000) - 1) * rank_space), text=print_word,
                                       anchor=tkinter.SW, fill=COLORS[name_num % len(COLORS)])
                    # Draw a short line of the data on the canvas
                    if name_year_rank_first[0] == 0:
                        name_year_rank_first = [x_coordinate, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE]
                    else:
                        name_year_rank_second = [x_coordinate, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE]
                        draw_the_baby_line(canvas, name_year_rank_first, name_year_rank_second, name_num % len(COLORS))
                        name_year_rank_first = name_year_rank_second

        name_num += 1


def draw_the_baby_line(canvas, first, second, name_color_num):
    """
    The function will draw a short line of the data on the canvas
    :param canvas: (Tkinter Canvas)The canvas on which we are drawing.
    :param first: list, the first point of the line
    :param second: list, the second point of the line
    :param name_color_num: int, the color number of the line
    :return: N/A
    """
    canvas.create_line(first[0], first[1], second[0], second[1],
                       fill=COLORS[name_color_num], width=LINE_WIDTH)


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
