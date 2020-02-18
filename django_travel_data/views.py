from django.shortcuts import render
import requests
from analyse_data import Process
from django.http import HttpResponse


def button(request):

    return render(request, 'home.html')


def output1(request):

    df = Process.load_data()
    q1 = Process.avg_time_lhr_dxb(df)

    return render(request, 'home.html', {'data1': q1})


def output2(request):

    df = Process.load_data()
    q2 = Process.max_departs_man(df)

    return render(request, 'home.html', {'data2': q2})


def output3(request):

    df = Process.load_data()
    q3 = Process.combined_business_proportion(df)

    return render(request, 'home.html', {'data3': q3})


def output4(request):

    df = Process.load_data()
    q4 = Process.flights_to_sweden(df)

    return render(request, 'home.html', {'data4': q4})


def output5(request):

    df = Process.load_data()
    q5 = Process.most_common_carrier(df)

    return render(request, 'home.html', {'data5': q5})
