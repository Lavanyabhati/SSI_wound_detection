from django.urls import path
from .views import *

urlpatterns = [
    path('patient_administration_details/add/', add_patient_administration_details, name='add_patient_administration_details'),
    # path('form2/add/', add_patient_surgery_form, name='add_patient_admin_form'),
    # path('form3/add/', add_patient_microbiology_form, name='add_patient_admin_form'),
    # path('form4/add/', add_patient_antibiotic_form, name='add_patient_admin_form')
]