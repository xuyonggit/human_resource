from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

"""
信用中心
"""
def index(request):
    return render(request, "Reputation.html")
