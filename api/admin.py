from django.contrib import admin
from api.models.upc_lead import UPCLead

#admin.site.register(UPCLead)
@admin.register(UPCLead)
class UPCLeadAdmin(admin.ModelAdmin):
    list_display=['id','registration_date','document_number','name','last_name_one','last_name_two', 'cellphone', 'sede_product_interest_1','product_one','email']

    # Campos que serán de solo lectura al editar
    '''readonly_fields = ['id', 'registration_date', 'document_number', 'email']

    def get_exclude(self, request, obj=None):
        # Campos que serán excluidos al editar
        if obj:
            return ['campo_a_excluir', 'otro_campo_a_excluir']
        else:
            return []
    '''