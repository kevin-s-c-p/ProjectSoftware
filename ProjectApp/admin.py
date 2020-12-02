from django.contrib import admin
from .models import archivos

# Register your models here.

class archivosAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha',)

admin.site.register(archivos,archivosAdmin)