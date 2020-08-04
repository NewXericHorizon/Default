'''
输入：第21行图片的path
输出：第32行输出的txt文件作为结果
'''

from aip import AipOcr
import time
"""百度AppID, API Key, Secret Key"""
APP_ID = '21788806'
API_KEY = 'uWjAp1GXrlF2P2e1ax3FdVzm'
SECRET_KEY = 'h88TmSVGAOucTKM3qVgLiyaZL3LvcvDt'

# 测试百度在线图片文本识别包
# 导入百度的OCR包

if __name__ == "__main__":
    appId, apiKey, secretKey = [APP_ID, API_KEY,SECRET_KEY]
    ocr = AipOcr(appId, apiKey, secretKey)
    with open('image\\Joanna.png', 'rb') as fin:
        img = fin.read()
        res = ocr.basicGeneral(img)
        dic_list=res["words_result"]
        str_dic=''
        for key, val in enumerate(dic_list):
            str_dic+=val["words"]
            str_dic+='\n'
            time.sleep(2e-4)
        print(str_dic)
    with open('ocr\\ocr_result.txt','w',encoding='utf-8') as f:
        f.write(str_dic)
    f.close()
