from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
def contacto(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            #Datos ingresados correctamente...
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            message = request.POST.get('message','')
            
            #Crear el email
            email = EmailMessage(
                "Rapidos y sabrosos: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribió:\n\n{}".format(name,email,message),
                "no-contestar@inbox.mailtrap.io",
                ["ch.mesina@alumnos.duoc.cl"],
                reply_to=[email]
            )

            #Enviamos el email y redireccionamos
            try:
                email.send()
                return redirect(reverse('contacto') + "?OK")
            except:
                return redirect(reverse('contacto') + "?FAIL")            

    return render(request,"contacto/contacto.html",{'form':contact_form})