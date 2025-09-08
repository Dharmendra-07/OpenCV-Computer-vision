import cv2

# Load the image
img = cv2.imread("image1234.png")

# Check if image is loaded
if img is None:
    print("Error: Could not load image.")
    exit()

# Convert BGR → Grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Save the grayscale image
cv2.imwrite("grayscale.png", gray)
print("✅ Grayscale image saved as grayscale.png")
