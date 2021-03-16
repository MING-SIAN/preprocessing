##將深度學習資料及分成訓練集與驗證集和測試集
# 將filePath檔案下的圖片儲存在newFilePath資料夾下的相應子資料夾中
# pic 是字典，存放每個圖片要移到的子資料夾名

import os, random, shutil
def moveFile(fileDir):
        #圖片原始路徑
        pathDir = os.listdir(fileDir)    
        #總共有幾個檔案
        filenumber=len(pathDir)
        rate=0.1    #驗證抽取比例
        picknumber=int(filenumber*rate) #按照rate比例劃分資料集
        sample = random.sample(pathDir, picknumber)  #隨機抽取樣本圖片
        print (sample)
        for name in sample:
                shutil.copyfile(fileDir+name, tarDir+name) 
        return

if __name__ == '__main__':
	fileDir = "C:\\Users\\ucl\\Desktop\\AIdeal_competition\\dataset\\train"    #   original_path
	tarDir = r'C:\Users\ucl\Desktop\AIdeal_competition\dataset\val'    #   target_path
	moveFile(fileDir)