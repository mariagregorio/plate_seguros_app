from django.shortcuts import render
from django.db.models import F
from .models import QuienesSomos, SegurosEncabezado, Seguro, Home, Incapacidad, IncapacidadSlide, Aseguradora, Contacto


def index(request): 
    home = Home.objects.get(pk=1)
    quienes_somos = QuienesSomos.objects.get(pk=1)
    seguros_encabezado = SegurosEncabezado.objects.get(pk=1)
    seguros = list(Seguro.objects.order_by(F('posicion').asc(nulls_last=True)))
    incapacidad = Incapacidad.objects.get(pk=1)
    incapacidad_slider = IncapacidadSlide.objects.order_by(F('posicion').asc(nulls_last=True))
    aseguradoras = Aseguradora.objects.order_by(F('posicion').asc(nulls_last=True))
    contacto = Contacto.objects.get(pk=1)

    # agrupar de a dos para preparar para el slider en mobile
    seguros_list = []

    for i in range(len(seguros)):
        if i%2 == 0:
            try:
                seguros_list.append([seguros[i], seguros[i+1]])
            except:
                seguros_list.append([seguros[i]])

    return render(request, 'landing/index.html', {
        'home': home,
        'quienes_somos': quienes_somos,
        'seguros_encabezado': seguros_encabezado,
        'seguros': seguros_list,
        'incapacidad': incapacidad,
        'incapacidad_slider': incapacidad_slider,
        'aseguradoras': aseguradoras,
        'contacto': contacto
    })
