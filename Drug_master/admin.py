from django.contrib import admin
from .models import Drug_Master, Generic_Information



class Drug_MasterAdmin(admin.ModelAdmin):
    list_display = ['id', 'company_name']
admin.site.register(Drug_Master, Drug_MasterAdmin)
class Generic_InformationAdmin(admin.ModelAdmin):
    list_display = ['id', 'generic_name', 'generic_unit', 'drug_master_id']
admin.site.register(Generic_Information, Generic_InformationAdmin)