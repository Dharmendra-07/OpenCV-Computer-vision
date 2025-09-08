import cv2

image = cv2.imread('Phase-1/image1234.png')

if image is not None:
  h,w,c = image.shape
  print(f'Image Loaded: \nHeight: {h}\nWidhth: {w}\nChannels: {c}')
else:
  print('Could not load image')