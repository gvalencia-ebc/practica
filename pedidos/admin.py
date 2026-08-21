from django.contrib import admin

# Register your models here.
from .models import Producto, Pedido

admin.site.site_header = "Admon Cafeteria La Cucaracha Risueña"
admin.site.site_title = "Panel Cafeteria La Cucaracha Risueña"
admin.site.index_title = "Panel de Administración"

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','precio','categoria','disponible')
    list_filter = ('categoria','disponible')
    search_fields = ('nombre',)

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id','cliente_nombre','estado','total','fecha')
    list_filter = ('estado','fecha')
    search_fields = ('cliente_nombre',)