import os
from cv2 import cv2
from PIL import Image
import numpy as np
import shutil
import random

def rotate(image, angle, center=None, scale=1.0):
    # 圖片寬、高
    (h, w) = image.shape[:2]
    # 預設使用圖片中心作為旋轉中心
    if center is None:
        center = (w / 2, h / 2)
    # 旋轉
    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (w, h))
 
    return rotated

def avg_blur(img, max_filiter_size = 3) :
	img = img.astype(np.uint8)
	if max_filiter_size >= 3 :
		filter_size = random.randint(3, max_filiter_size)
		if filter_size % 2 == 0 :
			filter_size += 1
		out = cv2.blur(img, (filter_size, filter_size))
	return out

def gaussain_blur(img, max_filiter_size = 3, sigma = 0) :
    img = img.astype(np.uint8)
    if max_filiter_size >= 3 :
        filter_size = random.randint(3, max_filiter_size)
        if filter_size % 2 == 0 :
            filter_size += 1
    # print ('size = %d'% filter_size)
    out = cv2.GaussianBlur(img, (filter_size, filter_size), sigma)
    return out

def flip(img) :
	img = img.astype(np.uint8)
	flip_factor = random.randint(-1, 1) # -1:水平垂直翻轉，0:垂直翻轉，1:水平翻轉
	out = cv2.flip(img, flip_factor)
	return out, flip_factor

#對比度
def contract(image, c, b):
    rows, cols, channels = image.shape
    blank = np.zeros([rows, cols, channels], image.dtype)
    contract_img = cv2.addWeighted(image, c, blank, 1-c, b)
    return contract_img

# input_path
input_path = r'C:\Users\ucl\Desktop\AIdeal_competition\dataset\train'  # 輸入資料夾
# output_path
out_path = r'C:\Users\ucl\Desktop\AIdeal_competition\data_aug_jack\train'
# 擴增後每一類別的數量
total_num = 2000
# 要使用的擴增方法
aug_list = ['contract']    
 # 類別
class_id = '2' 

# 建立資料夾
if not os.path.isdir(os.path.join(out_path, class_id)):
        os.mkdir(os.path.join(out_path, class_id))

fold_path = os.path.join(input_path, class_id)
img_list = os.listdir(fold_path)
#print(img_list)

# 複製原始圖片
for img in img_list:
    shutil.copy(os.path.join(fold_path, img), os.path.join(out_path, class_id, img))

if len(img_list) < total_num:    # 判斷資料是否需要擴增
    idxs = np.random.randint(0, len(img_list), size= total_num - len(img_list)) # 隨機挑選被擴增的樣本
for idx in  idxs:
    img_name = img_list[idx]
    img = cv2.imread(os.path.join(fold_path, img_name))
    aug = random.choice(aug_list)
    # 翻轉
    if  aug == 'flip':  
        img_aug, _ = flip(img)
    # 高斯濾波    
    elif aug == 'gaussain_blur': 
        img_aug = gaussain_blur(img)
    # 均值濾波
    elif aug == 'avg': 
        img_aug = avg_blur(img)
    #亮度
    elif aug == 'contract': 
        img_aug = contract(img, 1.1, 3)
    #旋轉
    elif aug == 'rotate': 
        # 隨機選轉角度
        degree = np.random.randint(-90, 90)
        img_aug = rotate(img , degree)

    img_name = '{}_{}.jpg'.format(img_name.split('.')[0], aug)    
    img_out = os.path.join(out_path, class_id,img_name)
    # 若檔案已經存在，重新命名
    i = 1
    while os.path.isfile(img_out):
        img_rename = '{}({}).jpg'.format(img_name.split('.')[0], str(i))
        img_out = os.path.join(out_path, class_id,img_rename)
        i += 1
    cv2.imwrite(img_out, img_aug)



































# import os
# import torch
# import torchvision
# import numpy as np
# import shutil
# import random
# import argparse
# import torchvision.transforms as transforms

# from cv2 import cv2
# from PIL import Image


# #旋轉
# def rotate(image, angle, center=None, scale=1.0):
#      #獲取圖像尺寸(長, 寬, 高)
#     (h, w) = image.shape[:2]
#     if center is None :
#          center = (w / 2, h / 2)
#     #getRotationMatrix2D(中心, 角度, 縮放比例)
#     M = cv2.getRotationMatrix2D(center, angle, scale)
#     #warpAffine(原圖, M, (寬, 高))
#     rotated = cv2.warpAffine(image, M, (w, h))

