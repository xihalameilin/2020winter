from selenium import webdriver
import selenium.webdriver.support.ui as ui


data = ''  # 用来保存数据
with open("id.txt", "r") as f:
    a = f.readlines()
    for i in a:
        b = "https://music.163.com/#/user/songs/rank?id=" + i
        driver = webdriver.Chrome()
        driver.get(b)
        driver.switch_to_frame('g_iframe')
        try:
            wait = ui.WebDriverWait(driver, 15)
            if wait.until(lambda driver: driver.find_element_by_class_name('g-bd')):
                print('success!')
                data += driver.find_element_by_id('rHeader').find_element_by_tag_name('h4').text + '\n'
                #print(data)
                lists = driver.find_element_by_class_name('m-record').find_elements_by_tag_name('li')
                print(len(lists))
                for l in lists:
                    temp = '歌曲名：' + l.find_element_by_tag_name('b').text + ' 歌手：' + l.find_element_by_class_name(
                        's-fc8').text.replace('-', '') + ' 频率：' + l.find_element_by_class_name('bg').get_attribute('style')
                    print(temp)  # 解析出歌名 歌手 频率
                    data += temp + '\n'

        finally:
            driver.quit()