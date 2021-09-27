import os

class BatchRename():
    #目標資料夾
    def __init__(self):
        self.path = r'C:\Users\UCL\Desktop\test_matlab\data\test_data\ground-truth'

    def rename(self):
        #獲取檔案路徑
        filelist = os.listdir(self.path)
        #檔案個數
        total_num = len(filelist)
        print(total_num)
        #重新命名     
        i = 301                   
        for item in filelist:
            if item.endswith('.jpg'):#初始格式(.jpg)  
                src = os.path.join(os.path.abspath(self.path), item)
                dst = os.path.join(os.path.abspath(self.path), 'IMG_'+str(i) + '.jpg')
                os.rename(src, dst)
                print ('converting %s to %s ...' % (src, dst))
                i = i + 1
        print ('total %d to rename & converted %d jpgs' % (total_num, i))

if __name__ == '__main__':
    demo = BatchRename()
    demo.rename()


