import cv2

# Load image from same folder
img = cv2.imread("image1234.png")

# Safety check
if img is None:
    print("Error: Could not load image. Check filename and format.")
else:
    cv2.imshow("My Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()