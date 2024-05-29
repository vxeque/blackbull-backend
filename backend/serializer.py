from rest_framework import serializers
from backend import models

# cliente restaurante productos pedido detallepedido repartidores tranferencias
class clientSelializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cliente
        fields = '__all__'

class canastaSelializer(serializers.ModelSerializer):
    class Meta:
        model = models.Canasta
        fields = '__all__'

class productosSelializer(serializers.ModelSerializer):
    class Meta:
        model = models.Productos
        fields = '__all__'

class pedidoSelializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pedido
        fields = '__all__'

class detallePedidoSelializer(serializers.ModelSerializer):
    class Meta:
        model = models.Detallespedido
        fields = '__all__'

class canastaProductosSelializer(serializers.ModelSerializer):
    class Meta:
        model = models.Canastaproductos
        fields = '__all__'

class repartidoresSelializer(serializers.ModelSerializer):
    class Meta:
        model = models.Repartidores
        fields = '__all__'

class transferenciasSelializer(serializers.ModelSerializer):
    class Meta:
        model = models.Transferencias
        fields = '__all__'

# class notificationSelializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Notification
#         fields = '__all__'
