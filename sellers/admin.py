from django.contrib import admin
from .models import Seller
# Register your models here.
class SellerAdmin(admin.ModelAdmin):
    list_display = ( 'nickname', 'email','phone')

admin.site.register(Seller, SellerAdmin)
