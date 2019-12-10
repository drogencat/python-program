# -- coding: utf-8 --
"""
    推送gitlab代码提交量到微信小程序
"""
import os
from collections import OrderedDict

import requests
import json
import datetime
'''
    检测今日代码数量
'''


def codeCount():
    userList = ['longmao', 'suolong', 'shuiyue', 'manji', "chimu", "侯振兵"]

    # 遍历集合进行统计
    dictionary = {'longmao': 0, "suolong": 0, "shuiyue": 0, "manji": 0, "chimu": 0, "侯振兵": 0}

    os.system("cd /Users/drogencat/git/shoubaodan-proj;git pull;")

    for i in range(len(userList)):
        out = os.popen("cd /Users/drogencat/git/shoubaodan-proj;git log --since=1.days --author=" + userList[
            i] + " --pretty=tformat: --numstat | awk '{ add += $1 ;} END { printf add+0}' ")
        dictionary[userList[i]] = int(out.read())

    return dictionary


def getAccessToken():
    """
    基础接口的token 获取接口
    """
    result = requests.get(
        "https://api.weixin.qq.com/cgi-bin/token",
        {
            "grant_type": "client_credential",
            "appid": "wxee025468e5187da1",
            "secret": "becd80449f562ea9efcd7bff3d21aefd",
        }
    ).json()

    if result.get("access_token"):
        access_token = result.get('access_token')
    else:
        access_token = None
    return access_token


def sendMsg(openid):
    dictionary = codeCount()

    maxCodeUser = max(dictionary, key=lambda x: dictionary[x])

    minCodeUser = min(dictionary, key=lambda x: dictionary[x])

    access_token = getAccessToken()

    # 详情
    dictionary = sortValue(dictionary)

    nowTime = datetime.datetime.now().strftime('%m-%d %H:%M')

    yestodayTime = (datetime.datetime.now() -
                    datetime.timedelta(hours=24)).strftime('%m-%d %H:%M')

    details = "从" + yestodayTime + "到" + nowTime

    for key in dictionary:
        details += "\n\n\t\t   " + key + "提交了：" + str(dictionary[key]) + "行代码"

    url = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=' + access_token

    data = json.dumps({
        "touser": openid,
        "template_id": "UDuuNto_K1ggrwv8hEDlUP5pxGVuMo2yKE98rA7TyP0",
        "url": "http://weixin.qq.com/download",
        "topcolor": "#FF0000",
        "data": {
            "first": {"value": "代码提交统计\n\n"},
            "keyword1": {"value": maxCodeUser + "\n\n", "color": "#173177"},
            "keyword2": {"value": minCodeUser + "\n\n", "color": "#173177"},
            "keyword3": {"value": minCodeUser + "\n\n", "color": "#173177"},
            "keyword4": {"value": details}
        }
    })

    result = requests.post(
        url, data
    )

    # 这里可根据回执code进行判定是否发送成功(也可以根据code根据错误信息)
    print(result.content)


# 对字典按 value 排序，默认升序, 返回 OrderedDict

def sortValue(old_dict, reverse=True):
    """对字典按 value 排序, 默认升序, 不修改原先字典"""

    # 获取按 value 排序后的元组列表

    items = sorted(old_dict.items(), key=lambda obj: obj[1], reverse=reverse)

    # 创建一个新的空字典

    new_dict = OrderedDict()

    # 遍历 items 列表

    for item in items:
        # item[0] 存的是 key 值
        new_dict[item[0]] = old_dict[item[0]]

    return new_dict


if __name__ == '__main__':
    sendMsg("oyNJDxI-BrmvGs9CZO3VHNwh-6_M")
