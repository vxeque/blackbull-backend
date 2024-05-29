from django.urls import path, include
from rest_framework import routers
from backend import views
from rest_framework.documentation import include_docs_urls

# cliente restaurante productos pedido detallepedido repartidores tranferencias
router = routers.DefaultRouter()
router.register(r'client', views.clientView) # cliente
# router.register(r'restaurant', views.restauranteView) # restaurantes 
router.register(r'canasta', views.canastaView)
router.register(r'products', views.productosView) # productos
router.register(r'order', views.pedidoView) # pedido
router.register(r'orderDetail', views.detallePedidoView) # detalles pedido 
router.register(r'dealers', views.repartidoresView) # repartidores 
router.register(r'transfers', views.tranferenciasView) # transferencias
router.register(r'canastaProductos', views.canastaProductosView) # canasta creada por productos
# router.register(r'notification', views.notificationView) # notificaciones

urlpatterns=[
    path('api/v1/', include(router.urls)),
    # path('api/v1/client/username/<str:username>', include(router.urls)),
    path('docs/', include_docs_urls(title='delivery+'))
]
