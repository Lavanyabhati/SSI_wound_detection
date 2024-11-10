from django.urls import path
from .views import *

urlpatterns = [
    path('patient_administration_details/add/', add_patient_administration_details, name='add_patient_administration_details'),
    path('patient_microbiology_details/add/', add_microbiology_details, name='add_microbiology_details'),
    path('patient_antibiotic_surveillance/add/', add_antibiotic_surveillance, name='add_antibiotic_surveillance'),
    path('patient_post_surgery_details/add/', add_post_surgery_details, name='add_post_surgery_details'),
    path('patient_ssi_evaluation_details/add/', add_ssi_evaluation_details, name='add_ssi_evaluation_details'),
    # path('form4/add/', add_patient_antibiotic_form, name='add_patient_admin_form')
]
