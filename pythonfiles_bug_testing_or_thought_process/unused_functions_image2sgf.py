def diagonal_x_value_stone_checker():
    """FUNCTION NOT NEEDED/USED!
    Adds 12 pixels to each x value of the intersection. This shifted x value
    combined with the shifted y value allow us to check if there's a black, white, or no stone
    on the intersection"""
    new_x_values = []
    for x in all_x_values:
        x+=12
        new_x_values.append(x)
    return new_x_values
x_stone_checker = diagonal_x_value_stone_checker()

def diagonal_y_value_stone_checker():
    """FUNCTION NOT NEEDED/USED!"""
    new_y_values = []
    for y in all_y_values:
        y+=12
        new_y_values.append(y)
    return new_y_values
y_stone_checker = diagonal_y_value_stone_checker()

def new_coordinates_for_stone_checking():
    """FUNCTION NOT NEEDED/USED!
    This is the new shifted coordinates, where we can test to see if there's a stone on the intersection.
    We went 12 pixels to the right and 12 pixels down from the intersection because there is
    always either a black color, white color, or brown-ish color (board color) at this diagonal point
    from the intersection. Note that Go stones are placed precisely on the intersection, meaning part of the stone
    hangs out between the intersections. Stones have a ~15 pixel radius, so going 12 pixels
    diagonally out from the center helps us avoid identifying the black color
    as a letter or symbol instead of a stone."""
    new_coordinates = []
    for x in x_stone_checker:
        for y in y_stone_checker:
            new_coordinates.append([x,y])
    return new_coordinates
coordinates_for_stone_check = new_coordinates_for_stone_checking()
