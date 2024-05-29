from django.contrib import admin
from django.contrib.admin import AdminSite
from django.http.request import HttpRequest
from backend import models

# Register your models here.
admin.site.register(models.Cliente)
# admin.site.register(models.Restaurantes)
admin.site.register(models.Productos)
# admin.site.register(models.Pedido)
admin.site.register(models.Detallespedido)
admin.site.register(models.Repartidores)
admin.site.register(models.Transferencias)
admin.site.register(models.Canastaproductos)
admin.site.register(models.Canasta)


# configuration of panel administration
class CustomAdminSite(AdminSite):
    site_title = "BlackBull"
    site_header = "BlackBull"
    index_title = "Panel de administración"


custom_site = CustomAdminSite()

admin.site.site_title = custom_site.site_title
admin.site.site_header = custom_site.site_header
admin.site.index_title = custom_site.index_title


# se pondran ver los pedidos pero no modificar los pedidos
class PedidoAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, objec=None):
        return False


admin.site.register(models.Pedido, PedidoAdmin)
# admin.site.register(PedidoAdmin)
