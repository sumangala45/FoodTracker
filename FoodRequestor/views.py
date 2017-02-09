from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from models import RegisteredUser

def index(request):
    context = {}
    # template = loader.get_template('FoodRequestor/index.html')
    # return HttpResponse(template.render(context,request))
    return render(request, 'FoodRequestor/RegisterPage.html', context)

def login_page(request):
    return render(request, 'FoodRequestor/LoginPage.html', {})

def save_register_details(request):
    reg_obj = RegisteredUser()
    document = request.POST
    reg_obj.reg_name = document['name']
    reg_obj.reg_email = document['mailid']
    reg_obj.reg_uid = document['userid']
    reg_obj.reg_pwd = document['rpwd']
    reg_obj.reg_contact_no = document['contact']
    reg_obj.reg_description = document['desp']
    reg_obj.reg_location = document['autocomplete']
    reg_obj.save()
    return render(request, 'FoodRequestor/RegisterPage.html', {})

def validate_login_page(request):
    print "inside------->>> LOGIN"
    document = request.POST
    uid = document['userid']
    pwd = document['password']
    db_values = RegisteredUser.objects.filter(reg_uid=uid).values_list('reg_uid','reg_pwd','reg_name')
    print "db_values-",db_values

    if len(db_values) == 1 and db_values[0][1] == pwd and db_values[0][0] == uid:
        context = {'status': True, 'name':db_values[0][2]}
    else:
        context = {'status': False, 'name': db_values[0][2]}

    return render(request, 'FoodRequestor/index.html', context)
