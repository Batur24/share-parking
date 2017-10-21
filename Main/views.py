from django.shortcuts import render
from django.http import HttpResponse
from json import dumps
from Main.models import User, Order
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
      user.save()
      result = ReturnValue("success", "ok", user)
    except:
      result = ReturnValue("fail", "sign up err", "")
  else:
      result = ReturnValue("fail", "please use get method", "")
  
  print(result)
  return HttpResponse(result)

def order(request):

  if request.method == 'POST':
    data = request.POST
    try:
      parking_owner = data.get('parking_owner', '')
      car_owner = data.get('car_owner', '')
      start_position = data.get('car_owner', '')
      target_position = data.get('target_owner', '')
      charge = data.get('charge', '')
      finished = data.get('finished', '')
      order = Order(parking_owner, car_owner, start_position, target_position, charge,finished)
      order.save()
      result = ReturnValue("success", "ok", "")
    except:
      result = ReturnValue("fail", "sign up err", "")
  else:
      result = ReturnValue("fail", "please use get method", "")

  return HttpResponse(result)

def find_parking(request):
  recommand_parking = ['22.3590822: 114.1321027','23.2590822: 114.1321027','24.2590822: 114.1321027']
  return HttpResponse(dumps(recommand_parking))