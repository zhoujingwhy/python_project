import itchat
import re
import jieba
from math import sqrt
import os
import numpy as np
import PIL.Image as Image
import matplotlib.pyplot as plt



def download_headimg(save_path):
    """
    该函数功能为下载所有好友头像
    param save_path: 头像存储路径

    """
    itchat.auto_login()
    friends = itchat.get_friends(update=True)[0:]

    for friend in friends:
        head = itchat.get_head_img(userName=friend["UserName"])
        img_file = open(save_path + friend['RemarkName'] + '.jpg', 'wb')
        img_file.write(head)
        img_file.close()



def splice_imgs(file_path, save_path):
    """
    该函数功能为拼接图片
    :param file_path: 源图片存储路径
    :param save_path: 拼接完成的图片存储路径
    """

    # 将所有头像的路径提取出来
    path_list = []
    for item in os.listdir(file_path):
        img_path = os.path.join(file_path, item)
        path_list.append(img_path)

    # 为拼凑成一个正方形图片，每行头像个数为总数的开平方取整
    line = int(sqrt(len(path_list)))

    # 新建待拼凑图片
    New_Image = Image.new('RGB', (128 * line, 128 * line))

    x, y = 0, 0

    # 进行拼图
    for item in path_list:
        try:
            img = Image.open(item)
            img = img.resize((128, 128), Image.ANTIALIAS)
            New_Image.paste(img, (x * 128, y * 128))
            x += 1
        except IOError:
            print("第%d行,%d列文件读取失败！IOError:%s" % (y, x, item))
            x -= 1
        if x == line:
            x = 0
            y += 1
        if (x + line * y) == line * line:
            break

    # 将拼好的图片存储起来
    New_Image.show()
    New_Image.save(save_path)


download_headimg("E:/a/图片/")
file_path="E:/a/图片/"
save_path = "E:/a/拼接完成的图片/tp.jpg"
splice_imgs(file_path,save_path)

