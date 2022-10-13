
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')), 
    path('admin/', admin.site.urls),
    path('',views.payment,name="payment"),
    # path('account/',include("accounts.urls")),
    # path('seller/',include("sellers.urls")),
    path('products/',include("products.urls")),
    # path('ven_items/',include("seller_product.urls")),
]
