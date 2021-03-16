import os
import numpy as np
import pandas as pd
import shutil
from tqdm import tqdm

#圖片路徑
target_path = r"C:\Users\ucl\Desktop\AIdeal_competition\dataset\train"
original_path = r"C:\Users\ucl\Desktop\AIdeal_competition\train_images\train_images"

#csv路徑
df = pd.read_csv(r"C:\Users\ucl\Desktop\AIdeal_competition\train.csv")

#0~5類label
#建立新的資料夾0-5
for i in range(0,6):
    newpath = os.path.join(target_path , str(i))
    os.makedirs(newpath)


for index, row in tqdm(df.iterrows()):
    #路徑+檔案名字
    #先分在擴
    now = os.path.join(original_path , str(row[0]))
    after = os.path.join(target_path, str(row[1]) , str(row[0]))
    shutil.copy(now,after)


