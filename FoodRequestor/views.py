from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def index(request):
    context = {}
    # template = loader.get_template('FoodRequestor/index.html')
    # return HttpResponse(template.render(context,request))
    return render(request,'FoodRequestor/LoginPage.html',context)