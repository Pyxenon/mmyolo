import json
import os


def deleteEmptyJson(path):
    """
    处理labelme格式标准json专用
    删除所有未检出的空json
    """

    for root, dirs, files in os.walk(path, topdown=True):
        dirs[:] = []  # 忽略当前目录下的子目录
        for name in files:
            filePath = os.path.join(root, name)
            with open(filePath, 'r+', encoding='utf-8') as jsonFile:
                data = json.load(jsonFile)
            if len(data.get('shapes')) == 0:
                os.remove(filePath)
                print(f"delete: {filePath}")
            else:
                continue


def countEmptyJson(path):
    """
    处理labelme格式标准json专用
    统计所有未检出的空json
    """
    num = 0
    for root, dirs, files in os.walk(path, topdown=True):
        dirs[:] = []
        for name in files:
            filePath = os.path.join(root, name)
            with open(filePath, 'r+', encoding='utf-8') as jsonFile:
                data = json.load(jsonFile)
            if len(data.get('shapes')) == 0:
                num += 1
            else:
                continue
    return num


if __name__ == "__main__":
    # 定义文件路径
    path = r'D:\datasets\cb_detc_test\3-label'
    print(countEmptyJson(path))
