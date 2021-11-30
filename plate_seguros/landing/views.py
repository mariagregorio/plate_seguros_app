from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.db.models import F
from django.core.mail import send_mail
from .models import QuienesSomos, SegurosEncabezado, Seguro, Home, Incapacidad, IncapacidadSlide, Aseguradora, Contacto
from .forms import ContactForm


def send_email_form():
    pass


def index(request): 
    home = Home.objects.get(pk=1)
    quienes_somos = QuienesSomos.objects.get(pk=1)
    seguros_encabezado = SegurosEncabezado.objects.get(pk=1)
    seguros = list(Seguro.objects.order_by(F('posicion').asc(nulls_last=True)))
    incapacidad = Incapacidad.objects.get(pk=1)
    incapacidad_slider = IncapacidadSlide.objects.order_by(F('posicion').asc(nulls_last=True))
    aseguradoras = Aseguradora.objects.order_by(F('posicion').asc(nulls_last=True))
    contacto = Contacto.objects.get(pk=1)
    contacto_alert = ''
    contacto_whatsapp = contacto.telefono3.replace(' ', '').replace('+', '')

    # agrupar de a dos para preparar para el slider en mobile
    seguros_list = []

    for i in range(len(seguros)):
        if i%2 == 0:
            try:
                seguros_list.append([seguros[i], seguros[i+1]])
            except:
                seguros_list.append([seguros[i]])

    is_contacto_post = False

    if request.method == 'POST':
        is_contacto_post = True
        contacto_form = ContactForm(request.POST)

        if contacto_form.is_valid():
            data = {
                'nombre': contacto_form.cleaned_data['nombre'],
                'email': contacto_form.cleaned_data['email'],
                'mensaje': contacto_form.cleaned_data['mensaje']
            }

            mensaje = '''
                Nombre: {}
                Email: {}
                Mensaje: {}
            '''.format(data['nombre'], data['email'], data['mensaje'])

            try:
                send_mail('Contacto de Plateseguros.com', mensaje, 'contacto@plateseguros.com', ['contacto@plateseguros.com'])
                contacto_alert = 'Mensaje enviado. Muchas gracias!'
            except:
                contacto_alert = 'Lo lamentamos, su mensaje no pudo ser enviado.'
            
            contacto_form = ContactForm()

    else:
        contacto_form = ContactForm()


    return render(request, 'landing/index.html', {
        'home': home,
        'quienes_somos': quienes_somos,
        'seguros_encabezado': seguros_encabezado,
        'seguros': seguros_list,
        'incapacidad': incapacidad,
        'incapacidad_slider': incapacidad_slider,
        'aseguradoras': aseguradoras,
        'contacto': contacto,
        'contacto_form': contacto_form,
        'contacto_alert': contacto_alert,
        'is_contacto_post': is_contacto_post,
        'contacto_whatsapp': contacto_whatsapp
    })
