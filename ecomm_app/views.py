from django.shortcuts import render
from .models import Products
import os

def index(request):

    settings_dir = os.path.dirname(__file__)
    PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir))    
    print(PROJECT_ROOT)
    context={
        "product_all":Products.objects.all()
    }
    return render (request,"ecomm_app/index.html",context)


