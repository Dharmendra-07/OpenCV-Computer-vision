import cv2

# Correct relative path (since image is in same folder as script)
img = cv2.imread("image1234.png")

if img is None:
    print("Error: Image not found")
else:
    cv2.imshow("Loaded Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()