"""
File: my_drawing.py
Name: CHANG, I FAN
----------------------
The world
"""

from campy.graphics.gobjects import GOval, GRect, GLine, GLabel
from campy.graphics.gwindow import GWindow
window = GWindow(width=600, height=400)

def main():
    """
    The follow code will show you a world in a window,
    which is width=600, and height=400
    """
    sunoval()
    ground_and_tree()
    building_and_window()
    couldsOval(180,0)
    couldsOval(180,60)


def sunoval():
    """
    The following code print out a sun
    """
    sun = GOval(100,100,x=20,y=40)
    sunlight_1 = GRect(20,40,x=50,y=0)
    sunlight_2 = GRect(20,40,x=73,y=0)
    sunlight_3 = GRect(20,40,x=50,y=140)
    sunlight_4 = GRect(20,40,x=73,y=140)
    sunlight_5 = GRect(40,20,x=120,y=70)
    sunlight_6 = GRect(40,20,x=120,y=93)
    sunlight_7 = GRect(40,20,x=0,y=70)
    sunlight_8 = GRect(40,20,x=0,y=93)

    printout = [sun,sunlight_1,sunlight_2,sunlight_3,sunlight_4,sunlight_5,
                sunlight_6,sunlight_7,sunlight_8]
    for sunprint in printout:
        sunprint.filled = True
        sunprint.fill_color = sunprint.color = "Yellow"
        window.add(sunprint)


def ground_and_tree():
    """
    The following code print out a ground and a tree
    """
    ground = GRect(600,40,x=0,y=360)
    tree_trunk = GRect(40,80,x=100,y=280)
    tree_top = GOval (80,60,x=80,y=220)
    tree_trunk2 = GRect(40, 80, x=200, y=280)
    tree_top2 = GOval(80, 60, x=180, y=220)
    tree_trunk3 = GRect(40, 80, x=300, y=280)
    tree_top3 = GOval(80, 60, x=280, y=220)

    ground.filled = tree_trunk.filled = tree_top.filled = \
        tree_trunk2.filled = tree_top2.filled = tree_trunk3.filled = tree_top3.filled = True
    ground.color = ground.fill_color = "Green"
    tree_trunk.color = tree_trunk.fill_color = tree_trunk2.color = tree_trunk2.fill_color =\
        tree_trunk3.color = tree_trunk3.fill_color = "Brown"
    tree_top.color = tree_top.fill_color = tree_top2.color = tree_top2.fill_color = \
        tree_top3.color = tree_top3.fill_color = "Green"

    printout = [ground, tree_trunk,tree_top,tree_trunk2,tree_top2,tree_trunk3,tree_top3]
    for groundprint in printout:
        window.add(groundprint)



def building_and_window():
    """
    The following code print out a building
    """
    building_outside = GRect(150, 200, x=440, y=160)
    building_window1 = GRect(30, 30, x=465, y=180)
    building_window2 = GRect(30, 30, x=500, y=180)
    building_window3 = GRect(30, 30, x=535, y=180)
    building_window4 = GRect(30, 30, x=465, y=220)
    building_window5 = GRect(30, 30, x=500, y=220)
    building_window6 = GRect(30, 30, x=535, y=220)
    building_window7 = GRect(30, 30, x=465, y=260)
    building_window8 = GRect(30, 30, x=500, y=260)
    building_window9 = GRect(30, 30, x=535, y=260)
    building_door = GRect(40, 60, x=495, y=300)

    building_outside.filled = building_window1.filled = building_window2.filled = \
        building_window3.filled = building_window4.filled = building_window5.filled = \
        building_window6.filled = building_window7.filled = building_window8.filled = \
        building_window9.filled = building_door.filled = True
    building_outside.color = building_outside.fill_color = "Gray"
    building_window1.color = building_window1.fill_color = \
        building_window2.color = building_window2.fill_color = \
        building_window3.color = building_window3.fill_color = \
        building_window4.color = building_window4.fill_color = \
        building_window5.color = building_window5.fill_color = \
        building_window6.color = building_window6.fill_color = \
        building_window7.color = building_window7.fill_color = \
        building_window8.color = building_window8.fill_color = \
        building_window9.color = building_window9.fill_color = "Red"
    building_door.color = building_door.fill_color = "Black"

    printout = [building_outside,building_window1,building_window2,building_window3,
                building_window4,building_window5,building_window6,building_window7,
                building_window8,building_window9,building_door]
    for buildingprint in printout:
        window.add(buildingprint)


def couldsOval(position_x,position_y):
    """
    The following code print out some cloud
    """
    for i in range(position_x,window.width,100):
        clouds = GOval(50,30,x=i,y=position_y+10)
        window.add(clouds)
        clouds.filled = True
        clouds.color = "Blue"
        clouds.fill_color = "Blue"
    for j in range(position_x+25,window.width,100):
        clouds = GOval(40,30,x=j,y=position_y)
        window.add(clouds)
        clouds.filled = True
        clouds.color = "Blue"
        clouds.fill_color = "Blue"
    for k in range(position_x+25,window.width,100):
        clouds = GOval(40,30,x=k,y=position_y+20)
        window.add(clouds)
        clouds.filled = True
        clouds.color = "Blue"
        clouds.fill_color = "Blue"
    for l in range(position_x-25,window.width,100):
        clouds = GOval(40,30,x=l,y=position_y)
        window.add(clouds)
        clouds.filled = True
        clouds.color = "Blue"
        clouds.fill_color = "Blue"
    for m in range(position_x-25,window.width,100):
        clouds = GOval(40,30,x=m,y=position_y+20)
        window.add(clouds)
        clouds.filled = True
        clouds.color = "Blue"
        clouds.fill_color = "Blue"

if __name__ == '__main__':
    main()
