import cv2
import numpy as np

img= cv2.imread(r"C:\Users\nharw\Desktop\image2sgf project files\test_image_3.png", -1)

cv2.imshow("image_test",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


x = 97
y = 819

print (img[y+12,x+12])
