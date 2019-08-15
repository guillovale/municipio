from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Empleado

from .models import Tipo

from .models import Permiso

admin.site.register(Empleado)
admin.site.register(Tipo)
admin.site.register(Permiso)
