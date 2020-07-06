from django.urls import path
from .import views
urlpatterns = [
    path('drug_master/', views.list_display, name='drug_master'),
    path('add_new/', views.new_DrugMaster, name='add_new'),
    path('create_drug/', views.createdrug, name='create_drug'),

    path('delete_drug/<int:id>/', views.destroy_drug, name="delete_drug"),  
    path('delete_generic/<int:id>/', views.destroy_generic, name="delete_generic"),
   
    path('edit_drug/<int:id>', views.edit_drug),
    path('update_drug/<int:id>', views.update_drug),

    path('edit_generic/<int:id>', views.edit_generic),
    path('update_generic/<int:id>', views.update_generic),



]
