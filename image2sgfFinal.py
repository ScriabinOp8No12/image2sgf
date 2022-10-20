import cv2 #imports openCV which lets us read the image (detect colors -> for finding the black and white stones)
from matplotlib import image #can make this consistent by making it start with "import"?
from matplotlib import pyplot as plt
from functions_and_corner_locations import finding_all_intersections #imports (x,y) pixel location of all intersections on the board
import subprocess #used later to open text file (SGF coordinates) with KGS's SGF editor

#matplotlib (3 lines below) shows you the pixel colors and coordinates when you hover over them (openCV doesn't)
#imgPLT = image.imread(r"C:\Users\nharw\Desktop\image2sgf project files\test_images\test_image_3.png")
#plt.imshow(imgPLT)
#plt.show()

#UPDATE CODE BELOW to load image you wanted converted to SGF -> can right-click image then "copy as path" to find path
path_to_image = r"C:\Users\nharw\Desktop\image2sgf project files\test_images\test_image_3.png"
#read the image (mode: -1 means color, 0 means gray scale, 1 means no change (including transparency value))
img = cv2.imread(path_to_image, -1)

#computer reads from top left corner, goes all the way down, then starts at top of board again, and goes down
stones_on_intersections = finding_all_intersections() #assigning function to a variable

sgf_letter_coordinates = []

sgf_letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s"] #sgf coordinates go a to s

location_of_black_stones = []
location_of_white_stones = []

#openCV uses numpy, which means the x and y need to be swapped. In below for loop img[x,y] needs to be img[y,x]
#https://stackoverflow.com/questions/49720605/pixel-coordinates-vs-drawing-coordinates
#Below numbers are hard coded, which can be replaced by variables if necessary

for x,y in stones_on_intersections:
    if img[y+12, x+12, 0] < 25:
        location_of_black_stones.append([x,y]) #appends pixel location of black stones to an empty list
    elif img[y+12, x+12, 0] > 150:
        location_of_white_stones.append([x,y]) #appends pixel location of white stones to an empty list

black_stones_sgf = []
white_stones_sgf = []

for x,y in location_of_black_stones:
    x = int((x-53)/45) #converts x value of pixel coordinate to number between 0 and 18
    y = int((y-56)/45) #converts y; 53,56 is starting value of top left corner of board, 45 is pixel distance between intersections
    black_stones_sgf_conversion = [sgf_letters[x],sgf_letters[y]] #sgf_letters[0] = letter a, and sgf_letters[18] = s
    black_stones_sgf.append(black_stones_sgf_conversion) #appends new SGF coordinates to empty list

for x,y in location_of_white_stones:
    x = int((x-53)/45)
    y = int((y-56)/45)
    white_stones_sgf_conversion = [sgf_letters[x],sgf_letters[y]]
    white_stones_sgf.append(white_stones_sgf_conversion)

sgf_add_black = 'AB'
sgf_add_white = 'AW'

bs = str(black_stones_sgf)[1:-1] #assigns black_stones_sgf to bs and uses string slicing to remove first and last bracket
bs=bs.replace("'","") #removes parenthesis from coordinates, aka replaces ' with nothing
bs=bs.replace(",","") #removes commas from coordinates
bs=bs.replace(" ","")#removes space between coordinates

final_formatted_black_stones_SGF = sgf_add_black + bs #Adds AB ("Add Black") in front of the black stone coordinates

ws = str(white_stones_sgf)[1:-1] #assigns white_stones_sgf to ws and uses string slicing to remove first and last bracket
ws=ws.replace("'","")
ws=ws.replace(",","")
ws=ws.replace(" ","")

final_formatted_white_stones_SGF = sgf_add_white + ws #Adds AW ("Add White") in front of the white stone coordinates

SGF_format_start = '(;SZ[19]' #SZ = board size, 19 means 19 by 19 size. The ( and ; are syntax for the start of the SGF
SGF_format_end = ')' #SGF format ends with a )

final_SGF_format = SGF_format_start + final_formatted_black_stones_SGF + final_formatted_white_stones_SGF + SGF_format_end
print(final_SGF_format) #great for bugtesting - this is how SGFs are read by the computer!

#writes SGF formatted stone coordinates to a pre-existing text file (overrides existing file each time!)
h = open(r"C:\Users\nharw\Desktop\image2sgf project files\image2sgf image.txt", "w")
h.write(final_SGF_format)
h.close()

path_to_text_file = r"C:\Users\nharw\Desktop\image2sgf project files\image2sgf image.txt"
path_to_CGoban = r"C:\Program Files (x86)\cgoban\cgoban.exe"
subprocess.Popen([path_to_CGoban, path_to_text_file]) #opens text_file with CGoban (KGS's SGF editor)
