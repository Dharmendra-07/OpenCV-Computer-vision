import cv2

image = cv2.imread('ganesh-ji-logo.png')

if image is not None:
  success = cv2.imwrite('output_python.png', image)
  if success:
    print('Image saved successfully as "output_python.png"')
  else:
    print('Failed to save an image')
else:
  print('Error: Could not load image')  

