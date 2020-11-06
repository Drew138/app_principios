from rest_framework import serializers
from . import models as custom_models


# view
class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = custom_models.Usuario
        fields = [
            'username',
            'telefono',
            "tipo",
            "establecimiento",
            "direccion"
        ]


# Register Serializer
class RegistroSerializer(serializers.ModelSerializer):

    establecimiento = serializers.CharField(required=False)

    class Meta:
        model = custom_models.Usuario
        fields = [
            'username',
            'password',
            'telefono',
            'direccion',
            'establecimiento',
            'tipo',
        ]
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}

    def create(self, validated_data):
        user = custom_models.Usuario.objects.create_user(**validated_data)
        return user


class ProductoSerializer(serializers.ModelSerializer):

    vendedor = UsuarioSerializer(required=False)

    class Meta:
        model = custom_models.Producto
        fields = '__all__'
    
    def create(self, validated_data):
        producto_instance = custom_models.Producto.objects.create(**validated_data, vendedor=self.context['request'].user)
        producto_instance.save()
        return producto_instance


class OrdenSerializer(serializers.ModelSerializer):

    comprador = UsuarioSerializer(required=False)

    producto = ProductoSerializer(required=False)

    class Meta:
        model = custom_models.Producto
        fields = '__all__'
    
    def create(self, validated_data):
        producto = validated_data["producto"]
        instanciaProducto = custom_models.Producto.objects.filter(vendedor=self.context['request'].user).filter(nombre=producto["nombre"])
        validated_data.pop("producto")
        orden_instance = custom_models.Orden.objects.create(**validated_data, producto=producto,comprador=self.context['request'].user)
        orden_instance.save()
        return orden_instance
