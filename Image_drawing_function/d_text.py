import cv2

image = cv2.imread('image1234.png')

if image is None:
    print('Oops! Your image is not working')
else:
    print('Image loaded successfully')
    
    # Add two different texts
    cv2.putText(image, 'Hello Python Programmers - RED', (50, 600), 
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,0,255), 2)

    cv2.putText(image, 'Hello Python Programmers - YELLOW', (50, 300), 
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,255,255), 2)

    cv2.imshow('Adding Text over image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()