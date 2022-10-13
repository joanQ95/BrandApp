from django import forms 
from .models import Account

class RegisterForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder":"Ingrese Password"
    }))
    confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder":"Confirmar Password"
    }))
    class Meta:
        model=Account
        fields=["first_name","last_name","email","password"]

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs["placeholder"]="Ingrese nombre"
        self.fields["last_name"].widget.attrs["placeholder"]="Ingrese apellido"
       
        self.fields["email"].widget.attrs["placeholder"]="Ingrese email"
        for field in self.fields:
            self.fields[field].widget.attrs["class"]="form-control"
    
    # validación personalizada, capturo los datos que necesito y le aplico condicion
    def clean(self):
        cleaned_data=super(RegisterForm,self).clean()
        password=cleaned_data.get("password")
        confirm_password=cleaned_data.get("confirm_password")
        
        if password!=confirm_password:
            raise forms.ValidationError("El password no coincide!")