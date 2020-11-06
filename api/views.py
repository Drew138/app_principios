from rest_framework import viewsets, permissions, generics
from . import serializers as custom_serializers
from . import models as custom_models
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response


# Get User API
class UserAPI(generics.RetrieveAPIView):

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = custom_serializers.UsuarioSerializer

    def get_object(self):
        return self.request.user


class UsersView(generics.GenericAPIView):

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = custom_serializers.UsuarioSerializer

    def get_queryset(self):
        if self.request.user.tipo == "comprador":
            queryset = custom_models.Usuario.objects.all().filter(tipo="vendedor")
        else:
            queryset = custom_models.Usuario.objects.all().filter(tipo="comprador")
        return queryset


class RegistroView(generics.ListAPIView):

    serializer_class = custom_serializers.RegistroSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(self.request.user)  # JWT token
        return Response({
            "user": custom_serializers.RegistroSerializer(
                user,
                context=self.get_serializer_context()).data,
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        })


class ProductoView(viewsets.ModelViewSet):

    serializer_class = custom_serializers.ProductoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        vendedor = self.request.query_params.get("vendedor", None)
        queryset = custom_models.Producto.objects.filter(
            vendedor__establecimiento=vendedor)
        return queryset


class OrdenView(viewsets.ModelViewSet):

    serializer_class = custom_serializers.OrdenSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.tipo == "comprador":
            queryset = custom_models.Orden.objects.filter(
                comprador=self.request.user)
        else:
            queryset = custom_models.Orden.objects.filter(
                producto__vendedor=self.request.user).filter(completado=False)
        return queryset
