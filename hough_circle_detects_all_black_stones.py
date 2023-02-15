import cv2
import numpy as np

def detect_circles(img):
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    gray_blur = cv2.GaussianBlur(gray, (9, 9), 0)

    # Set the parameters for Hough Circle Transform
    dp = 1
    minDist = 20
    param1 = 50
    param2 = 30
    minRadius = 18
    maxRadius = 20

    # Detect circles using Hough Circle Transform
    circles = cv2.HoughCircles(gray_blur, cv2.HOUGH_GRADIENT, dp, minDist, param1=param1, param2=param2, minRadius=minRadius, maxRadius=maxRadius)

    # Ensure at least one circle was found
    if circles is not None:
        # Convert the (x, y) coordinates and radius of the circles to integers
        circles = np.round(circles[0, :]).astype("int")

        # Draw the circles on the image
        for (x, y, r) in circles:
            cv2.circle(img, (x, y), r, (0, 255, 0), 2)

    # Display the resulting image
    cv2.imshow("Detected circles", img)
    cv2.waitKey(0)

# Load the image of the Go board
img = cv2.imread(r"C:\Users\nharw\Desktop\Extra folder of puzzles\Eric 1 2023-02-11.png")

# Detect circles in the image
detect_circles(img)

