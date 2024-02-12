from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404

from api.models.upc_lead import UPCLead

def saludo(request):
    #page = get_object_or_404(Page, id="autoridades", online=True)

    return JsonResponse(
        {
            "name": "Richard",
            "saludo": "Hola chicos",
        },
        json_dumps_params={"indent": 4},
    )

def test(request):
    return JsonResponse(
        {
            "saludo": "Hola chicos",
        },
        json_dumps_params={"indent": 4},
    )