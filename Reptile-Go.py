# version 0.0.1
import requests
from bs4 import BeautifulSoup
import re

#顶层函数
def main(a,b = None,c = None,d = None):  ##主函数
    print("欢迎使用Reptile-Go".center(50,"-"))
    print("功能: \n {} \n {} \n {} \n {}".format(a,b,c,d))
    global user
    user = input("请输入对应数字:")
    if user[0] in "0":
        exit()
    elif user[0] in "1":
        user_input = input(" 0.返回 \n 1.快速爬取(推荐) \n 2.精准爬取(开发ing) \n 请输入对应数字:")
        if user_input[0] in "0":
            main(a,b,c,d)
        elif user_input[0] in "1":
            url()
        elif user_input[0] in "2":
           print("正在开发中,敬请期待qwq") 
    elif user[0] in "2":
        print("正在开发中,敬请期待qwq")
    elif user[0] in "3":
        print("正在开发中,敬请期待qwq")
    else:
        print("不要输入奇怪的东西!请输入数字!")

def text_search():  ##搜索引擎爬取,待修
    content = input("请输入搜索内容:")
    request ="https://www.baidu.com/#ie=UTF-8&wd=" + content 
    txt = requests.get(request)
    txt.raise_for_status()
    txt.encoding = "utf-8"
    txt = txt.text
    save = input("是否保存html网页副本?是/否: \n")
    if save == "是":
        file = open ("requests","w+")
        file.write(txt)
        file.close
    elif save not in "是":
        if save not in "否":
            print("请检查输入是否正确!不要搞我力wwww!")
    analyse = BeautifulSoup(txt,"html.parser")
    string = input("请输入你想快速查找的内容:")
    string = str(string)
    txt =analyse.find_all(string=re.compile(string))
    print(txt)

def url():  ##自定义链接爬取
    user_url = input("请输入你要爬取的链接 \n (目前还没有提供对robots协议网站的爬取，部分网址可能无效) \n :")
    if user_url[0:4] not in "http":
         user_url = "http://" + user_url
    html = requests.get(user_url)
    html.raise_for_status()
    html.encoding = "utf-8"
    txt = html.text
    txt = BeautifulSoup(txt,"lxml")
    content = input("是否需要爬取网页上所有文字?(这可能包括一些你不需要的内容) \n 是/否:")
    if content in "是":
        for text in txt.find_all("title"):
            print(text.string)
        for text in txt.find_all("p"):
            print(text.string)
        for text in txt.find_all("div"):
            print(text.string)
        for text in txt.find_all("a"):
            print(text.string)
    elif content in "否":
        for text in txt.find_all("title"):
            print(text.string)
        for text in txt.find_all("p"):
            print(text.string)
        

#程序运行
a,b,c,d = "0.退出脚本","1.自定义链接爬取","2.搜索引擎爬取(开发ing)","3.图片爬取(开发ing)"
main(a,b,c,d)
