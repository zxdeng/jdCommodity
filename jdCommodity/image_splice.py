from os import listdir
from PIL import Image

from jdCommodity.settings import IMAGES_STORE


def spliceImage():
    dirList = listdir(IMAGES_STORE)
    for i in range(len(dirList)):
        dirList[i] = IMAGES_STORE + '\\' + dirList[i]
        print(dirList[i])
        try:
            mm = listdir(dirList[i])
            cp_list = []
            #根据前缀排序
            for img in listdir(dirList[i]):
                cp_list.insert(int(img.split('_')[0]), img)
            print(mm)
            print(cp_list)
        # 判断图片是否已经存在，如果存在，会抛出异常，直接进入下一次循环
        except NotADirectoryError:
            continue
        imgs = [Image.open(dirList[i]+"\\"+fn) for fn in cp_list]
        height = 0
        all_height=[]
        for k in range(len(imgs)):
            height += imgs[k].size[1]
            all_height.insert(k, height)
        #     print('图片高度为：' + str(imgs[k].size[1]))
        #     print('当前图片总高度为：' + str(height))
        # print('图片总高度为：' + str(height))

        newImage = Image.new(imgs[0].mode, (imgs[0].size[0], height))
        left_top = 0
        for j in range(len(imgs)):
            # print('新图片当前新增总高度为' + str(all_height[j]))
            newImage.paste(imgs[j], box=(0, left_top))
            left_top = all_height[j]
        newImage.save(dirList[i] + '.jpg')