import math
import cv2 # imports openCV which lets us read the image (detect colors -> for finding the black and white stones)
from matplotlib import image
from matplotlib import pyplot as plt
import subprocess # used later to open text file of SGF coordinates with KGS's SGF editor

# Pixel coordinates in [x, y] of 4 corners (image is 915x921 pixels) T = Top, L = Left, R = Right
TL_CORNER = [51, 54]
TR_CORNER = [703, 54]
BL_CORNER = [51, 706]
BR_CORNER = [703, 706]

# 19 by 19 board
GO_BOARD_SIZE = 19

# hd and vd = horizontal and vertical distances between intersections (36-37 pixels for both)
# got rid of math.ceil in front of the float, seems like the rounding is really messing things up
hd = float((TR_CORNER[0] - TL_CORNER[0]) / (GO_BOARD_SIZE-1))
vd = float((BL_CORNER[1] - TL_CORNER[1]) / (GO_BOARD_SIZE-1))

# used round(hd) here because location of black stones can't be a float
all_x_values = [x * round(hd) + TL_CORNER[0] for x in range(0, GO_BOARD_SIZE)]
all_y_values = [y * round(vd) + TL_CORNER[1] for y in range(0, GO_BOARD_SIZE)]
all_coordinates = [[x,y] for x in all_x_values for y in all_y_values]
print(all_coordinates)

# Right click, "copy as path", paste path below
path_to_image = r"C:\Users\nharw\Desktop\Screenshot Project\Stored Screenshots\Eric 1 2023-02-11.png"
# mode: -1 means color, 0 means gray scale, 1 means no change (including transparency value))
img = cv2.imread(path_to_image, -1)

sgf_letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s"]

# #openCV uses numpy, which means the x and y need to be swapped. In below for loop img[x,y] needs to be img[y,x]
# https://stackoverflow.com/questions/49720605/pixel-coordinates-vs-drawing-coordinates

# Below numbers are hard coded, which can be replaced by variables if necessary
# Pixel color spectrum is [0, 0, 0] to [255, 255, 255], black is 0,0,0 white is 255,255,255

# Move 7 pixels to the right and 7 pixels down to find the bottom right edge of the stone's color.
# KGS image2sgf was using 12 instead of 7
# Output is always correct, but it is also always shifted 1 stone up and to the left (diagonally off)
location_of_black_stones = [[x, y] for x, y in all_coordinates if img[y+7, x+7, 0] < 25]
location_of_white_stones = [[x, y] for x, y in all_coordinates if img[y+7, x+7, 0] > 150]

black_stones_sgf = []
white_stones_sgf = []

# Original bug: all stones would be put in a spot that's off by a diagonal location,
# for example, a stone at [2, 2] would incorrectly be thrown at [1, 1]
# by adding 1 to x = int ((x-TL_CORNER[0]/hd) to make it  x = 1 + int((x-TL_CORNER[0])/hd) everything works now!
for x, y in location_of_black_stones:
    # changed to "hd" 'vd" and TL_corner[0] / [1] instead of hard coded 45 and 36 respectively
    x = math.ceil(((x-TL_CORNER[0])/hd))  # converts x value to number between 0 and 18
    y = math.ceil(((y-TL_CORNER[1])/vd))  # values are slightly below the whole number, 0.993 or 2.935, need to round up
    # x = 1 + int((x-TL_CORNER[0])/hd)  # this and below line work, but above 2 lines should be better!
    # y = 1 + int((y-TL_CORNER[1])/vd)
    black_stones_sgf_conversion = [sgf_letters[x], sgf_letters[y]]
    black_stones_sgf.append(black_stones_sgf_conversion)

for x, y in location_of_white_stones:
    x = 1 + int((x-TL_CORNER[0])/hd)
    y = 1 + int((y-TL_CORNER[1])/vd)
    white_stones_sgf_conversion = [sgf_letters[x], sgf_letters[y]]
    white_stones_sgf.append(white_stones_sgf_conversion)

sgf_add_black = 'AB'
sgf_add_white = 'AW'

# string join + list comprehension replaces lines 60 - 63, maybe 65. "".join takes a list
bs = str(black_stones_sgf)[1:-1]  # assigns black_stones_sgf to bs and uses string slicing to remove brackets
bs = bs.replace("'", "")  # removes parenthesis from coordinates
bs = bs.replace(",", "")  # removes commas from coordinates
bs = bs.replace(" ", "")  # removes space between coordinates

final_formatted_black_stones_SGF = sgf_add_black + bs  # Adds AB ("Add Black") in front of the black stone coordinates

ws = str(white_stones_sgf)[1:-1]  # assigns white_stones_sgf to ws and uses string slicing to remove brackets
ws = ws.replace("'", "")
ws = ws.replace(",", "")
ws = ws.replace(" ", "")

final_formatted_white_stones_SGF = sgf_add_white + ws  # Adds AW ("Add White") in front of the white stone coordinates

SGF_format_start = '(;SZ[19]'  # SZ[19] means board size 19 by 19. The ( ; ) are SGF syntax
SGF_format_end = ')'

final_SGF_format = SGF_format_start + final_formatted_black_stones_SGF + final_formatted_white_stones_SGF + SGF_format_end
print(final_SGF_format)

# look up "with open python" or with "with statement"
h = open(r"C:\Users\nharw\Desktop\image2sgf project files\image2sgf image.txt", "w")
h.write(final_SGF_format)  # if this crashes, h.close won't go
h.close()

path_to_text_file = r"C:\Users\nharw\Desktop\image2sgf project files\image2sgf image.txt"
path_to_CGoban = r"C:\Program Files (x86)\cgoban\cgoban.exe"
subprocess.Popen([path_to_CGoban, path_to_text_file])  # opens text_file with CGoban (KGS's SGF editor)

# if __name__ == '__main__' --> indicates this is an executable
# singleton -> what my code does now if I import it (good if running a server / other stuff if you want it once)

