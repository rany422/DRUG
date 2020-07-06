from django.db import models
from datetime import datetime, date
from django.utils import timezone
from django_currentuser.db.models import CurrentUserField
from django_currentuser.middleware import get_current_authenticated_user


class Drug_Master(models.Model):
    company_name = models.CharField(max_length=60, null=True, blank=False)
    brand_name = models.CharField(max_length=60, null=True, blank=False)
    dosage_type = models.CharField(max_length=60, null=True, blank=False)
    dosage_form = models.CharField(max_length=60, null=True, blank=False)
    schedule_type = models.CharField(max_length=60, null=True, blank=False)
    sheif_life = models.IntegerField(null=True, blank=False)
    speciality = models.CharField(max_length=70, null=True, blank=False)
    HSN_CODE = models.CharField(max_length=50, null=True, blank=False)
    drug_indication = models.CharField(max_length=70, null=True, blank=False)
    warning = models.CharField(max_length=100, null=True, blank=False)
    gst = models.IntegerField(null=True, blank=False)
    updated_on = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name

class Generic_Information(models.Model):
    generic_name = models.CharField(max_length=120)
    generic_strength = models.IntegerField()    
    generic_unit = models.CharField(max_length=120)        
    drug_master = models.ForeignKey(Drug_Master, null=True, on_delete=models.CASCADE, related_name="drug")

    def __str__(self):
        return self.generic_name
