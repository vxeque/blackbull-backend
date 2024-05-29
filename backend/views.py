from rest_framework import viewsets
from backend import serializer
from backend import models
from rest_framework.decorators import api_view

# cliente restaurante productos pedido detallepedido repartidores tranferencias


# Create your views here.
class clientView(viewsets.ModelViewSet):
    serializer_class = serializer.clientSelializer
    queryset = models.Cliente.objects.all()


class canastaView(viewsets.ModelViewSet):
    serializer_class = serializer.canastaSelializer
    queryset = models.Canasta.objects.all()


class productosView(viewsets.ModelViewSet):
    serializer_class = serializer.productosSelializer
    queryset = models.Productos.objects.all()


class pedidoView(viewsets.ModelViewSet):
    serializer_class = serializer.pedidoSelializer
    queryset = models.Pedido.objects.all()


class detallePedidoView(viewsets.ModelViewSet):
    serializer_class = serializer.detallePedidoSelializer
    queryset = models.Detallespedido.objects.all()


class repartidoresView(viewsets.ModelViewSet):
    serializer_class = serializer.repartidoresSelializer
    queryset = models.Repartidores.objects.all()


class tranferenciasView(viewsets.ModelViewSet):
    serializer_class = serializer.transferenciasSelializer
    queryset = models.Transferencias.objects.all()


class canastaProductosView(viewsets.ModelViewSet):
    serializer_class = serializer.canastaProductosSelializer
    queryset = models.Canastaproductos.objects.all()

# class notificationView(viewsets.ModelViewSet):
#     serializer_class = serializer.notificationSelializer
#     queryset = models.Notification.objects.all()
