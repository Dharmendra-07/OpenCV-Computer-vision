import cv2

image = cv2.imread('ganesh-ji-logo.png')

if image is not None:
  h,w,c = image.shape
  print(f'Image Loaded: \nHeight: {h}\nWidhth: {w}\nChannels: {c}')
else:
  print('Could not load image')