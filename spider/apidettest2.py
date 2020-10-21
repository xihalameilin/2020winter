import requests
from selenium import webdriver
import time
#此文件用于爬取id
#需要修改这个值 表示你想写入txt的本机地址
destination = "C:\\Users\\hp\\Desktop\\ids.txt"
#这个值表示要多少个id
resultCount = 300

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
        link = broswer.find_elements_by_xpath('//div[@class="head"]/a')
        with open(destination, 'a', newline='', encoding='utf_8_sig')as f:
            for i in link:
                count += 1
                id = i.get_attribute('href')[35:]
                print("-----------获取到id为：" + id + "-----------")
                f.write(id+"\n")
                if(count == resultCount):
                    print("------------------方法结束---------------------")
                    broswer.quit()
                    return
            button = broswer.find_element_by_link_text('下一页')
            broswer.execute_script("arguments[0].click();", button)
            time.sleep(2)
    broswer.quit()#退出

spider()
