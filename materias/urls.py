from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IdiomaViewSet, CategoriaViewSet, PalabraViewSet

router = DefaultRouter()
router.register(r'idiomas', IdiomaViewSet)
router.register(r'categorias', CategoriaViewSet)
router.register(r'palabras', PalabraViewSet)

urlpatterns = [
    path('', include(router.urls)),
]