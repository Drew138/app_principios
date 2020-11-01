from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import routers
from django.urls import path
from . import views


auth_views = [
    path('auth/register', views.RegisterAPI.as_view()),
    path('auth/user', views.UserAPI.as_view()),
    path('auth/login/', TokenObtainPairView.as_view()),
    path('auth/token/refresh/', TokenRefreshView.as_view()),
]

router = routers.DefaultRouter()
router.register("usuarios", views.UsersView, "usuarios")
router.register("productos", views.UsersView, "productos")
router.register("ordenes", views.UsersView, "ordenes")


urlpatterns = auth_views + router.urls
