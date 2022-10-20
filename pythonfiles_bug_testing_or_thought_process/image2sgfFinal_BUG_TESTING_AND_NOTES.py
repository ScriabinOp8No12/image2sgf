import cv2 #imports openCV which lets us read the image (detect colors -> for finding the black and white stones)
import subprocess
import os

#read the image (mode: -1 means color, 0 means gray scale, 1 means no change (including transparency value))
img= cv2.imread(r"C:\Users\nharw\Desktop\image2sgf project files\test_image_3.png", -1)

#cv2.imshow("image_test",img) #opens the image in a window called "image_test"
#cv2.waitKey(0) #wait an infinite amount of time before a mouse click.
#cv2.destroyAllWindows() #mouse click closes the image window (DESTROYYYY)

from functions_image2sgf import finding_all_intersections

#computer reads from top left corner, goes all the way down, then starts at top of board again, and goes down
stones_on_intersections = finding_all_intersections()

sgf_letter_coordinates = []

sgf_letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s"]
for horz_letters in sgf_letters:
    for vert_letters in sgf_letters:
        sgf_letter_coordinates.append([horz_letters,vert_letters])
#THESE 3 lines above are not needed, was just there to print out all the letters. learn that coordinates go top down
#starting from the top left corner.

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

#writes SGF formatted stone coordinates to a text file
h = open(r"C:\Users\nharw\Desktop\image2sgf project files\image2sgf image.txt", "w")
h.write(final_SGF_format)
h.close()

path_to_text_file = r"C:\Users\nharw\Desktop\image2sgf project files\image2sgf image.txt"

test_CGoban = r"C:\Users\nharw\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\KGS"

subprocess.Popen([r"C:\Program Files (x86)\cgoban\cgoban.exe", path_to_text_file])
#path_to_CGoban = r"C:\Program Files (x86)\cgoban\cgoban.exe" #apparently if you put "path_to_CGoban" in
#subprocess.Popen(path_to_CGoban) - it doesn't work!!! But if you paste it in like it is now, it works???????????

#os.startfile(path_to_text_file) #opens text file with it's default application - the text file
#os.startfile(r'C:\Program Files (x86)\cgoban\cgoban.exe') #opens up KGS properly too


#Bug testing all intersections below:
#for x,y in stones_on_intersections:
#    x = int((x-53)/45)
#    y = int((y-56)/45)
#    print(sgf_letters[x],sgf_letters[y])

#prints out letter index positions of coordinates! (look at notebook if confused)
#for x,y in stones_on_intersections:
#   x = (x-53)/45
#   y = (y-56)/45
#   print(x,y)

#for black_stones in sgf_letter_coordinates:

#coordinate x=53, y=56
# x value    a = 53, b = 53+45, 53+2*45, etc
# y value    a = 56, b = 56+45, 56+2*45, etc

#no_stones = []

#elif img[y+12, x+12, 0] > 75 and img[y, x, 0] < 100:
#    no_stones.append([x,y]) #appends pixel location of no stone to an empty list

#all_info_of_intersections = black_stones + white_stones + no_stones
#print(all_info_of_intersections)



#Bug testing code below (manually testing each coordinate and seeing if the stone on the image is indeed correct)!
#pixel format goes [x][y] --> can be formatted as just [x,y]
#x = 380
#y = 200

#print(img[y,x])
#print(img[y,x,0])

#when openCv reads the image, the pixel colors are in Blue, Green, Red, Transparency
#note: when hovering over the pixels in matplotlib, it shows the values as fractions of 1 (instead of values out of 255),
#meaning [1, 1, 1, 1] = pure white
#and [0.5, 0.5, 0.5, 0.5] = half way between white and black
#and [0, 0, 0, 0] = pure black


# below code prints color of pixel[G,B,R] instead of the [R,G,B] from matplotlib graph at X = 50, Y = 188
#print(img[50, 188])
#below code prints pixel color at X = 188, y = 850, and prints out all the value of the "green" value b/c it's at index 0
#print(img[188,850,0])
#below code prints pixel color at X = 188, y = 850, and prints out index 0 - 2 not including 2 (prints red and green values)
#print(img[188,850,0:2])
#below code prints pixel color at X = 188, y = 850, and prints out all 4 values
#print(img[188,850,:])

#Manually checking coordinates - would take forever...
#for coordinates in new_coordinates_for_stone_checking:
#    x = new_coordinates_for_stone_checking[0][0]
#    x = new_coordinates_for_stone_checking[1][0]
#    y = new_coordinates_for_stone_checking[0][1]
#    y = new_coordinates_for_stone_checking[1][1]

#for x,y in stones_on_intersections:
    #shift_x = 12 #type a number to shift pixel amount in x direction (remember openCV uses numpy arrays so we need to flip y and x)
    #shift_y = 12 #IF NOT HARD CODING +12, below code will be img[y+shift_x, x + shift_y, 0] <25
    #print(x,y)
    #print(img[y, x]) This isn't giving me the values I expect the pixels to be! should be giving me 91, 175, 216 but it's giving me numbers very close to 0 on all coordinates

    #if img[y+12, x+12, 0] < 25: #can change this value to < 10 if needed
    #    print("Black Stone")
    #elif img[y+12, x+12, 0] > 150:
    #    print("White Stone")
    #elif img[y+12, x+12, 0] > 75 and img[y, x, 0] < 100: #can remove this, only care if stone is white or black
    #    print("No Stone")

#CODE BELOW ALSO WORKS - last line there with board color is good for bug testing!
#black_stones = []
# white_stones = []
# no_stones = []
# for x,y in stones_on_intersections:

#     if img[y+12, x+12, 0] < 25:
#         black_stones.append([x,y]) #appends a black stone to empty list
#     elif img[y+12, x+12, 0] > 150:
#         white_stones.append([x,y]) #appends a white stone to empty list
###    elif img[y+12, x+12, 0] > 75 and img[y, x, 0] < 100: #can remove this (good for bug testing though)
#         no_stones.append([x,y])