#     return rotated

# #均值濾波
# def mean_filter(image, max_filiter_size = 3):
#     if max_filiter_size >= 3:
#         filter_size = random.randint(3, max_filiter_size)
#         if filter_size % 2 == 0:
#             filter_size += 1
#     out = cv2.blur(image, (filter_size, filter_size))
#     return out

# #高斯模糊
# def gaussain_blur(image, max_filiter_size = 3, sigma = 0):
#     if max_filiter_size >= 3:
#         filter_size = random.randint(3, max_filiter_size)
#         if filter_size % 2 == 0:
#             filter_size +=1
#     out = cv2.GaussianBlur(image, (filter_size, filter_size), sigma)
#     return out

# #翻轉
# def flip(image):
#     flip_factor = random.randint(-1, 1)
#     out = cv2.flip(img, flip_factor)
#     return out, flip_factor

# #對比度
# def contract(image, c, b):
#     rows, cols, channels = image.shape
#     blank = np.zeros([rows, cols, channels], image.dtype)
#     contract_img = cv2.addWeighted(image, c, blank, 1-c, b)
#     return contract_img


# #原圖路徑
# original_path = r"C:\Users\ucl\Desktop\AIdeal_competition\dataset\train"
# #目標路徑
# target_path = r"C:\Users\ucl\Desktop\AIdeal_competition\data_aug_jack\train"

# # 擴增後每一類別的數量
# total_num = 2000
# # 要使用的擴增方法
# aug_list = ['flip', 'gaussain_blur']    
#  # 類別
# class_id = '5' 

# # 建立資料夾
# if not os.path.isdir(os.path.join(target_path, class_id)):
#         os.mkdir(os.path.join(target_path, class_id))

# fold_path = os.path.join(original_path, class_id)
# img_list = os.listdir(fold_path)

# # 複製原始圖片
# for img in img_list:
#     shutil.copy(os.path.join(fold_path, img), os.path.join(target_path, class_id, img))

# if len(img_list) < total_num:    # 判斷資料是否需要擴增
#     idxs = np.random.randint(0, len(img_list), size= total_num - len(img_list)) # 隨機挑選被擴增的樣本
# for idx in  idxs:
#     img_name = img_list[idx]
#     img = cv2.imread(os.path.join(fold_path, img_name))
#     aug = random.choice(aug_list)
#     # 翻轉
#     if  aug == 'flip':  
#         img_aug, _ = flip(img)
#     # 高斯濾波    
#     elif aug == 'gaussain_blur': 
#         img_aug = gaussain_blur(img)
#     # 均值濾波
#     elif aug == 'avg': 
#         img_aug = mean_filter(img)
#     # 旋轉
#     elif aug == 'rotate': 
#         # 隨機選轉角度
#         degree = np.random.randint(-90, 90)
#         img_aug = rotate(img , degree)

#     img_name = '{}_{}.jpg'.format(img_name.split('.')[0], aug)    
#     img_out = os.path.join(target_path, class_id,img_name)
#     # 若檔案已經存在，重新命名
#     i = 1
#     while os.path.isfile(img_out):
#         img_rename = '{}({}).jpg'.format(img_name.split('.')[0], str(i))
#         img_out = os.path.join(target_path, class_id,img_rename)
#         i += 1
#     cv2.imwrite(img_out, img_aug)




# for item in os.listdir(original_path):
#     #提取路徑名稱
#     fname = os.path.splitext(item)
#     os.path.split(fname[0])
#     file_name = fname[0]
#     path_com =os.path.join(original_path, item)

#     img = cv2.imread(path_com)

#     for i in range(0,5):
#         flip_1 = flip(img)
#         newName = os.path.join(target_path, file_name)
#         newNameTotal = newName + "_flip_type" + "_1.jpg"
#         print(newNameTotal)
#         cv2.imwrite(newNameTotal, flip_1)

       
       
       
       
        # for i in range(1, 2):
        #     sigma = (50*i)
        #     sharp_2 = sharpen(sharp_1, sigma)
        #     newName = os.path.join(target_path, file_name)
        #     newNameTotal = newName + "_sharpen_type" + "_2.jpg"
        #     print(newNameTotal)
        #     cv2.imwrite(newNameTotal, sharp_2)
     



