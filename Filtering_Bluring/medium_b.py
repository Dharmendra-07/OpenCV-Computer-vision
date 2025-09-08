import cv2

image = cv2.imread('water-body.png')
blurred = cv2.medianBlur(image, 9)

cv2.imshow('Original', image)
cv2.imshow('Blurred Image', blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()