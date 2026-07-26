from django.http import JsonResponse
from .models import Recompensa

def lista_recompensas(request):
    recompensas = list(
        Recompensa.objects.all().values(
            'id',
            'nombre',
            'descripcion',
            'puntos_necesarios'
        )
    )

    return JsonResponse(recompensas, safe=False)