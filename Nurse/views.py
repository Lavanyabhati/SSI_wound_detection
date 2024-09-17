import json
from django.http import JsonResponse
from .forms import *
from .register_views import *
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from configuration import *
from geopy.distance import geodesic
import math
from functools import wraps
# from helpers.jwthelper import JWToken
import random



@csrf_exempt
@require_http_methods(["POST"])
def add_patient_administration_details(request, *args, **kwargs):
    EVENT = "AddPatientAdministration"
    IP = client_ip(request)
    LOG_PREFIX = f'"EventName":"{EVENT}", "IP":"{IP}"'
    cls_nurse = Nurse()

    try:
        decoded_body = json.loads((request.body).decode())
        form = PatientAdministrationForm(decoded_body)

        if not form.is_valid():
            return JsonResponse({"status": "FAILURE", "statuscode": 400, "msg": form.errors})

        # unique_id = kwargs.get('unique_id')
        # log.info("UNIQUE ID :%s" % unique_id)
        #
        # if not unique_id:
        #     return JsonResponse({"status": "FAILURE", "statuscode": 400, "msg": "Unique ID is required!"})

        data_dict = {
            # 'unique_id': unique_id,
            'patient_name': decoded_body.get('patient_name'),
            'patient_id': decoded_body.get('patient_id'),
            'age': decoded_body.get('age'),
            'gender': decoded_body.get('gender'),
            'date_of_admission': decoded_body.get('date_of_admission'),
            'date_of_procedure': decoded_body.get('date_of_procedure'),
            'admitting_department': decoded_body.get('admitting_department'),
            'department_primary_surgeon': decoded_body.get('department_primary_surgeon'),
            'name_of_procedure': decoded_body.get('name_of_procedure'),
            'diagnosis': decoded_body.get('diagnosis'),
            'procedure_done_by': decoded_body.get('procedure_done_by'),
            'operation_theatre': decoded_body.get('operation_theatre'),
            'outpatient_procedure': decoded_body.get('outpatient_procedure'),
            'scenario_of_procedure': decoded_body.get('scenario_of_procedure'),
            'wound_class': decoded_body.get('wound_class'),
            'pap_given': decoded_body.get('pap_given'),
            'antibiotics_given': decoded_body.get('antibiotics_given'),
            'duration_of_pap': decoded_body.get('duration_of_pap'),
            'ssi_event_occurred': decoded_body.get('ssi_event_occurred'),
            'date_of_event': decoded_body.get('date_of_event'),
            'specific_event_sip': decoded_body.get('specific_event_sip'),
            'specific_event_sis': decoded_body.get('specific_event_sis'),
            'specific_event_dip': decoded_body.get('specific_event_dip'),
            'specific_event_dis': decoded_body.get('specific_event_dis'),
            'organ_space': decoded_body.get('organ_space'),
            'detected': decoded_body.get('detected'),
            'death_by_BSI': decoded_body.get('death_by_BSI'),
            'microorganism_1': decoded_body.get('microorganism_1'),
            'microorganism_2': decoded_body.get('microorganism_2'),
            'isolate_1_sensitive': decoded_body.get('isolate_1_sensitive'),
            'isolate_2_sensitive': decoded_body.get('isolate_2_sensitive'),
        }

        insert_patient = cls_nurse._add_patient_administration_details(LOG_PREFIX, data=data_dict)
        log.info("INSERT PATIENT ADMINISTRATION DETAILS :%s" % insert_patient)

        if insert_patient:
            return JsonResponse(
                {"status": "SUCCESS", "statuscode": 200, "msg": "Patient administration details added successfully!"})
        else:
            return JsonResponse({"status": "FAILURE", "statuscode": 500, "msg": "Failed to add patient admininstration details!"})

    except Exception as e:
        log.error(f'{LOG_PREFIX}, "Result":"Failure", "Reason":"{e}"')
        return JsonResponse({"status": "FAILURE", "statuscode": 500, "msg": "Internal Server Error!"})