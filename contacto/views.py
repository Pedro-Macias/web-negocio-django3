from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactoForm
# Create your views here.

def contact(request):
    contacto_form = ContactoForm()
    if request.method =='POST':
        contacto_form= ContactoForm(data=request.POST)
        if contacto_form.is_valid():
            nombre = request.POST.get('nombre','')
            email = request.POST.get('email','')
            contenido = request.POST.get('contenido','')
            # enviar el correo electronico y redireccionamos mensaje de confirmacion
            email = EmailMessage(
                'Mundo Maya: Nuevo mensaje de contacto',
                'de {} <{}>\n\nEscribio:\n\n{}'.format(nombre, email, contenido),
                'no-contestar@inbox.mailtrap.io',
                ['pedro@pedro.com'],
                reply_to=[email]
            )
            # enviar el mail
            try:
                email.send()
                return redirect(reverse('contact')+'?ok')
            except:
                # algo falla
                return redirect(reverse('contact')+'?fail')    
            
    return render(request, "contacto/contact.html",{'form':contacto_form})