from selenium import webdriver
import selenium.webdriver.support.ui as ui

#文件输出位置 需要修改
destination = "song.txt"
#id.txt 文件的位置 需要修改
inputpath = "id3.txt"

data = ''  # 用来保存数据
dic = {}   #保存听歌信息
count = 0
with open(inputpath, "r") as f:
    with open(destination, 'a', newline='', encoding='utf_8_sig') as fw:
        a = f.readlines()
        for i in a:
            if i.strip() == "":
                continue
            b = "https://music.163.com/#/user/songs/rank?id=" + i
            driver = webdriver.Chrome()
            driver.get(b)
            driver.switch_to_frame('g_iframe')
            try:
                wait = ui.WebDriverWait(driver, 15)
                if wait.until(lambda driver: driver.find_element_by_class_name('g-bd')):
                    print("--------id为 {} 的用户歌曲分析开始--------".format(i.strip()))
                    #data += driver.find_element_by_id('rHeader').find_element_by_tag_name('h4').text + '\n'
                    fw.write("id :{} 的数据：{}".format(str(i.strip()),
                                                    driver.find_element_by_id('rHeader').find_element_by_tag_name('h4').text + '\n'))
                    lists = driver.find_element_by_class_name('m-record').find_elements_by_tag_name('li')
                    size = len(lists)
                    if size == 0:
                        print("id为 {} 的用户设置隐私不可见,无法获取数据".format(str(i.strip())))
                    else:
                        print("id为{}的用户数据如下 {} 条:".format(str(i.strip()), str(size)))
                    for l in lists:
                        songname = str(l.find_element_by_tag_name('b').text)
                        count += 1
                        if songname in dic.keys():
                            num = dic[songname]
                            dic[songname] = num + 1
                        else:
                            dic[songname] = 1
                        temp = '歌曲名：' + songname + ' 歌手：' + l.find_element_by_class_name(
                            's-fc8').text.replace('-', '') + ' 频率：' + l.find_element_by_class_name('bg').get_attribute('style')
                        print(temp)  # 解析出歌名 歌手 频率
                        fw.write(temp+"\n")
                        #data += temp + '\n'
                    print("--------id为 {} 的用户歌曲分析结束--------".format(str(i.strip())))
                    print("\n\n")
                    fw.write("\n\n")
            finally:
                driver.quit()
    fw.close()
f.close()
print("以下为分析结果：")
reslist = sorted(dic.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
print(reslist)
print("一共收集到 "+str(count)+" 歌曲")
print("歌曲排行第一名： "+reslist[0][0])
print("歌曲排行第二名： "+reslist[1][0])
print("歌曲排行第三名： "+reslist[2][0])
