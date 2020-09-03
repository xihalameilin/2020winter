# encoding:utf-8


def get_content(path):
    with open(path, 'r', encoding='gbk', errors='ignore') as f:
        content = ''
        for l in f:
            l = l.strip()
            content += l
        return content


def get_TF(words, topK=10):
    tf_dic = {}
    for w in words:
        tf_dic[w] = tf_dic.get(w, 0)+1;
    return sorted(tf_dic.items(), key=lambda x:x[1],reverse= True)[:topK]

def stop_words(path):
    with open(path,encoding='UTF-8') as reader:
        return [l.strip() for l in reader]
def main():

    import glob
    import random
    import jieba

    ##files = glob.glob('./data/news/c000013/*.txt')
    ##corpus = [get_content(x) for x in files]
    ##sample_inx = random.randint(0,len(corpus))
    content = '中国卫生部官员24日说，截至2005年底，中国各地报告的尘肺病病人累计已超过60万例，职业病整体防治形势严峻。卫生部副部长陈啸宏在当日举行的“国家职业卫生示范企业授牌暨企业职业卫生交流大会”上说，中国各类急性职业中毒事故每年发生200多起，上千人中毒，直接经济损失达上百亿元。职业病病人总量大、发病率较高、经济损失大、影响恶劣。卫生部24日公布，2005年卫生部共收到全国30个省、自治区、直辖市(不包括西藏、港、澳、台)各类职业病报告12212例，其中尘肺病病例报告9173例，占75．11%。陈啸宏说，矽肺和煤工尘肺是中国最主要的尘肺病，且尘肺病发病工龄在缩短。去年报告的尘肺病病人中最短接尘时间不足三个月，平均发病年龄40．9岁，最小发病年龄20岁。陈啸宏表示，政府部门执法不严、监督不力，企业生产水平不高、技术设备落后等是职业卫生问题严重的原因。“但更重要的原因是有些企业法制观念淡薄，社会责任严重缺位，缺乏维护职工健康的强烈的意识，职工的合法权益不能得到有效的保障。”他说。为提高企业对职业卫生工作的重视，卫生部、国家安全生产监督管理总局和中华全国总工会24日在京评选出56家国家级职业卫生工作示范企业，希望这些企业为社会推广职业病防治经验，促使其他企业作好职业卫生工作，保护劳动者健康'
    print(1)
    split_words = list(jieba.cut(content))
    split_words = [x for x in split_words if x not in stop_words('./exception')]
    print('分词效果：'+'/'.join(split_words))
    print('top10:'+str(get_TF(split_words)))

main()