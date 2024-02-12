from django.db import models
from django.conf import settings
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils import timezone

import requests
from django.db.models.signals import post_save
from django.dispatch import receiver

class UPCLead(models.Model):
    ORIGIN_CHOICES = (
        (1, 'Peruano'),
        (2, 'Extranjero'),
    )

    GENDER_CHOICES = (
        (1, 'Masculino'),
        (2, 'Femenino'),
    )

    DOCUMENT_TYPE_CHOICES = (
        ('1', 'DNI'),
        ('2', 'Pasaporte'),
        # Agrega más tipos de documentos según sea necesario
    )

    CAMPAIGN_CHOICES = (
        ('1', 'Vive UPC'),
        ('6', 'Landing'),
        # Agrega más opciones según sea necesario
    )

    SALES_PHASE_CHOICES = (
        ('1', 'Lead'),
        # Agrega más opciones según sea necesario
    )

    ORIGIN_CHANNEL_CHOICES = (
        ('1', 'Vive UPC'),
        # Agrega más opciones según sea necesario
    )

    origin = models.IntegerField(choices=ORIGIN_CHOICES)
    name = models.CharField(max_length=50)
    last_name_one = models.CharField(max_length=50)
    last_name_two = models.CharField(max_length=50)
    document_type = models.CharField(choices=DOCUMENT_TYPE_CHOICES, max_length=2) # (Verificar) Listo
    document_number = models.CharField(max_length=20) #definir max_length
    birth_date = models.DateField(blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    cellphone = models.CharField(max_length=20)#definir max_length 9 Listo
    email = models.EmailField(max_length=80, blank=True, null=True)
    city = models.IntegerField(blank=True, null=True) #definir

    #Historia digital
    guid_client = models.CharField(max_length=50, blank=True, null=True)
    campaign_has_reference = models.CharField(max_length=30)
    digital_channel = models.CharField(max_length=2)#codigo
    format = models.CharField(max_length=3, blank=True, null=True) #catalogo
    inscription = models.IntegerField(default=0)#Listo | validar
    registration_date = models.DateField(blank=True, null=True)#formato yyyy/mm/dd
    pdp_version = models.CharField(max_length=60, blank=True, null=True)
    pdp_authorization_date = models.DateTimeField(blank=True, null=True)#formato yyyy/mm/dd
    pdp_authorization = models.BooleanField(default=False)
    
    history_id = models.CharField(max_length=50, blank=True, null=True) #solo para capturar respuesta de api historia
    
    #Oportunidad
    sales_phase = models.CharField(max_length=1, default=1)#opcion 1: Lead Listo
    period_interest = models.CharField(max_length=50)
    state_sale = models.CharField(max_length=3, blank=True, null=True)
    sub_state_sale = models.CharField(max_length=3, blank=True, null=True)
    product_one = models.CharField(max_length=50)
    sede_product_interest_1 = models.CharField(max_length=50, blank=True, null=True)
    origin_channel = models.CharField(max_length=1)
    
    #Auditoria
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    create_year = models.CharField(max_length=4, blank=True)
    create_month = models.CharField(max_length=2, blank=True)
    create_day = models.CharField(max_length=2, blank=True)

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.created_at =  timezone.now()
            # Si es un nuevo registro
            if self.created_at is not None:
                self.create_year = str(self.created_at.year)
                self.create_month = str(self.created_at.month).zfill(2)
                self.create_day = str(self.created_at.day).zfill(2)
        else:
            # Si se está actualizando un registro existente
            self.updated_at = timezone.now()

        super().save(*args, **kwargs)


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "UPCLead"
        verbose_name_plural = "UPCLeads"
        db_table = "upc_leads"