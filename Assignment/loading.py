import cv2

image = cv2.imread('ganesh-ji-logo.png')

if image is None:
  print('Error: Image not found')
else:
  cv2.imshow('Loaded Image', image)
  cv2.waitKey(0)
  cv2.destroyAllWindows()

