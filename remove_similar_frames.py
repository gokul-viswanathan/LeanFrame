import cv2
import os
from skimage.metrics import structural_similarity as ssim

def orb_sim(img1, img2):
    img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # Compute SSIM
    score, diff = ssim(img1_gray, img2_gray, full=True)
    # print(f"SSIM score: {score}")

    return score

home_folder = "/home/gokulv/Documents/projects/ASL/still frames removal/"

for current in  os.listdir(home_folder):

    folder = home_folder + current
    print(f"currently in the folder {current}")
    arr = []
    counter = 0

    for pic in os.listdir(folder):
        arr.append(pic)
    arr.sort()

    src = folder + "/" + arr[0]
    for pic in arr:
        cmp = folder + "/" + pic
        img1 = cv2.imread(src)
        img2 = cv2.imread(cmp)
        orb_similarity = orb_sim(img1, img2) 
        
        if counter !=0 and orb_similarity*1000 > 985:
            os.remove(src)
            print(f"Similarity between {src[-8:]} and {pic} is  {orb_similarity * 1000}")
        src = cmp
        counter += 1

    print(f"the counter value is {counter}")