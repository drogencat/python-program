from aip import AipFace
import base64
import os
import time

'''
    安卓抖音识图 -- 速度慢
'''


def faceFun(path):
    # 百度云key
    APP_ID = '11309832'
    API_KEY = 'KmhCIEas4m7oj06PG4B1fs2x'
    SECRET_KEY = 'n3tw7So2bGXG91ZfPdy7rLBV8r4q7j3N'

    client = AipFace(APP_ID, API_KEY, SECRET_KEY)
    # 读取文件
    with open(path, "rb") as f:
        # b64encode是编码
        base64_data = base64.b64encode(f.read())

    image = str(base64_data, 'utf-8')
    imageType = "BASE64"
    # 参数设置
    options = {"face_field": "gender,beauty", "max_face_num": 1, "face_type": "LIVE"}
    # 调用人脸检测
    result = client.detect(image, imageType, options)
    return result


def phoneAutoScreen():
    """
    # 打开抖音
    # resultCode = os.system('adb shell am start -n com.ss.android.ugc.aweme/com.ss.android.ugc.aweme.main.MainActivity')
    # if resultCode != 0:
    #     print("执行失败", resultCode)
    #     return
    """

    # 截图
    print("截屏...")
    os.system("adb shell screencap -p /sdcard/game.png")
    print("保存电脑中...")
    os.system("adb pull /sdcard/game.png /Users/drogencat/Desktop/python/screenPhoto/game.png")  # 存入电脑里面
    # 调用识别
    filePath = "/Users/drogencat/Desktop/python/screenPhoto/game.png"
    result = faceFun(filePath)
    # 如果当前图像 没有识别出人物，滑动手机
    if result['error_code'] == 222202:
        print('未检测到活体，进入下一循环')
        os.system('adb shell input swipe 300 800 300 300')
        time.sleep(1)
        phoneAutoScreen()
    if result['error_code'] == 0:
        # beauty val
        beauty = result['result']['face_list'][0]['beauty']
        # sex  val
        sex = result['result']['face_list'][0]['gender']['type'] == 'female'
        if not sex:
            print('检测到图像为男性，长相评分为：%s,进入下一循环', beauty)
            os.system('adb shell input swipe 300 800 300 300')
            time.sleep(1)
            phoneAutoScreen()

        if sex:
            print('检测到图像为女性，长相评分为:%s' % beauty)
            if beauty > 50:
                print('评分大于50 ，点赞环节！开始！')
                os.system('adb shell input tap 1000 1350')
                print('评分大于50 ，点赞结束，进入下一循环')
                os.system('adb shell input swipe 300 800 300 300')
                time.sleep(1)
                phoneAutoScreen()

            else:
                os.system('adb shell input swipe 300 800 300 300')
                time.sleep(1)
                phoneAutoScreen()


if __name__ == '__main__':
    phoneAutoScreen()
