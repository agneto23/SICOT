from principal.models import Proveedor,Producto,OrdenProducto,OrdenTrabajo,Cliente,Usuario,Rol,Permiso,Categoria
from django.contrib import admin

# Register your models here.
admin.site.register(Producto)
admin.site.register(Proveedor)
admin.site.register(Categoria)
admin.site.register(OrdenTrabajo)
admin.site.register(OrdenProducto)
admin.site.register(Usuario)
admin.site.register(Cliente)
admin.site.register(Rol)
admin.site.register(Permiso)