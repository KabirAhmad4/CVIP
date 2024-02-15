import cv2
import numpy as num

image= cv2.imread("C:/Users/HS/Downloads/Gray & Cream Modern New Collection Instagram Post Carousel.png")
print(image.shape)
print(image[2][3])
# cv2.imshow("heloo",image)
# cv2.waitKey(0)

blue_channel=image[:,:,0]
green_channel=image[:,:,1]
red_channel=image[:,:,2]

# print(blue_channel)
# 

# print(green_channel)
# cv2.imshow("green",green_channel)

# print(red_channel)
# cv2.imshow("red",red_channel)
# cv2.waitKey(0)
shape= image.shape


z=num.zeros((image.shape[0],image.shape[1]))
# green
image[:,:,0]=z
image[:,:,2]=z


sub_image=image[0:75,0:50,:]
image[100:175,51:101,:]=sub_image
cv2.imshow("sub_image",image[100:175,51:101,:])

cv2.waitKey(0)


# cv2.imshow("blue",blue_channel)
# cv2.imshow("green",green_channel)
# cv2.imshow("red",red_channel)
# cv2.waitKey(0)