import cv2
import numpy as np

def detect_dust(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian Blur
    blur = cv2.GaussianBlur(gray, (9, 9), 0)

    # Find difference (dust areas)
    diff = cv2.absdiff(gray, blur)
    _, dust_mask = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

    # Display
    cv2.imshow("Original", img)
    cv2.imshow("Dust Mask", dust_mask)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()

    return gray, blur, dust_mask, img
