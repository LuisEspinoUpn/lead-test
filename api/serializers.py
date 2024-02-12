from rest_framework.serializers import ModelSerializer
from api.models.upc_lead import UPCLead

class UPCLeadSerializer(ModelSerializer):
    class Meta:
        model = UPCLead
        #fields = '__all__'
        fields = [
            'origin',
            'name',
            'last_name_one',
            'last_name_two',
            'document_type',
            'document_number',
            'birth_date',
            'gender',
            'cellphone',
            'email',
            'city',
            'campaign_has_reference',
            'digital_channel',
            'period_interest',
            'state_sale',
            'product_one',
            'origin_channel'
        ]
        #fields = ['id', 'name']