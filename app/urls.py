from django.contrib import admin
from django.urls import include, path

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from core.views import (
    FilaViewSet,
    ModalidadeViewSet,
    ServicoViewSet,
    EloViewSet,
    StatusViewSet,
    UserViewSet,
)

# Define os roteadores
router = DefaultRouter()
router.register(r"fila", FilaViewSet)
router.register(r"modalidade", ModalidadeViewSet)
router.register(r"servico", ServicoViewSet)
router.register(r"elo", EloViewSet)
router.register(r"status", StatusViewSet)
router.register("users", UserViewSet, basename="users")

urlpatterns = [
    # Endpoints do core
    path("", include(router.urls)),
    # Endpoints do admin
    path("admin/", admin.site.urls),
    # Endpoints da API de usuário
    path("api/", include(router.urls)),
    # Endpoints do Spectacular para documentação
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    # Endpoints para autenticação JWT
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
