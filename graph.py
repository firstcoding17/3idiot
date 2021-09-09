import pandas as pd
import matplotlib.pyplot as plt
import datetime as DT
import numpy as np
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

## 수정 예정

get_csv = pd.read_csv('user_info/User_info.csv')
cal_csv = pd.read_csv('price_list.csv')

def graph(name,date):


    safe = get_csv[get_csv['Type'] == '안정']
    nomal = get_csv[get_csv['Type'] == '중립']
    danger = get_csv[get_csv['Type'] == '적극']

    safe = pd.DataFrame(safe)
    nomal = pd.DataFrame(nomal)
    danger = pd.DataFrame(danger)

    safe.reset_index(inplace=True)
    nomal.reset_index(inplace=True)
    danger.reset_index(inplace=True)

    safe_len = len(safe)
    nomal_len = len(nomal)
    danger_len = len(danger)

    safe_money = 0.3
    nomal_money = 0.15
    danger_money = 0

    safe_bond = 0.28
    nomal_bond = 0.34
    danger_bond = 0.4

    safe_stock = 0.42
    nomal_stock = 0.51
    danger_stock = 0.6

    division = 0.16666

    load_safe = pd.read_csv('user_info/안정.csv')
    load_nomal = pd.read_csv('user_info/중립.csv')
    load_danger = pd.read_csv('user_info/적극.csv')

    positon = pd.read_csv('Postion.csv')

    get_buy = []
    P_list = [
        'KODEX 200',
        'KODEX 코스닥 150',
        'KODEX 골드선물(H)',
        'KODEX 미국S&P500선물(H)',
        'KINDEX 미국나스닥100',
        'TIGER 차이나CSI300',
        'KODEX MSCI EM선물(H)',
        'KODEX 선진국MSCI World',
        'KODEX 다우존스미국리츠(H)',
        'TIGER 유로스탁스50(합성 H)',
        'TIGER 차이나HSCEI',
        'KODEX 미국FANG플러스(H)',
        'TIGER KRX BBIG K-뉴딜',
        'TIGER MSCI KOREA ESG',
        'KBSTAR ESG 사회책임투자',
        'KODEX단기채권PLUS',
        'TIGER 미국채10년선물'
    ]

    info_safe = pd.read_csv('user_info/안정.csv')
    info_nomal = pd.read_csv('user_info/중립.csv')
    info_danger = pd.read_csv('user_info/적극.csv')


    now_time = DT.datetime.today()
    now_time.strftime("Y%m%d")

    recal_csv = cal_csv[cal_csv['Date'] == date]

    safe_list = np.array(info_safe['이름'].tolist())
    nomal_list = np.array(info_nomal['이름'].tolist())
    danger_list = np.array(info_danger['이름'].tolist())

    string_date = str(date)
    year = string_date[:4]
    month = int(string_date[5:7])
    month = '0'+str(month-1)
    total_ym = year+month




    if name in safe_list:
        set_amount = 0
        count = info_safe[info_safe['이름'] == name]
        recount = cal_csv[cal_csv['Date'] == str(date)]
        count_stock = count[count['month'] == int(total_ym)]
        for j in range(0, len(P_list)):
            set_amount += count_stock[P_list[j]] * recount[P_list[j]]
        set_amount += count_stock['cash']

        list_1 = []
        name_list=[]
        per_list = []
        for i in range(0,len(P_list)):
            if int(count_stock[P_list[i]]) == 0:
                continue
            else:
                name_list.append(P_list[i])
                list_1.append(int(count_stock[P_list[i]]) * int(recount[P_list[i]]))




        ratio = list_1
        labels = name_list

        plt.pie(ratio,labels=labels,autopct='%.1f%%')
        plt.show()





    elif name in nomal_list:
        set_amount = 0
        count = info_nomal[info_nomal['이름'] == name]
        recount = cal_csv[cal_csv['Date'] == str(date)]
        count_stock = count[count['month'] == int(total_ym)]
        for j in range(0, len(P_list)):
            set_amount += count_stock[P_list[j]] * recount[P_list[j]]
        set_amount += count_stock['cash']

        list_1 = []
        name_list = []
        per_list = []
        for i in range(0, len(P_list)):
            print()
            if int(count_stock[P_list[i]]) == 0:
                continue
            else:
                name_list.append(P_list[i])
                list_1.append(int(count_stock[P_list[i]]) * int(recount[P_list[i]]))

        ratio = list_1
        labels = name_list

        plt.pie(ratio, labels=labels, autopct='%.1f%%')
        plt.show()

    elif name in danger_list:
        set_amount = 0
        count = info_danger[info_danger['이름'] == name]
        recount = cal_csv[cal_csv['Date'] == str(date)]
        count_stock = count[count['month'] == int(total_ym)]
        for j in range(0, len(P_list)):
            set_amount += count_stock[P_list[j]] * recount[P_list[j]]
        set_amount += count_stock['cash']

        list_1 = []
        name_list = []
        per_list = []
        for i in range(0, len(P_list)):
            print()
            if int(count_stock[P_list[i]]) == 0:
                continue
            else:
                name_list.append(P_list[i])
                list_1.append(int(count_stock[P_list[i]]) * int(recount[P_list[i]]))

        ratio = list_1
        labels = name_list

        plt.pie(ratio, labels=labels, autopct='%.1f%%')
        plt.show()




