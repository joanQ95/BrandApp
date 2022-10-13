from django.db import models
from accounts.models import Account
from sellers.models import Seller

# Create your models here.
class Product(models.Model):
    supervisor=models.ForeignKey(Account,on_delete=models.SET_NULL, null=True)
    title=models.CharField(max_length=255,null=False)
    brand=models.CharField(max_length=255,null=False)
    pvp=models.IntegerField(default=0)
    discount=models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)
    

     #  nombre con que figura en /admin
    class Meta:
        verbose_name="product"
        verbose_name_plural="products"
        
        
    def __str__(self):
        return self.title
    
    
    