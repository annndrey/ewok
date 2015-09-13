# encoding: utf-8
from django.shortcuts import render, HttpResponseRedirect
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect
from .forms import RegisterForm

@cache_page(3600 * 4)
@csrf_protect
def index(request):
    if request.method == 'POST':
        print request.POST
        return HttpResponseRedirect("/tests/")
    elif request.method == 'GET':
        return render(request, 'register.html', form=RegisterForm)
