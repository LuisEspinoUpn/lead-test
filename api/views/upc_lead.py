from rest_framework.viewsets import ModelViewSet
from api.models.upc_lead import UPCLead
from api.serializers import UPCLeadSerializer

from api.services import scheduler
from api.upctasks import send_upc_form

class UPCLeadApiViewSet(ModelViewSet):
    queryset = UPCLead.objects.all()
    serializer_class = UPCLeadSerializer

    def perform_create(self, serializer):
        # Lógica antes de la creación del objeto
        super().perform_create(serializer)
        # Lógica después de la creación del objeto
        objeto_creado = serializer.instance
        #print(f'Se ha creado un objeto con id {objeto_creado.id}')

        scheduler.add_job(
            send_upc_form,
            kwargs={"pk": objeto_creado.pk},
            id=f"send_upc_form-{objeto_creado.pk}",
            replace_existing=True,
        )
