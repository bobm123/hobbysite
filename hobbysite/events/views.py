from django.http import HttpResponse
from django.shortcuts import redirect, render

import datetime

from events.models import Event

mnames = "January February March April May June July August September October November December"
mnames = mnames.split()


def home_page(request):
    return render(request, 'home.html', {'nbar': 'home'})


def view_events(request):
    startdate = datetime.datetime.now()
    months_ = month_rages()
    events_by_month = []
    for m in months_:
        month_tuple = (m[0], Event.objects.filter(date__range=[m[1], m[2]]))
        events_by_month.append(month_tuple)
    return render(request, 'events.html', {
        'nbar': 'events',
        'events_by_month': events_by_month})


def month_rages():
    startdate = datetime.date.today()
    startdate = startdate.replace(day=1)
    month_list = []
    for m in range(0,12):
        enddate = next_month(startdate)
        month_list.append((mnames[startdate.month-1], startdate, enddate))
        startdate = enddate

    return month_list


def next_month(somedate):
    next_month = somedate.month+1
    if next_month > 12:
        next_month = next_month - 12
        return(somedate.replace(day=1, month=next_month, year=somedate.year+1))
    else:
        return(somedate.replace(day=1, month=next_month))