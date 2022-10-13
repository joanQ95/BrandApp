from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from .models import Product
from .forms import ProductForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.decorators import login_required
# def id_product(product_id,BASE_URL):
# 	 item_list = []
# 	 item=requests.get(f"{BASE_URL}/items/{product_id}")
# 	 if item.status_code==200:
# 	 	item=item.json()
# 	 	return item.get("price")



# Create your views here.
@login_required(login_url='login')
def create_product(request):
    if request.method=="POST":
        productForm=ProductForm(request.POST)
        if productForm.is_valid():
            productForm.save()
            messages.success(request,_("Producto creado correctamente"))
        else:
            messages.error(request, _("Campo/s incorrectos"))

    else:
          productForm=ProductForm()
    return render(request, "create_product.html", {"productForm":productForm})

@login_required(login_url='login')
def product_list(request):
    product=Product.objects.filter(supervisor=request.user)
    return render(request,'list_product.html',{"product":product})
 
def borrar_product(request,id):
    prod = get_object_or_404(Product, pk=id)
    if prod:
        prod.delete()
    return redirect("product_list")    

@login_required
def edit_product(request, id):
    obj = get_object_or_404(Product, pk=id)
    if request.method == "POST" and obj:
        productForm = ProductForm(request.POST or None, instance = obj)
        if productForm.is_valid():
            productForm.save()
            messages.success(request, ('Su producto fue editado exitosamente!'))
            return redirect("product_list")
        else:
            messages.error(request, 'Ups! Al parecer hubo un error con el llenado del formulario.')
    else:
        productForm = ProductForm(instance=obj)
        
    return render(request, "edit_product.html", {'productForm':productForm})
