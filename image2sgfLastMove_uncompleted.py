import math
import cv2 # imports openCV which lets us read the image (detect colors -> for finding the black and white stones)
import subprocess # used later to open text file of SGF coordinates with KGS's SGF editor

# Pixel coordinates in [x, y] of 4 corners (image is 915x921 pixels) T = Top, L = Left, R = Right
TL_CORNER = [53, 56]
TR_CORNER = [862, 56]
BL_CORNER = [53, 865]
BR_CORNER = [862, 865]

# 19 by 19 board
GO_BOARD_SIZE = 19

# hd and vd = horizontal and vertical distances between intersections (45 pixels for both)
hd = math.ceil(float((TR_CORNER[0] - TL_CORNER[0]) / (GO_BOARD_SIZE-1)))
vd = math.ceil(float((BL_CORNER[1] - TL_CORNER[1]) / (GO_BOARD_SIZE-1)))

all_x_values = [x * hd + TL_CORNER[0] for x in range(0, GO_BOARD_SIZE)]
all_y_values = [y * vd + TL_CORNER[1] for y in range(0, GO_BOARD_SIZE)]
all_coordinates = [[x,y] for x in all_x_values for y in all_y_values]

# matplotlib (3 lines below) shows you the pixel colors and coordinates when you hover over them (openCV doesn't)
# imgPLT = image.imread(r"C:\Users\nharw\Desktop\image2sgf project files\test_images\test_image_3.png")
# plt.imshow(imgPLT)
# plt.show()

# Right click, "copy as path", paste path below
path_to_image = r"C:\Users\nharw\Downloads\Dave New 12 2023-02-03 .png"
# mode: -1 means color, 0 means gray scale, 1 means no change (including transparency value))
img = cv2.imread(path_to_image, -1)

sgf_letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s"]

# #openCV uses numpy, which means the x and y need to be swapped. In below for loop img[x,y] needs to be img[y,x]
# https://stackoverflow.com/questions/49720605/pixel-coordinates-vs-drawing-coordinates

# Below numbers are hard coded, which can be replaced by variables if necessary
# Pixel color spectrum is [0, 0, 0] to [255, 255, 255], black is 0,0,0 white is 255,255,255

location_of_black_stones = [[x, y] for x, y in all_coordinates if img[y+12, x+12, 0] < 25]
location_of_white_stones = [[x, y] for x, y in all_coordinates if img[y+12, x+12, 0] > 150]

black_stones_sgf = []
white_stones_sgf = []

for x, y in location_of_black_stones:
    x = int((x-53)/45)  # converts x value to number between 0 and 18
    y = int((y-56)/45)
    black_stones_sgf_conversion = [sgf_letters[x],sgf_letters[y]]
    black_stones_sgf.append(black_stones_sgf_conversion)

# black_stones_sgf_conversion = [[sgf_letters[int((x-53)/45)],sgf_letters[int((y-56)/45)]
# for x,y in location_of_black_stones]
# tuples are much faster - convert x,y to that

for x, y in location_of_white_stones:
    x = int((x-53)/45)
    y = int((y-56)/45)
    white_stones_sgf_conversion = [sgf_letters[x],sgf_letters[y]]
    white_stones_sgf.append(white_stones_sgf_conversion)

sgf_add_black = 'AB'
sgf_add_white = 'AW'

bs = str(black_stones_sgf)[1:-1]  # assigns black_stones_sgf to bs and uses string slicing to remove first and last bracket
bs=bs.replace("'","")  # removes parenthesis from coordinates, aka replaces ' with nothing
bs=bs.replace(",","")  # removes commas from coordinates
bs=bs.replace(" ","")  # removes space between coordinates

final_formatted_black_stones_SGF = sgf_add_black + bs #Adds AB ("Add Black") in front of the black stone coordinates

ws = str(white_stones_sgf)[1:-1] #assigns white_stones_sgf to ws and uses string slicing to remove first and last bracket
ws=ws.replace("'","")
ws=ws.replace(",","")
ws=ws.replace(" ","")

final_formatted_white_stones_SGF = sgf_add_white + ws #Adds AW ("Add White") in front of the white stone coordinates

SGF_format_start = '(;SZ[19]'  # SZ[19] means board size 19 by 19. The ( ; ) are SGF syntax
SGF_format_end = ')'

final_SGF_format = SGF_format_start + final_formatted_black_stones_SGF + final_formatted_white_stones_SGF + SGF_format_end
# final_SGF_format = SGF_format_start + player_move + final_formatted_black_stones_SGF + final_formatted_white_stones_SGF + SGF_format_end
# player_move format is PL[W] or PL[B]


print(final_SGF_format)

#look up "with open python" or with "with statement"
h = open(r"C:\Users\nharw\Desktop\image2sgf project files\image2sgf image.txt", "w")
h.write(final_SGF_format) #if this crashes, h.close won't go
h.close()

path_to_text_file = r"C:\Users\nharw\Desktop\image2sgf project files\image2sgf image.txt"
path_to_CGoban = r"C:\Program Files (x86)\cgoban\cgoban.exe"
subprocess.Popen([path_to_CGoban, path_to_text_file]) #opens text_file with CGoban (KGS's SGF editor)

# Between (;SZ[19]    and AB[bm], add the following for the move number
#  PL[W] or PL[B] for player turn