from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings


def formulario_contacto(request):
    return render(request, "Formulario_contacto.html")


def contactar(request):
    if request.method == "POST":
        asunto = request.POST["txtAsunto"]
        mensaje = request.POST["txtMensaje"] + " / Email: " + request.POST["txtEmail"] 
        email_desde = settings.EMAIL_HOST_USER
        email_para = ["emmanuelorozco1993@gmail.com"]
        send_mail(Asunto, mensaje, email_desde, email_para, fail_silently=False)
        return render(request, "contactoExitoso.html")
    return render(request, "Formulario_contacto.html")
    


