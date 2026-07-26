from rest_framework import serializers
from .models import Idioma, Categoria, Palabra


class IdiomaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idioma
        fields = '__all__'


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class PalabraSerializer(serializers.ModelSerializer):
    idioma_nombre = serializers.CharField(source='idioma.nombre', read_only=True)
    categoria_nombre = serializers.CharField(source='categoria.nombre', read_only=True)

    class Meta:
        model = Palabra
        fields = [
            'id',
            'palabra_espanol',
            'traduccion',
            'descripcion',
            'imagen',
            'audio',
            'idioma',
            'idioma_nombre',
            'categoria',
            'categoria_nombre',
        ]