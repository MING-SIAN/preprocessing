import os
import shutil
import random
import glob
#定義資料集名稱
sets = ['train', 'val', 'test']
#訓練比例
train_percent = 0.8
#驗證比例
val_percent = 0.2
#測試比例
test_percent = 0
#原始路徑
original_path = r'C:\Users\ucl\Desktop\AIdeal_competition\dataset\train' 
#目標路徑
target_path = r'C:\Users\ucl\Desktop\AIdeal_competition\dataset\val'
#dataset_percent
#多打這個才不會變剩下的0.2，舉例來說，總共200張，訓練0.8，驗證0.2，若沒打這行會變成訓練160張，驗證變40*0.2張
val_percent = val_percent/ (val_percent+ test_percent)
test_percent = 1
dataset_percent = [train_percent, val_percent, test_percent] 
#圖片原名稱
original_name = 'train'


fileLists = os.listdir(original_path)

for i in fileLists:
    # 分拆成訓練與驗證資料夾
    switch = True
    for j in sets:
        set_path = os.path.join(target_path, j)
        if not os.path.isdir(set_path):
            os.mkdir(set_path)
        # 0,1,2,3,4,5分類資料夾
        class_dir = os.path.join(set_path, i)
        if not os.path.isdir(class_dir):
            os.mkdir(class_dir)
        # 查詢單一種類樣本數量
        if switch:
            dirPathPattern = os.path.join(original_path, i, str(original_name+ '*'))
            #看不懂
            sample = glob.glob(dirPathPattern)
            switch = False
        sample_number = int(len(sample)*dataset_percent[sets.index(j)])
        #從資料及隨機抽樣
        filePaths = random.sample(sample, sample_number)
        sample = set(sample) - set(filePaths)
        sample = list(sample)
        #將圖片複製之指定資料夾
        for filePath in filePaths:
            fname = os.path.basename(filePath)
            src = os.path.join(original_path, i, fname)
            dst = os.path.join(class_dir,fname)
            shutil.copyfile(src, dst)
        print(i, j, len(os.listdir(class_dir)))



