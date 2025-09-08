import cv2
import numpy as np
image = cv2.imread('low_res_image.jpg')

sharper_kernel = np.array([
  [0, -1, 0],
  [-1,5,-1],
  [0,-1,0]
])

sharpered = cv2.filter2D(image, -1, sharper_kernel)

cv2.imshow('Original Image', image)
cv2.imshow('Sharpered Image', sharpered)
cv2.waitKey(0)
cv2.destroyAllWindows()