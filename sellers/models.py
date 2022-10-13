from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from accounts.models import Account
# Create your models here.
class Seller(models.Model):
    supervisor = models.ForeignKey(Account ,on_delete=models.SET_NULL, null=True)
    nickname = models.CharField(max_length=100, unique=True)
    phone = PhoneNumberField()
    email = models.EmailField(max_length=255, unique=True)
    products_id = models.CharField(max_length=200)
    #  nombre con que figura en /admin
    class Meta:
        verbose_name = 'seller'
        verbose_name_plural = 'sellers'
    
    def  __str__(self):
        return self.nickname