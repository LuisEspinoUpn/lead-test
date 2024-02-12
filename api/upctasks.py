import zoneinfo, json
from datetime import datetime

import requests
from django.db import transaction
from django.template import loader

from api.models import UPCLead


tzlima = zoneinfo.ZoneInfo("America/Lima")


def send_upc_form(pk):
    
    #gs = Setting.get_all()

    with transaction.atomic():
        lead = UPCLead.objects.select_for_update().get(id=pk)

        print(lead.document_number)
        try:
            send_form_to_crm(lead)
            #send_form_to_rw(form, gs)
            #send_form_to_new_rw(form)
        finally:
            lead.save()
            

def send_form_to_crm(form, gs=None):
    print("Invoca a CRM")