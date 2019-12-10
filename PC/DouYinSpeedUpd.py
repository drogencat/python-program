from PIL import ImageGrab
import pyautogui
from aip import AipFace
import base64
import time
from Log import logInfo

'''pc模拟器抖音识图'''


def cutComputerPhoto(i):
    box = (0, 200, 600, 1200)
    im = ImageGrab.grab(box)
    # 参数 保存截图文件的路径
    im.save('/Users/drogencat/Desktop/python/screenPhoto/game.png')
    # 调用识别
    filePath = "/Users/drogencat/Desktop/python/screenPhoto/game.png"
    result = faceFun(filePath)
    # 如果当前图像 没有识别出人物，滑动电脑
    if result['error_code'] == 222202:
        # 连续问题 todo
        logInfo('[第:%s 次]未检测到活体，进入下一循环' % i)
        pyautogui.scroll(-500, x=100, y=700)
        time.sleep(1)
        cutComputerPhoto(i+1)
    if result['error_code'] == 0:
        # beauty val
        beauty = result['result']['face_list'][0]['beauty']
        # sex  val
        sex = result['result']['face_list'][0]['gender']['type'] == 'female'
        if not sex:
            logInfo('[第:%s 次]检测到图像为男性，长相评分为:%s,进入下一循环' % (i, beauty))
            pyautogui.scroll(-500, x=100, y=700)
            time.sleep(1)
            cutComputerPhoto(i+1)

        if sex:
            logInfo('[第:%s 次]检测到图像为女性，长相评分为:%s' % (i, beauty))
            if beauty > 0:
                logInfo('[第:%s 次]评分大于50 ，点赞关注环节！开始！' % i)
                pyautogui.click(365, 412)
                pyautogui.click(365, 457)
                logInfo('[第:%s 次] 评分大于50 ，点赞关注环节，进入下一循环' % i)
                pyautogui.scroll(-500, x=100, y=700)
                time.sleep(1)
                cutComputerPhoto(i+1)

            else:
                pyautogui.scroll(-500, x=100, y=700)
                time.sleep(1)
                cutComputerPhoto(i+1)


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


if __name__ == '__main__':
    cutComputerPhoto(1)
