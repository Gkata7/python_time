from django.shortcuts import render
import datetime

def index(request):
    context = {
        "time" :datetime.datetime.now()
    }
    return render(request,'displayTime/index.html', context)
