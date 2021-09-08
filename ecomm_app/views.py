from django.shortcuts import render
from .models import Products
import os

def index(request):

    #settings_dir = os.path.dirname(__file__)
    #PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir))    
    #print(PROJECT_ROOT)
    context={
        "product_all":Products.objects.all()
    }
    item_name= request.GET.get('item_name')
    if (item_name !='' and item_name!=None):
        context["product_all"]=Products.objects.filter(title__contains=item_name)

    
    return render (request,"ecomm_app/index.html",context)


