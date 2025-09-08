import cv2

# Load image
img = cv2.imread('circle.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Threshold
_, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)

# Find contours
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    # Perimeter
    peri = cv2.arcLength(contour, True)
    
    # Polygonal approximation
    approx = cv2.approxPolyDP(contour, 0.01 * peri, True)
    
    # Draw contours
    cv2.drawContours(img, [approx], -1, (0, 255, 0), 2)

cv2.imshow('Contours with Approximation', img)
cv2.waitKey(0)
cv2.destroyAllWindows()