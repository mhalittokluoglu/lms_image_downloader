import cv2
import os


images_path = []
images = os.listdir('./New_images/')
for element in images:
    images_path.append('./New_images/'+element)

images_path.sort()

def compare_diff(diff_gray):
    is_same = True
    for rows in diff_gray:
        for element in rows:
            if element != 0:
                is_same = False

    return is_same

counter = 0
rm_str =[]
for image in images_path:
    img1 = cv2.imread(image)
    for i in range(counter,counter+2):
        try:
            img2 = cv2.imread(images_path[i])
            dif1 = cv2.absdiff(img1,img2)
            dif1_gray = cv2.cvtColor(dif1,cv2.COLOR_BGR2GRAY)
            if image != images_path[i]:
                if compare_diff(dif1_gray):
                    print(f'{image} and {images_path[i]} are the same images')
                    rm_str.append('rm -f '+images_path[i])
        except IndexError:
            pass
    counter += 1

for j in rm_str:
    os.system(j)
