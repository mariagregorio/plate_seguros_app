from django.contrib import admin
from .models import QuienesSomos, SegurosEncabezado, Seguro, Home, Incapacidad, IncapacidadSlide, Aseguradora, Contacto


class QuienesSomosAdmin(admin.ModelAdmin):
    list_display = ('titulo',)

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(QuienesSomos, QuienesSomosAdmin)


class SegurosEncabezadoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'subtitulo',)

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(SegurosEncabezado, SegurosEncabezadoAdmin)


class SeguroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'posicion',)
    ordering = ['posicion']


admin.site.register(Seguro, SeguroAdmin)


class HomeAdmin(admin.ModelAdmin):
    list_display = ('titulo',)

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Home, HomeAdmin)


class IncapacidadAdmin(admin.ModelAdmin):
    list_display = ('titulo',)

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Incapacidad, IncapacidadAdmin)


class IncapacidadSlideAdmin(admin.ModelAdmin):
    ordering = ['posicion']


admin.site.register(IncapacidadSlide, IncapacidadSlideAdmin)


class AseguradoraAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'posicion',)
    ordering = ['posicion']


admin.site.register(Aseguradora, AseguradoraAdmin)


class ContactoAdmin(admin.ModelAdmin):
    list_display = ('titulo',)

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Contacto, ContactoAdmin)

admin.site.site_header = 'Plate Seguros'