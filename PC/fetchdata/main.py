# -*- coding: utf-8 -*-
import time
from urllib.parse import quote

import requests


def fetchUserId(username):
    global userId, scheme
    type = "type=3&q=" + str(
        username)
    chinese_str_url = quote(type)

    searchUser = "https://m.weibo.cn/api/container/getIndex?containerid=100103" + chinese_str_url + "&page_type=searchall"
    # headers
    headers = {
        'accept': "*/*",
        "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "content-type": "application/x-www-form-urlencoded",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-requested-with": "XMLHttpRequest"
    }
    res = requests.get(searchUser, headers)
    if res.status_code == 200:
        items = res.json().get("data").get("cards")
        for item in items:
            if item.get("card_type") == 11:
                userId = item.get("card_group")[0].get("user").get("id")
                break
    return "107603" + str(userId)


def fetchImage(userName, dir, pageNum):
    print(userName, dir)
    userName = fetchUserId(userName)
    print(userName)
    # target url
    global headers, sinceId
    if pageNum == 0:
        targetUrl = "https://m.weibo.cn/api/container/getIndex?containerid=" + str(userName)
    else:
        targetUrl = "https://m.weibo.cn/api/container/getIndex?containerid= " + str(
            userName) + "&since_id=" + str(sinceId)

    # save path
    # headers
    headers = {
        'accept': "*/*",
        "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "content-type": "application/x-www-form-urlencoded",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-requested-with": "XMLHttpRequest"
    }
    res = requests.get(targetUrl, headers)
    if res.status_code == 200:
        items = res.json().get("data").get("cards")
        sinceId = res.json().get("data").get("cardlistInfo").get("since_id")
        for item in items:
            if item.get("mblog") != None:
                pics = item.get("mblog").get("pics")
            else:
                continue
            picList = []
            if pics is not None:
                for pic in pics:
                    pic_dict = {"pid": pic.get("pid"), "url": pic.get("large").get("url")}
                    picList.append(pic_dict)
            downLoad(picList, dir)


def downLoad(results, path):
    path = path + "/"
    for result in results:
        img_name = result.get("pid") + ".jpg"
        try:
            img_data = requests.get(result.get("url")).content
            with open(path + img_name, "wb") as file:
                file.write(img_data)
                file.close()
                print(img_name + "\tdownload success!")
                time.sleep(3)
        except Exception as e:
            print(print(img_name + "\tdownload fail!", e.args))


def fetchByPage(userName, path, totalPage):
    i = 0
    for i in range(i, int(totalPage)):
        fetchImage(userName, path, i)
