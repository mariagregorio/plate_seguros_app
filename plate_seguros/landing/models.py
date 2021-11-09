from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator


class QuienesSomos(models.Model):
    titulo = models.CharField(max_length=250)
    contenido = models.TextField()
    imagen = models.ImageField(default=None, null=True, blank=True, upload_to='images')

    def save(self, *args, **kwargs):
        if not self.pk and QuienesSomos.objects.exists():
            raise ValidationError('Solo puede haber una instancia de Quienes Somos')
        return super(QuienesSomos, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Quienes Somos'
        verbose_name_plural = 'Quienes Somos'


class SegurosEncabezado(models.Model):
    titulo = models.CharField(max_length=250)
    subtitulo = models.CharField(max_length=250)

    def save(self, *args, **kwargs):
        if not self.pk and SegurosEncabezado.objects.exists():
            raise ValidationError('Solo puede haber una instancia de Seguros Encabezado')
        return super(SegurosEncabezado, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo
        
    class Meta:
        verbose_name = 'Seguros Encabezado'
        verbose_name_plural = 'Seguros Encabezado'


class Seguro(models.Model):
    icono = models.ImageField(upload_to='images')
    titulo = models.CharField(max_length=250)
    contenido = models.TextField()
    posicion = models.IntegerField(default=None, null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(50)])

    def __str__(self):
        return self.titulo


class Home(models.Model):
    titulo = models.CharField(max_length=250)
    subtitulo = models.CharField(max_length=250)

    def save(self, *args, **kwargs):
        if not self.pk and Home.objects.exists():
            raise ValidationError('Solo puede haber una instancia de Home')
        return super(Home, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Home'
        verbose_name_plural = 'Home'


class Incapacidad(models.Model):
    titulo = models.CharField(max_length=250)
    contenido = models.TextField()

    def save(self, *args, **kwargs):
        if not self.pk and Incapacidad.objects.exists():
            raise ValidationError('Solo puede haber una instancia de Incapacidad')
        return super(Incapacidad, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Incapacidad'
        verbose_name_plural = 'Incapacidad'


class IncapacidadSlide(models.Model):
    imagen = models.ImageField(upload_to='images')
    posicion = models.IntegerField(default=None, null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(50)])

    def __str__(self):
        return f'{self.imagen.name} (posicion={self.posicion})'


class Aseguradora(models.Model):
    nombre = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='images')
    posicion = models.IntegerField(default=None, null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(50)])

    def __str__(self):
        return self.nombre


class Contacto(models.Model):
    titulo = models.CharField(max_length=250)
    instagram = models.CharField(max_length=250)
    facebook = models.CharField(max_length=250)
    linkedin = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    telefono1 = models.CharField(max_length=50)
    telefono2 = models.CharField(max_length=50)
    telefono3 = models.CharField(max_length=50)
    direccion = models.CharField(max_length=250)

    def save(self, *args, **kwargs):
        if not self.pk and Contacto.objects.exists():
            raise ValidationError('Solo puede haber una instancia de Contacto')
        return super(Contacto, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contacto'