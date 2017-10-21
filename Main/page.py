
from django.shortcuts import render_to_response

def page(request):
  return render_to_response("page.html")

def order_info(request):
  print("wtf")
  return render_to_response("Parking/dist/index.html")
