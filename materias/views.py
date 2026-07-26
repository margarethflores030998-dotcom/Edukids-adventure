from rest_framework import viewsets
from .models import Idioma, Categoria, Palabra
from .serializers import IdiomaSerializer, CategoriaSerializer, PalabraSerializer


class IdiomaViewSet(viewsets.ModelViewSet):
    queryset = Idioma.objects.all()
    serializer_class = IdiomaSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class PalabraViewSet(viewsets.ModelViewSet):
    queryset = Palabra.objects.all()
    serializer_class = PalabraSerializer

    def get_queryset(self):
        queryset = Palabra.objects.all()

        idioma = self.request.query_params.get('idioma')
        categoria = self.request.query_params.get('categoria')

        if idioma:
            queryset = queryset.filter(idioma__id=idioma)

        if categoria:
            queryset = queryset.filter(categoria__id=categoria)

        return queryset