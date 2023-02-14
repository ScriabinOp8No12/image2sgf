# First method: Modifying the OGS_image2SGF code.

# Given there's a black stone in that location, scan the surrounding area, if there's any spot that is
# very white, then that must be the last move
# Do the same with the white stones, if there's something around it that's very black, then that's the last move

# Second method: Use an external library to detect the hollow circles

# Without using the OGSimage2sgf, use a library to scan the image, if there's a hollow circle (either white or black)
# on it, then that's the last move.  If that image has the last move, then move that image into the front of the Anki
# card. All other images where that hollow circle isn't detected are the moved onto the back of the anki cards (answers)

# For hough circles method, you can set a maximum radius.  The hollow circle will always be smaller than the size of the
# stones, so this shouldn't be too hard... right?

import math
import cv2 # imports openCV which lets us read the image (detect colors -> for finding the black and white stones)
import subprocess # used later to open text file of SGF coordinates with KGS's SGF editor

TL_CORNER = [51, 54]
TR_CORNER = [703, 54]
BL_CORNER = [51, 706]
BR_CORNER = [703, 706]

GO_BOARD_SIZE = 19

hd = float((TR_CORNER[0] - TL_CORNER[0]) / (GO_BOARD_SIZE-1))
vd = float((BL_CORNER[1] - TL_CORNER[1]) / (GO_BOARD_SIZE-1))

all_x_values = [x * round(hd) + TL_CORNER[0] for x in range(0, GO_BOARD_SIZE)]
all_y_values = [y * round(vd) + TL_CORNER[1] for y in range(0, GO_BOARD_SIZE)]
all_coordinates = [[x,y] for x in all_x_values for y in all_y_values]

for count in range(1, 51):
    path_to_image = rf"C:\Users\nharw\Desktop\Extra folder of puzzles\Eric {count} 2023-02-11.png" # CHANGED FROM STORED SCREENSHOTS FOLDER
    # r"C:\Users\nharw\Desktop\Screenshot Project\Stored Screenshots\Eric 5 2023-02-11.png"
    img = cv2.imread(path_to_image, -1)

# sgf_letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s"]

    location_of_black_stones = [[x, y] for x, y in all_coordinates if img[y+14, x+7, 0] < 25]
    location_of_white_stones = [[x, y] for x, y in all_coordinates if img[y+14, x+7, 0] > 150]
    # original working code that detected last move, but also found false last moves (numbers)
    # range (3, 12)   AND [y + num, x, 0]
    print("---------------------")
    print(f"Puzzle Number: {count}")
    for num in range(-10, 12):
        num_or_circle = [[x, y] for x, y in location_of_black_stones if img[y+num, x+num, 0] > 200]
        if num_or_circle != []:
            print(num_or_circle)
            print("Has white on black stone")
            print(f"num is: {num}")
            break

    for num in range(-10, 12):
        num_or_circle = [[x, y] for x, y in location_of_white_stones if img[y+num, x+num, 0] < 50]

        if num_or_circle != []:
            print(num_or_circle)
            print("Has black on white stone")
            print(f"num is: {num}")
            break


# black_stones_sgf = []
# white_stones_sgf = []
#
# for x, y in location_of_black_stones:
#     x = math.ceil(((x-TL_CORNER[0])/hd))
#     y = math.ceil(((y-TL_CORNER[1])/vd))
#     black_stones_sgf_conversion = [sgf_letters[x], sgf_letters[y]]
#     black_stones_sgf.append(black_stones_sgf_conversion)
#
# for x, y in location_of_white_stones:
#     x = math.ceil((x-TL_CORNER[0])/hd)
#     y = math.ceil((y-TL_CORNER[1])/vd)
#     white_stones_sgf_conversion = [sgf_letters[x], sgf_letters[y]]
#     white_stones_sgf.append(white_stones_sgf_conversion)
#
# sgf_add_black = 'AB'
# sgf_add_white = 'AW'
#
# # string join + list comprehension replaces lines 60 - 63, maybe 65. "".join takes a list
# bs = str(black_stones_sgf)[1:-1]  # assigns black_stones_sgf to bs and uses string slicing to remove brackets
# bs = bs.replace("'", "")  # removes parenthesis from coordinates
# bs = bs.replace(",", "")  # removes commas from coordinates
# bs = bs.replace(" ", "")  # removes space between coordinates
#
# final_formatted_black_stones_SGF = sgf_add_black + bs  # Adds AB ("Add Black") in front of the black stone coordinates
#
# ws = str(white_stones_sgf)[1:-1]  # assigns white_stones_sgf to ws and uses string slicing to remove brackets
# ws = ws.replace("'", "")
# ws = ws.replace(",", "")
# ws = ws.replace(" ", "")
#
# final_formatted_white_stones_SGF = sgf_add_white + ws  # Adds AW ("Add White") in front of the white stone coordinates
#
# SGF_format_start = '(;SZ[19]'  # SZ[19] means board size 19 by 19. The ( ; ) are SGF syntax
# SGF_format_end = ')'
#
# final_SGF_format = SGF_format_start + final_formatted_black_stones_SGF + final_formatted_white_stones_SGF + SGF_format_end
# print(final_SGF_format)
#
# # look up "with open python" or with "with statement"
# h = open(r"C:\Users\nharw\Desktop\image2sgf project files\image2sgf image.txt", "w")
# h.write(final_SGF_format)  # if this crashes, h.close won't go
# h.close()
#
# path_to_text_file = r"C:\Users\nharw\Desktop\image2sgf project files\image2sgf image.txt"
# path_to_CGoban = r"C:\Program Files (x86)\cgoban\cgoban.exe"
# subprocess.Popen([path_to_CGoban, path_to_text_file])  # opens text_file with CGoban (KGS's SGF editor)
#
# # if __name__ == '__main__' --> indicates this is an executable
# # singleton -> what my code does now if I import it (good if running a server / other stuff if you want it once)

