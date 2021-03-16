import os
import random
import shutil

def copyFile(fileDir):

	pathDir = os.listdir(fileDir)
	sample = random.sample(pathDir, 500)
	print (sample)
	
	# 3
	for name in sample:
		shutil.copyfile(fileDir+name, tarDir+name)
if __name__ == '__main__':
	fileDir = "C:/Users/ucl/Desktop/AIdeal_competition/data_augmentation/val/4/"
	tarDir = "C:/Users/ucl/Desktop/AIdeal_competition/dataset_final/val/4/"
	copyFile(fileDir)
