from django.shortcuts import render
from .models import Products

def index(request):
    context={
        "product_all":Products.objects.all()
    }
    return render (request,"ecomm_app/index.html",context)


