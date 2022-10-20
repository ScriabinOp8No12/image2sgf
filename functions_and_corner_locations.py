import math #imports math module, which is later used for math.ceil to round pixel distance to the nearest integer

#pixel coordinates in [x, y] of 4 corners (image is 915x921 pixels)
#tl = top left, tr = top right, bl = bottom left, br = bottom right
tl_corner = [53, 56]
tr_corner = [862, 56]
bl_corner = [53, 865]
br_corner = [862, 865]

#horizontal and vertical distances between intersections are 44.94 pixels, which I'm rounding up to 45
horz_dist_intersection = math.ceil(float((tr_corner[0] - tl_corner[0]) / 18))
vert_dist_intersection = math.ceil(float((bl_corner[1] - tl_corner[1]) / 18))
hd = horz_dist_intersection #assigns variable to a shorter one so it's easier to read later
vd = vert_dist_intersection

def list_of_x_values():
    """Finds all x pixel values (horizontal) of coordinates on the Go board.
    The top left corner of the Go board is at (x=53, y=56) pixels. x is 53, and distance between
    each new x value is 45 pixels.
    """
    x_values = []
    for x in range(0,19): #range end is 19 because the board is 19 by 19. range goes 0-18 (doesn't include 19, the end point)
        x = x * hd + tl_corner[0] #makes new x value x*45*(mult by range from 0-18) + 53
        x_values.append(x)
    return x_values
all_x_values = list_of_x_values() #assigns function output to a new variable called "all_x_values"

def list_of_y_values():
    """Finds all y pixel values (vertical) of coordinates on the Go board.
    The top left corner of the Go board is at (x=53, y=56) pixels. y is 56, and distance between
    each new y value is surprisingly (not sarcastic) also 45 pixels. The board has perfect squares unlike
    real life boards!
    """
    y_values = []
    for y in range(0,19):
        y = y * vd + tl_corner[1] #makes new y value y*45*(0-18) + 56
        y_values.append(y)
    return y_values
all_y_values = list_of_y_values()

def finding_all_intersections():
    """Finds the x and y pixel coordinate of all intersections on the Go board
    using a nested for loop. This function will be used later to determine
    if there's a black stone, white stone, or no stone on the intersections"""

    all_intersections = []
    for x in all_x_values:
        for y in all_y_values:
            all_intersections.append([x,y]) #saves x,y coordinate as a list within all_intersections list (nested list)
    return all_intersections
all_coordinates = finding_all_intersections()
