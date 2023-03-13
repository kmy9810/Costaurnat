from django.shortcuts import render
from django.http import HttpResponse, Http404
from datetime import datetime
from foods.models import Menu

# Create your views here.
#장고 앱의 메인 로직 처리와 관련된 파일

def index(request):
    context = dict()
    today = datetime.today().date()
    menus = Menu.objects.all()
    context["date"] = today #사전형으로 보내버리기!
    context["menus"] = menus
    return render(request, 'foods/index.html', context=context)

def food_detail(request, pk):
    context = dict()
    menu = Menu.objects.get(id=pk)
    context["menu"] = menu
    return render(request, 'foods/detail.html', context=context)