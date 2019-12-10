import os
import cv2


def main():
    # os.system('adb shell dumpsys window ')  # 查看所有软件包
    # os.system('adb shell dumpsys meminfo com.tencent.mobileqq  ') #查看软件信息
    # os.system('adb shell dumpsys alarm ')# 查看系统闹钟
    # os.system('sqlite3 test.db ')# 查看系统数据库
    # 电源键
    # os.system('adb shell input keyevent KEYCODE_POWER ')
    # active = os.system('adb shell dumpsys window windows | grep "Current"')# 当前页面的应用
    # print(active)
    # os.system('adb shell am start -n com.tencent.mobileqq/com.tencent.mobileqq.activity.SplashActivity') # 打开软件

    # os.system('adb shell am start -n com.ss.android.ugc.aweme/com.ss.android.ugc.aweme.main.MainActivity') # 打开软件

    # 下滑
    # while True:

    # os.system('adb shell input swipe 540 1300 540 500 100')
    # image = cv2.imread('/Users/drogencat/Desktop/python/screenPhoto/game.png')
    # # hsv = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # im = cv2.resize(image, (1080, 2160))
    # task = cv2.inRange(im,0,0)
    # cv2.imshow("t",task)
    # cv2.waitKey(0)

    # dict = {'error_code': 0, 'error_msg': 'SUCCESS', 'log_id': 9915359920179, 'timestamp': 1573539908, 'cached': 0,
    #         'result': {'face_num': 1, 'face_list': [{'face_token': '60c949b4e236a51606697c3239a22dea',
    #                                                  'location': {'left': 549.55, 'top': 884.68, 'width': 108,
    #                                                               'height': 117, 'rotation': 42},
    #                                                  'face_probability': 0.71,
    #                                                  'angle': {'yaw': -43.35, 'pitch': -5.25, 'roll': 32.11},
    #                                                  'gender': {'type': 'female', 'probability': 0.98},
    #                                                  'beauty': 45.58}]}}
    # # beauty val
    # beauty = dict['result']['face_list'][0]['beauty']
    # print(beauty)
    # # sex  val
    # sex = dict['result']['face_list'][0]['gender']['type'] == 'female'
    print('sex')


if __name__ == '__main__':
    main()
