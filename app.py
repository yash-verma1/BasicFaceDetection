import cv2
import sys

img_path = sys.argv[1]

img = cv2.imread(img_path)

#print(img)
# Resizing Image
width = int(img.shape[0])
height
"""
cv2.imshow("Test Image",img)
cv2.waitKey(0)
"""
