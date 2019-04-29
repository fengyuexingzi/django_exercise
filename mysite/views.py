# -*- coding: utf-8 -*-
import json
from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
    print(request.GET.get('name'))
    context = {'hello': '!Hello World!'}
    return render(request, 'hello.html', context)


def post(request):
    return render(request, 'index.html')


def upload(request):
    files = request.FILES
    print(files)
    return HttpResponse(json.dumps({"success": "success"}), content_type="application/json")


def api(request):
    print(request.POST.get('name'))
    response = {
        'status': 1,
        'info': 'message from python',
        'msg': 'message from python',
        'data': [{
            'name': 'a'},
            {'name': 'b'},
            {'name': 'c'}
        ]}
    return HttpResponse(json.dumps(response), content_type="application/json")
