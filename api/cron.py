from django_cron import CronJobBase, Schedule
from .models.upc_lead import UPCLead
import requests

class DisplayUPCLeads(CronJobBase):
    RUN_EVERY_MINS = 1  # ejecutar cada minuto

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'api.display_upc_leads'    # un identificador único para esta tarea cron

    def do(self):
        api_url = "https://apicert-manager.upc.edu.pe/crm365/v3/contacto"
        subscription_key = "fc22433c099347ba87415eda480eb1db"

        for lead in UPCLead.objects.all():
            data = {
                "Origen": lead.origin,
                "NombreCompleto": lead.name,
                "PrimerApellido": lead.last_name_one,
                "SegundoApellido": lead.last_name_two,
                "TipoDocumento": lead.document_type,
                "NumeroDocumento": lead.document_number,
                "FechaNacimiento": str(lead.birth_date),
                "Genero": lead.gender,
                "TelefonoCelular": lead.cellphone,
                "CorreoPrincipal": lead.email,
                "Ciudad": lead.city,
            }

            headers = {
                "Ocp-Apim-Subscription-Key": subscription_key,
            }

            response = requests.post(api_url, json=data, headers=headers)

            if response.status_code == 200:
                json_response = response.json()  # Convertir la respuesta a JSON
                id_value = json_response.get("Id")  # Obtener el valor del campo "Id"
                if id_value:
                    lead.guid_client = id_value
                    lead.save()  # Guardar el valor en la base de datos
                    print(f"Registro enviado con éxito a la API. ID almacenado en lead.guid_client")

                    if lead.guid_client:  # Verificar si hay un guid_client almacenado
                        api_url2 = "https://apicert-manager.upc.edu.pe/CRM365/v3/HistorialDigital"
                        data = {
                            "ClienteGuid": lead.guid_client,
                            "CampanhaReferencia": "CMP-01108-N7W2P8",
                            "CanalDigital": "10",
                            "FechaRegistro": "2024-02-07",  # Puedes obtener la fecha actual usando bibliotecas como datetime
                            "PDP_Version": "TEST",
                            "PDP_FechaAutorizacion": "2024-02-07 08:14:00",
                            "PDP_Autoriza": "1"
                        }

                        headers = {
                            "Ocp-Apim-Subscription-Key": subscription_key,  # Asegúrate de definir subscription_key
                        }

                        response = requests.post(api_url2, json=data, headers=headers)

                        if response.status_code == 200:
                            print(f"Registro enviado con éxito a la segunda API para el cliente con GUID {lead.guid_client}")
                            json_response = response.json()  # Convertir la respuesta a JSON
                            id_api_two = json_response.get("Id")
                            if id_api_two:
                                api_url3 = "https://apicert-manager.upc.edu.pe/CRM365/v3/Oportunidad"
                                data = {
                                    "contactid": lead.guid_client,
                                    "FaseVenta": "1",
                                    "PeriodoInteres": lead.period_interest, 
                                    "EstadoVenta": lead.state_sale, 
                                    #"SubEstadoVenta": "30", //Opcional
                                    "Producto1": lead.product_one,
                                    #"SedeInteresProducto1": "B", //Opcional
                                    "Origen": lead.origin_channel
                                }
                                response = requests.post(api_url3, json=data, headers=headers)
                                if response.status_code == 200:
                                    print(f"Registro enviado con éxito a la tercera API para el cliente con GUID {lead.guid_client}")
                                else:
                                    print(f'Error al emviar la tercera api {lead.guid_client}: {response.status_code} - {response.text}')


                        else:
                            print(f"Error al enviar registro a la segunda API para el cliente con GUID {lead.guid_client}: {response.status_code} - {response.text}")

                    else:
                        print(f"No hay guid_client para el registro con ID {lead.id}. No se puede enviar a la segunda API.")

                else:
                    print("La respuesta de la API no contiene un campo 'Id'")
            else:
                print(f"Error al enviar registro a la API: {response.status_code} - {response.text}")