import os
import time
# pip install baidu-aip 来进行安装
from aip import AipOcr

# 新建一个AipOcr对象
# appId apiKey secretKey 需要在https://cloud.baidu.com/product/ocr.html免费开通文字识别服务后获取
config = {
    'appId': '********',
    'apiKey': 'fE*****28xZc*****O57eZ**',
    'secretKey': '*****Ay5m7*****BhMpL*****1xVP0**'
}
client = AipOcr(**config)

pic_dir = r"D:\\desk\\pics\\"


# 读取图片
def get_file_content(file_path):
    with open(file_path, 'rb') as fp:
        return fp.read()


# 识别图片里的文字
def img_to_str(image_path):
    image = get_file_content(image_path)
    # 调用通用文字识别, 图片参数为本地图片
    result = client.basicAccurate(image)
    # 结果拼接返回
    words_list = []
    if 'words_result' in result:
        if len(result['words_result']) > 0:
            for w in result['words_result']:
                words_list.append(w['words'])
            print(words_list)
            file_name = get_code(words_list, 7)
            if file_name == None:
                file_name = 'None' + '-' + str(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()))
            print(file_name)
            os.rename(image_path, pic_dir + str(file_name).replace("/", "") + '.jpg')


# 获取字符串列表中最长的字符串
def get_longest_str(str_list):
    return max(str_list, key=len)

# 获取字符串列表中7位服务编号、11位快速服务代码
def get_code(str_list, length):
    code_num = ''
    for str in str_list:
        if len(str.strip()) == length:
            code_num = str
            return code_num
    return None

# 遍历某个文件夹下所有图片
def query_picture(dir_path):
    pic_path_list = []
    for filename in os.listdir(dir_path):
        pic_path_list.append(dir_path + filename)
    return pic_path_list


if __name__ == '__main__':
    pic_list = query_picture(pic_dir)
    if len(pic_list) > 0:
        for i in pic_list:
            img_to_str(i)
