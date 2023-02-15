import cv2
import numpy as np

def detect_circles(img):

    # Convert the image to grayscale, houghcircles method requires this
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to preprocess image better, it actually does make a difference
    gray_blur = cv2.GaussianBlur(gray, (9, 9), 0)

    # Parameters for Hough Circle Transform
    dp = 1
    minDist = 20
    param1 = 50
    param2 = 30
    minRadius = 10  # between 10 and 15 radius gets you the hollow inner circle
    maxRadius = 15

    # Detect circles using Hough Circle Transform
    circles = cv2.HoughCircles(gray_blur, cv2.HOUGH_GRADIENT, dp, minDist, param1=param1, param2=param2, minRadius=minRadius, maxRadius=maxRadius)

    # If no circles detected, function immediately returns false
    if circles is not None:
        # Convert the (x, y) coordinates and radius of the circles to integers
        circles = np.round(circles[0, :]).astype("int")

        # loops over each detected circle and extracts its center coordinate (x, y) and radius r.
        for (x, y, r) in circles:
            # draws circle with center: (x, y), radius: r, color: green (0, 255, 0), thickness: 3 pixels
            cv2.circle(img, (x, y), r, (0, 255, 0), 3)

    # Display the resulting image
    cv2.imshow("Detected circles", img)
    cv2.waitKey(0)


# Load the image of the Go board
img = cv2.imread(r"C:\Users\nharw\Desktop\Extra folder of puzzles\Eric 1 2023-02-11.png")

# Call detect_circles function
detect_circles(img)

