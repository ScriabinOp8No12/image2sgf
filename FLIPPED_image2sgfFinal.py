import math
import cv2
import subprocess

TL_CORNER = [53, 56]
TR_CORNER = [862, 56]
BL_CORNER = [53, 865]
BR_CORNER = [862, 865]

GO_BOARD_SIZE = 19

hd = math.ceil(float((TR_CORNER[0] - TL_CORNER[0]) / (GO_BOARD_SIZE-1)))
vd = math.ceil(float((BL_CORNER[1] - TL_CORNER[1]) / (GO_BOARD_SIZE-1)))

all_x_values = [x * hd + TL_CORNER[0] for x in range(0, GO_BOARD_SIZE)]
all_y_values = [y * vd + TL_CORNER[1] for y in range(0, GO_BOARD_SIZE)]
all_coordinates = [[x,y] for x in all_x_values for y in all_y_values]

# Change path below for your specific image you want converted
path_to_image_FOR_FLIPPING = r"C:\Users\nharw\Desktop\Situation puzzles\Dave 14 2023-01-13.png"

img = cv2.imread(path_to_image_FOR_FLIPPING, -1)

sgf_letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s"]

location_of_black_stones = [[x, y] for x, y in all_coordinates if img[y+12, x+12, 0] < 25]
location_of_white_stones = [[x, y] for x, y in all_coordinates if img[y+12, x+12, 0] > 150]

black_stones_sgf = []
white_stones_sgf = []

for x, y in location_of_black_stones:
    x = int((x-53)/45)
    y = int((y-56)/45)
    black_stones_sgf_conversion = [sgf_letters[x],sgf_letters[-y-1]]  # swapped from [y]
    black_stones_sgf.append(black_stones_sgf_conversion)

for x, y in location_of_white_stones:
    x = int((x-53)/45)
    y = int((y-56)/45)
    white_stones_sgf_conversion = [sgf_letters[x],sgf_letters[-y-1]]  # swapped from [y]
    white_stones_sgf.append(white_stones_sgf_conversion)

sgf_add_black = 'AW'  # swapped from 'AB'
sgf_add_white = 'AB'  # swapped from 'AW'

bs = str(black_stones_sgf)[1:-1]
bs=bs.replace("'", "")
bs=bs.replace(",", "")
bs=bs.replace(" ", "")

final_formatted_black_stones_SGF = sgf_add_black + bs

ws = str(white_stones_sgf)[1:-1]
ws=ws.replace("'", "")
ws=ws.replace(",", "")
ws=ws.replace(" ", "")

final_formatted_white_stones_SGF = sgf_add_white + ws

SGF_format_start = '(;SZ[19]'
SGF_format_end = ')'

final_SGF_format = SGF_format_start + final_formatted_black_stones_SGF + final_formatted_white_stones_SGF + SGF_format_end
print(final_SGF_format)

h = open(r"C:\Users\nharw\Desktop\image2sgf project files\image2sgf image.txt", "w")
h.write(final_SGF_format)
h.close()
path_to_text_file = r"C:\Users\nharw\Desktop\image2sgf project files\image2sgf image.txt"
path_to_CGoban = r"C:\Program Files (x86)\cgoban\cgoban.exe"
subprocess.Popen([path_to_CGoban, path_to_text_file])
