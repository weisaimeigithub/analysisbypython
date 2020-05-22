# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def layout(request):
    return render(request, 'analysisWeb/layout.html')


def analysis1(request):
    import pandas as pd
    df = pd.read_excel('D:/dataAnalysisbyPython/analysisWeb/XLS/20200501.xls')
    # df2 = pd.read_excel('D:/untitled/analysisWeb/XLS/20200502.xls')
    # 使用price均值对NA进行填充，设置一个按钮，点击前台接收不同的按钮，然后就是能够展示不同日期的数据
    data = df.fillna('*')
    readT = data.阅读时长
    # 将用户使用情况根据阅读时长进行分区：分为[5-15][15-25][25-35][35-45]
    # 设置不同的变量：readT1,readT2,readT3,readT4
    # 弄一个参数输入不同的点
    readT1 = readT2 = readT3 = readT4 = 0
    for i in range(len(readT)):
        if 5 < readT[i] < 15:
            readT1 = readT1 + 1
        elif 15 < readT[i] < 25:
            readT2 = readT2 + 1
        elif 25 < readT[i] < 35:
            readT3 = readT3 + 1
        elif 35 < readT[i] < 45:
            readT4 = readT4 + 1
    read_list = [readT1, readT2, readT3, readT4]
    key_list = ["15-45(min)", "45-75(min)", "75-105(min)", "105-135(min)"]
    dict_list = dict(zip(key_list, read_list))
    return render(request, 'analysisWeb/analysis1.html',
                  {"key_list": key_list, "read_list": read_list, "dict_list": dict_list})
