from django.shortcuts import render
from .models import Products
import os
from django.core.paginator import Paginator

def index(request):

    #settings_dir = os.path.dirname(__file__)
    #PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir))    
    #print(PROJECT_ROOT)
    ################## SEARCH CODE ############################
    context={
        "product_all":Products.objects.all()
    }
    item_name= request.GET.get('item_name')
    if (item_name !='' and item_name!=None):
        context["product_all"]=Products.objects.filter(title__contains=item_name)

    ################### PAGINATOR CODE #########################
    paginator= Paginator(context["product_all"],4)
    page= request.GET.get('page')
    context["product_all"]= paginator.get_page(page)
    return render (request,"ecomm_app/index.html",context)

    ########### code for displaying detail of item ###########
def detail(request,id):
    context={
        "product_object": Products.objects.get(id=id)
        }
    return render (request,"ecomm_app/detail.html",context)


