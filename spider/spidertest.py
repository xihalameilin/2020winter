import requests
from selenium import webdriver
import time
#此文件用于爬取评论
#需要修改这个值 表示你想写入txt的本机地址
destination = "C:\\Users\\hp\\Desktop\\comments.txt"
#这个值表示要多少个评论
resultCount = 100


def spider():
    print("------------------方法开始---------------------")
    url = 'https://music.163.com/#/song?id=1293886117'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    response = requests.get(url, headers=headers)
    broswer = webdriver.Chrome()
    broswer.get(url)
    time.sleep(10)
    broswer.switch_to.frame('g_iframe') #所爬取数据在g_iframe中，所以转到iframe中
    count = 0
    for j in range(100):
        c = broswer.find_elements_by_xpath('//div[@class="cnt f-brk"]')
        with open(destination, 'a', newline='', encoding='utf_8_sig')as f:
            for i in c:
                count += 1
                f.write(i.text+"\n")
                if(count == resultCount):
                    print("------------------方法结束---------------------")
                    broswer.quit()
                    return
            button = broswer.find_element_by_link_text('下一页')
            broswer.execute_script("arguments[0].click();", button)
            time.sleep(2)
    broswer.quit()#退出

spider()