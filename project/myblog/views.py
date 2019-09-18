from django.shortcuts import render

from myblog.models import Myblog

def myblog_index(request):
    myblog = Myblog.objects.all()
    context = {
        'myblog': myblog
    }
    return render (request,'myblog_index.html', context)

def myblog_detail(request, pk):
    myblog = Myblog.objects.get(pk=pk)
    context = {
        'myblog': myblog
    }
    return render (request, 'myblog_detail.html', context)
    