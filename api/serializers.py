from rest_framework import serializers
from . import models as custom_models


# view
class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = custom_models.Usuario
        fields = [
            'id',
            'username',
            'telefono',
            "tipo",
            "genero",
            "establecimiento",
            "direccion"
        ]


# Register Serializer
class RegistroSerializer(serializers.ModelSerializer):

    class Meta:
        model = custom_models.VibroUser
        fields = [
            'username',
            'first_name',
            'last_name',
            'password',
            'genero',
            'telefono',
            'direccion',
            'ciudad',
            'establecimiento',
            'tipo',
        ]
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}

    def create(self, validated_data):
        user = custom_models.Usuario.objects.create_user(**validated_data)
        return user


class ProductoSerializer(serializers.ModelSerializer):

    vendedor = UsuarioSerializer()

    class Meta:
        model = custom_models.Producto
        fields = '__all__'


class OrdenSerializer(serializers.ModelSerializer):

    comprador = UsuarioSerializer()

    producto = ProductoSerializer()

    class Meta:
        model = custom_models.Producto
        fields = '__all__'
