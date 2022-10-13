from django.forms import  ModelForm,CharField,EmailField, IntegerField, EmailInput, NumberInput,TextInput
from .models import Product

class ProductForm(ModelForm):
    pvp=IntegerField(label='Precio',widget=TextInput(attrs={'min':0, 'value':0,'type':'number','class':'form-control'}))  
    discount=IntegerField(label='Descuento',widget=TextInput(attrs={'min':0, 'value':0,'type':'number','class':'form-control'}))  
    brand=CharField(label='Marca',widget=TextInput(attrs={'class':'form-control',"placeholder":"Marca del Producto"}))
    title=CharField(label='Título',widget=TextInput(attrs={ 'class':'form-control',"placeholder":"Título del Producto"}))

    class Meta:
        model=Product
        fields=["title","brand","pvp","discount","supervisor"]
       
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['supervisor'].empty_label="Escoge email de quién inició sesión"
        self.fields['supervisor'].widget.attrs["class"]="form-control"   