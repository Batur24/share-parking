
from django.shortcuts import render_to_response

def page(request):
  return render_to_response("page.html")

def vue(request):
  return render_to_response("Parking/dist/index.html")
