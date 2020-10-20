from selenium import webdriver
import selenium.webdriver.support.ui as ui

# 存储为文本
def write2txt(data,path):
    file = open(path, "w")
    file.write(data)
    file.close()


driver = webdriver.Chrome()#chrome浏览器的驱动，下载链接：https://chromedriver.storage.googleapis.com/2.31/chromedriver_linux64.zip

driver.get("http://music.163.com/#/user/songs/rank?id=39686047")#需要抓取的用户链接，这里注意的是这里的id不是用户的id，而是用户听歌形成的所有时间排行的排行版的id

driver.switch_to.frame('g_iframe')  # 从windows切换到frame，切换到歌曲列表所在的frame

data=''#用来保存数据
try:
    wait = ui.WebDriverWait(driver, 15)
    #找到歌曲列表所在的父标签
    if wait.until(lambda driver: driver.find_element_by_class_name('g-bd')):
        print('success!')
        data += driver.find_element_by_id('rHeader').find_element_by_tag_name('h4').text+'\n'
        print(data)#抓取用户听了多少首歌
        lists = driver.find_element_by_class_name('m-record').find_elements_by_tag_name('li')
        print(len(lists))#网易只给出了前100首听的最频繁的歌
        for l in lists:
            temp = '歌曲名：'+l.find_element_by_tag_name('b').text+' 歌手：'+l.find_element_by_class_name('s-fc8').text.replace('-','')+' 频率：'+l.find_element_by_class_name('bg').get_attribute('style')
            print(temp)#解析出歌名 歌手 频率
            data += temp+'\n'

finally:
    driver.quit()
