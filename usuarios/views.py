from django.http import JsonResponse
from .models import Usuario

def lista_usuarios(request):
    usuarios = list(
        Usuario.objects.all().values(
            'id',
            'nombre',
            'edad',
            'nivel'
        )
    )

    return JsonResponse(usuarios, safe=False)