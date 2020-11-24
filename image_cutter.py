import cv2
import os


y1 = 55
y2 = 805
x1 = 130
x2 = 1130
images_path = []
images = os.listdir('./Images/')
for element in images:
    images_path.append('./Images/'+element)



counter = 0
for image in images_path:
    img = cv2.imread(image)
    roi_image = img[y1:y2, x1:x2]
    cv2.imwrite('./New_images/'+images[counter],roi_image)
    counter += 1
