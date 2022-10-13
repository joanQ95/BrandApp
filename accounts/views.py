from email.message import EmailMessage
from django.shortcuts import render,redirect
from .forms import RegisterForm
from .models import Account
from django.contrib import messages,auth
from django.contrib.auth.models import auth

from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from django.utils.translation import gettext_lazy as _

# Create your views here.
def register(request):
    registerForm=RegisterForm()
    if request.method=="POST":
        registerForm=RegisterForm(request.POST)
        if registerForm.is_valid():
            # capturo los valores
            first_name=registerForm.cleaned_data["first_name"]
            last_name=registerForm.cleaned_data["last_name"]
          
            email=registerForm.cleaned_data["email"]
            password=registerForm.cleaned_data["password"]
            username=email.split("@")[0]
            user=Account.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password)
            
            user.save()
            
            # sition actual
            current_site=get_current_site(request)
            mail_subject=_("Por favor activa tu cuenta en BrandProteccion")
            body=render_to_string('account/account_verification_email.html',{
                 'user':user,
                 'domain':current_site,
                # cifrado
                 'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                 'token':default_token_generator.make_token(user),
             })
            to_email=email
            send_email=EmailMessage(mail_subject,body,to=[to_email])
            send_email.send()
            
            
            # messages.success(request,"El usuario se registro correctamente")
            # return redirect("register")
            return redirect('/account/login/?command=verification&email='+email)
    return render(request,'account/register.html',{"registerForm":registerForm})

def login(request):
    if request.method=="POST":
        email=request.POST["email"]
        password=request.POST["password"]
        
        user=auth.authenticate(email=email,password=password)

        if user is not None:
            auth.login(request,user)
            messages.success(request,_("Has iniciado sesión correctamente"))
            return redirect("login")
        else:
            messages.error(request,_("Las credenciales son incorrectas"))
            return redirect("login")
        
    return render(request,'account/login.html')

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request,_("Cerraste sesión"))
    return redirect("login")

def activate(request,uidb64,token):
    try:
        uid=urlsafe_base64_decode(uidb64).decode()
        user=Account._default_manager.get(pk=uid)
    except(TypeError,ValueError,OverflowError,Account.DoesNotExist):
        user=None
        
    if user is not None and default_token_generator.check_token(user,token):
        user.is_active=True
        user.save()
        messages.success(request, _("Felicidades, tu cuenta está activa"))
        return redirect("login")
    else:
        messages.error(request,_("La activación es inválida"))
        return redirect("register")
        
        
# @login_required(login_url='login')
def dashboard(request):
    return render(request,'account/dashboard.html')



def forgotPassword(request):
    if request.method=="POST":
        email=request.POST["email"]
        if Account.objects.filter(email=email).exists():
            user=Account.objects.get(email__exact=email)
            
            current_site=get_current_site(request)
            mail_subject=_("Resetear password en BrandProteccion")
            body=render_to_string('account/reset_password_email.html',{
                 'user':user,
                 'domain':current_site,
                # cifrado
                 'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                 'token':default_token_generator.make_token(user),
             })
            to_email=email
            send_email=EmailMessage(mail_subject,body,to=[to_email])
            send_email.send()
            
            messages.success(request,_("Un email fue enviado a tu correo para resetear tu password"))
            return redirect("login")
        else:
            messages.error(request,_("La cuenta de usuario no existe"))
            return redirect('forgot')
        
    return render(request,'account/forgot.html')


def resetPassword_valida(request,uidb64,token):
    try:
        uid=urlsafe_base64_decode(uidb64).decode()
        user=Account._default_manager.get(pk=uid)
    except(TypeError,ValueError,OverflowError,Account.DoesNotExist):
        user=None
        
    if user is not None and default_token_generator.check_token(user,token):
        request.session['uid']=uid
        messages.success(request,_("Por favor, resetea tu password"))
        return redirect("resetPassword")
    else:
        messages.error(request,_("El link ha expirado"))
        return redirect("login")
    
def resetPassword(request):
    if request.method=="POST":
        password=request.POST["password"]
        confirm_password=request.POST['confirm_password']
        
        if password == confirm_password:
            uid=request.session.get('uid')
            user=Account.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request,_("El password se reseteó correctamente"))
            return redirect("login")
        else:
            messages.error(request,_("El password de confirmación no concuerda"))
            return redirect("resetPassword")
    else:
        return render(request,"account/resetPassword.html")