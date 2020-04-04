import random
import linecache

def random_sampling ():
    bull_ball = random.randint(1, 16) #抽蓝球
    bull_ball_path = 'data/' + str(bull_ball) + '.txt'  # 蓝球的文件路径
    count = len(open(bull_ball_path, 'r').readlines())
    red_ball = random.randint(1, count) #抽红球
    red_ball_line = linecache.getline(bull_ball_path, red_ball)#抽取文件中的一行作为开奖
    list_num = change_to_list(red_ball_line)#开奖结果
    if bull_ball<10:
        list_num.append('0'+str(bull_ball))
    if bull_ball>=10:
        list_num.append(str(bull_ball))
    print ('抽取结果是：',list_num)
    return list_num

def change_to_list(red_ball_line):
    list_num = []  # 开奖结果
    for i in range(2, 28, 5) :
        j = str(red_ball_line[i])
        if j == '1'or j == '2'or j == '3'or j == '4'or j == '5'or j == '6'or j == '7'or j == '8'or j == '9':j='0'+j
        elif j =='0':j='10'
        elif j =='A':j='11'
        elif j =='B':j='12'
        elif j =='C':j='13'
        elif j =='D':j='14'
        elif j =='E':j='15'
        elif j =='F':j='16'
        elif j =='G':j='17'
        elif j =='H':j='18'
        elif j =='I':j='19'
        elif j =='J':j='20'
        elif j =='K':j='21'
        elif j =='L':j='22'
        elif j =='M':j='23'
        elif j =='N':j='24'
        elif j =='O':j='25'
        elif j =='P':j='26'
        elif j =='Q':j='27'
        elif j =='R':j='28'
        elif j =='S':j='29'
        elif j =='T':j='30'
        elif j =='U':j='31'
        elif j =='V':j='32'
        elif j =='W':j='33'
        list_num.append(j)
    return list_num

def change_to_data(m):
    if m == '01': n = '1'
    elif m == '02':n = '2'
    elif m == '03':n = '3'
    elif m == '04':n = '4'
    elif m == '05':n = '5'
    elif m == '06':n = '6'
    elif m == '07':n = '7'
    elif m == '08':n = '8'
    elif m == '09':n = '9'
    elif m == '10':n = '0'
    elif m == '11':n = 'A'
    elif m == '12':n = 'B'
    elif m == '13':n = 'C'
    elif m == '14':n = 'D'
    elif m == '15':n = 'E'
    elif m == '16':n = 'F'
    elif m == '17':n = 'G'
    elif m == '18':n = 'H'
    elif m == '19':n = 'I'
    elif m == '20':n = 'J'
    elif m == '21':n = 'K'
    elif m == '22':n = 'L'
    elif m == '23':n = 'M'
    elif m == '24':n = 'N'
    elif m == '25':n = 'O'
    elif m == '26':n = 'P'
    elif m == '27':n = 'Q'
    elif m == '28':n = 'R'
    elif m == '29':n = 'S'
    elif m == '30':n = 'T'
    elif m == '31':n = 'U'
    elif m == '32':n = 'V'
    elif m == '33':n = 'W'
    return n

def clean_data ():
    count = len(open('ssq.txt', 'r').readlines()) #打开历史开奖数据
    num = 0 #计数器
    for i in range(1, count+1): #对文件每一行循环
        read_history_line = linecache.getline('ssq.txt', i) #抽取某一行
        red = [] #历史开奖号码
        for j in range(6,24 ,3): #取出历史红球
            m = read_history_line[j]+read_history_line[j+1] #红球
            n =change_to_data(m) #转换格式
            red.append(n) #组装
        str_bull = read_history_line[24]+read_history_line[25] #历史的蓝球
        bull_ball = int(str_bull) #去0操作
        bull_ball_path = 'data/'+str(bull_ball)+'.txt' #蓝球的文件路径
        print("此次从这个文件删除：",bull_ball_path)
        red_s = str(red)
        red_s = red_s.replace('[','(')
        red_s = red_s.replace(']', ')')
        print("删除这个：",red_s)

        count_data1 = len(open(bull_ball_path, 'r').readlines())
        with open(bull_ball_path, 'r') as r:
            lines = r.readlines()
        with open(bull_ball_path, 'w') as w:
            for l in lines:
                if red_s not in l:
                    w.write(l)
        count_data2 = len(open(bull_ball_path, 'r').readlines())
        if count_data1 == count_data2:
            print("没删")
        if count_data1 != count_data2:
            print("删除一条")
            num = num+1
            print("已经删除了",num)
    print('删除的条数',num)
    print('现有开奖条数：', count)

if __name__ == "__main__":
    random_sampling()
