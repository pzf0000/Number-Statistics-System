from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from datetime import date
from CountPeople.models import *
import json


def index(request):
    return HttpResponseRedirect('/login_page/')


def error(request):
    return render(request, 'error.html')


def login_page(request):
    return render(request, 'login.html')


def login(request):
    id = request.POST['id']
    pwd = request.POST['pwd']
    user_query = user.objects.filter(id=id)
    s = user_query.first()
    if user_query.count() == 0 or s.pwd != pwd:
        return HttpResponseRedirect('/error/')
    class_item = item.objects.filter(date=date.today(), user__stu_class=s.stu_class).order_by('user__stu_class__name')
    if class_item.count() == 0:
        class_item = item.objects.none()
    classes = student_class.objects.all().order_by('name')
    return render(request, 'home.html', {
        'user': s,
        'item0': class_item.first(),
        'class': classes,
        'today': date.today().isoformat()
    })


def submit(request):
    try:
        class_name = request.POST['stu_class']
        user_name = request.POST['user']
        number = request.POST['number']
        others = request.POST['others']
        stu_class = student_class.objects.get(name=class_name)
        user_submit = user.objects.get(stu_class=stu_class, name=user_name)
        item_query = item.objects.filter(user=user_submit, date=date.today())
        if item_query.count() != 0:
            item_query.update(number=number, others=others)
        else:
            item.objects.create(user=user_submit, date=date.today(), number=number, others=others)
        return render(request, 'success.html')
    except Exception as e:
        print(e)
        return render(request, 'error.html')


def change_date(request):
    date_str = request.POST['date'].split('-')
    year = int(date_str[0])
    month = int(date_str[1])
    day = int(date_str[2])
    date_request = date(year, month, day)
    items = item.objects.filter(date=date_request).order_by('user__stu_class__name')
    ret = {
        "item": [],
        "all": 0
    }
    for i in items:
        r = {}
        r['user_name'] = i.user.name
        r['user_class'] = str(i.user.stu_class)
        r['number'] = i.number
        ret['all'] += i.number
        r['others'] = i.others
        ret['item'].append(r)
    return HttpResponse(json.dumps(ret))


