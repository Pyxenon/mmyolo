import os
import shutil


def copyLabeledPic(labelFolder, picFolder, outFolder):
    '''
    有对应Label的图片(相同文件名)copy至out
    标签文件夹必须纯净，不包含子文件夹
    '''

    labelList = []
    for root, dirs, files in os.walk(labelFolder, topdown=True):
        dirs[:] = []  # 忽略当前目录下的子目录
        for name in files:
            labelList.append(os.path.splitext(name)[0])

    for root, dirs, files in os.walk(picFolder, topdown=True):
        dirs[:] = []
        for name in files:
            picName = os.path.splitext(name)[0]
            if picName in labelList:
                picPath = str(root) + "\\" + str(name)
                shutil.copy(picPath, outFolder)
                print(f"copy: {picName}")


if __name__ == '__main__':
    labelFolder = r"D:\datasets\cb_detc_test\3-label"
    picFolder = r"D:\datasets\cb_detc_test\2-images"
    outFolder = r"D:\datasets\cb_detc_test\3-images"

    copyLabeledPic(labelFolder, picFolder, outFolder)
