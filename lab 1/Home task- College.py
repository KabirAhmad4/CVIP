import cv2
import numpy as num

image2= cv2.imread("Downloads/resize_image.png")
print(image2.shape)
h,w,c= image2.shape
image= cv2.imread("c:/Users/HS/Downloads/IMG_2745-removebg-preview.png")
w=280
h=345
image=cv2.resize(image,(w,h))
image2=cv2.resize(image2,(w,h))

x=num.concatenate((image2, image,image2,image,image2), axis=1, out=None)
y=num.concatenate((image, image2, image, image2, image), axis=1, out=None)

z=num.concatenate((x, y), axis=0, out=None)
print(x.shape)

cv2.imshow("heloo",z)
cv2.waitKey(0)
