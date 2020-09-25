from django.contrib import admin
from . import models


admin.site.register(models.Ciudad)
admin.site.register(models.Producto)
admin.site.register(models.Orden)
admin.site.register(models.Usuario)
