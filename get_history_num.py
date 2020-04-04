#coding=utf-8
# 源链接：https://blog.csdn.net/love_bb/article/details/81223432
# 少许改动适应本项目需要
import io
import linecache
import Random_sampling

from requests import get
from bs4 import BeautifulSoup
from user_agent import generate_user_agent
import time

def request_content(start, end):
    url_link = 'https://datachart.500.com/ssq/history/newinc/history.php?start={0}&end={1}'.format(start, end)
    headers = {
        'User-Agent': generate_user_agent(device_type='desktop', os=('mac', 'linux', 'win', 'android'))
    }
    response = get(url_link, headers=headers, timeout=6)
    page_content = BeautifulSoup(response.content, "html.parser")
    html_tag = page_content.find_all('tbody', id='tdata')[0]
    return html_tag.find_all('tr', 't_tr1')


class ssqclazz:
    def __init__(self):
        self.period = ''  # 期号
        self.red_1 = ''  # 红球
        self.red_2 = ''
        self.red_3 = ''
        self.red_4 = ''
        self.red_5 = ''
        self.red_6 = ''
        self.blue_1 = ''  # 蓝球

    def __str__(self):
        return '{0} {1} {2} {3} {4} {5} {6} {7}'.format(self.period, self.red_1,self.red_2, self.red_3,self.red_4, self.red_5,self.red_6,self.blue_1)

    def tr_tag(self, tag):
        tds = tag.find_all('td')
        index = 0
        self.period = tds[index].string
        index += 1
        self.red_1 = tds[index].string
        index += 1
        self.red_2 = tds[index].string
        index += 1
        self.red_3 = tds[index].string
        index += 1
        self.red_4 = tds[index].string
        index += 1
        self.red_5 = tds[index].string
        index += 1
        self.red_6 = tds[index].string
        index += 1
        self.blue_1 = tds[index].string


def get_history_data():
    count = len(open('ssq.txt', 'r').readlines())
    list_ssq_qh = [] #期号
    for i in range(1,count+1):
        ssq_line = linecache.getline('ssq.txt', i)
        num = ssq_line[0]+ssq_line[1]+ssq_line[2]+ssq_line[3]+ssq_line[4]
        list_ssq_qh.append(int(num))
    before_num = max(list_ssq_qh) #取文件中最大的期号
    file = io.open('ssq.txt', mode='w', encoding='utf-8')
    localtime = time.localtime(time.time())
    lyear = localtime.tm_year
    ymin = 20  # 开始年份
    ymax = lyear - 2000
    print('===抓取数据开始===，20%s-20%s' % (ymin, ymax))
    file.truncate()
    for year in range(ymin, ymax + 1):
        start = before_num
        end = '{0}300'.format(year)
        trs = request_content(start, end)
        for tr in trs:
            ssqobj = ssqclazz()
            ssqobj.tr_tag(tr)
            objstr = ssqobj.__str__()
            file.write(objstr)
            file.write('\n')
            print(objstr)
        print()
        time.sleep(1)
    file.close()
    print('抓取完毕！！！')
    Random_sampling.clean_data()
    file1 = open('now_data.txt', mode='w', encoding='utf-8')
    sum = 0
    for i in range(1,17):
        bull_ball_path = 'data/' + str(i) + '.txt'
        count = len(open(bull_ball_path, 'r').readlines())
        sum = sum +count
    file1.write(str(sum))
    file1.close()
    return sum
if __name__ == '__main__':
    get_history_data()