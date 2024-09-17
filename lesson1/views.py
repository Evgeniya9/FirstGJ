from django.shortcuts import render
from django.http import HttpResponse
import datetime
import os


def home_view(request):
    return render(request, 'app/home.html')


def current_time_view(request):
    now = datetime.datetime.now()
    html = f"<html><body>Текущее время: {now}</body></html>"
    return HttpResponse(html)


def workdir_view(request):
    dir_contents = os.listdir()
    html = "<html><body>Содержимое рабочей директории:<br>"
    for item in dir_contents:
        html += f"{item}<br>"
    html += "</body></html>"
    return HttpResponse(html)