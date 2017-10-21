from django.shortcuts import render
from django.http import HttpResponse
from json import dumps
from Main.models import User
from Utils.Common import Setting, ReturnValue

def test(request):

  result = ReturnValue("success", "ok", "")
  return HttpResponse(result)

def sign_up(request):

  if request.method == 'POST':
    data = request.POST
    try:
      name = data.get('name','')
      phone = data.get('phone','')
      gender = data.get('gender','')
      role = data.get('role','')
      can_share = data.get('',)
      plate = data.get('plate','')
      parking_position = data.get('parking_position','')
      user = User(phone,name,gender,role,can_share,plate,parking_position,'')
      result = ReturnValue("success", "ok", user)
    except:
      result = ReturnValue("fail", "sign up err", "")
  else:
      result = ReturnValue("fail", "please use get method", "")
  
  print(result)
  return HttpResponse(result)

def order(request):

  if request.method == 'POST':
    try:
      result = ReturnValue("success", "ok", "")
    except:
      result = ReturnValue("fail", "sign up err", "")
  else:
      result = ReturnValue("fail", "please use get method", "")

  return HttpResponse(result)