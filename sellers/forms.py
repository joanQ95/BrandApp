from accounts.models import Account
from .models import Seller
from django.forms import  ModelForm,CharField,EmailField,Select, IntegerField, EmailInput, NumberInput,TextInput



class SellerForm(ModelForm):
    email =EmailField(label='Email',widget=EmailInput(attrs={'type':'email' ,'class':'form-control',"placeholder":"Email del Vendedor"}))  
    phone =CharField(label='Teléfono',widget=TextInput(attrs={'class':'form-control',"placeholder":"Teléfono del Vendedor"}))  
    nickname =CharField(label='Nombre',widget=TextInput(attrs={'class':'form-control',"placeholder":"Nombre del Vendedor"}))

    
    class Meta:
        model=Seller
        fields=["nickname","email","phone","supervisor"]
        
    def __init__(self, *args, **kwargs):
        super(SellerForm, self).__init__(*args, **kwargs)
        self.fields['supervisor'].empty_label="Escoge email de quién inició sesión"
        self.fields['supervisor'].widget.attrs["class"]="form-control"
        # self.fields['products_id'].widget.attrs["class"]="form-control"