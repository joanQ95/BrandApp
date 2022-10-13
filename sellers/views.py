from django.http import HttpResponse,JsonResponse
import json
import urllib.request
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from .forms import SellerForm
from .models import Seller
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.decorators import login_required
from .models import Account

    


# Create your views here.
@login_required(login_url='login')
def create_seller(request):
    if request.method=="POST":
        sellerForm=SellerForm(request.POST)
        if sellerForm.is_valid():
            sellerForm.save()
           
            messages.success(request,_("Vendedor creado correctamente"))
        else:
            messages.error(request, _("Campo/s incorrectos"))
        return redirect("seller")
    sellerForm=SellerForm()
    return render(request, "create_seller.html", {"sellerForm":sellerForm})

@login_required(login_url='login')
def seller_list(request):
    seller_obj=Seller.objects.filter(supervisor=request.user)
    return render(request,'list_seller.html',{"seller_obj":seller_obj})
 


def borrar_seller(request,id):
    sel = get_object_or_404(Seller, pk=id)
    if sel:
        sel.delete()
    return redirect("seller_list")    

