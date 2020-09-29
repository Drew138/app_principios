from rest_framework import serializers
from . import models as custom_models


class CiudadSerializer(serializers.ModelSerializer):

    class Meta:
        model = custom_models.Ciudad
        fields = '__all__'


# view
class UsuarioSerializer(serializers.ModelSerializer):

    ciudad = CiudadSerializer()

    class Meta:
        model = custom_models.Usuario
        fields = [
            'id',
            'username',
            'email',
            'ciudad',
            "tipo",
            "genero",
        ]


# Register Serializer
class RegistroSerializer(serializers.ModelSerializer):

    ciudad = CiudadSerializer()

    class Meta:
        model = custom_models.VibroUser
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
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
        user = custom_models.VibroUser.objects.create_user(**validated_data)
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
