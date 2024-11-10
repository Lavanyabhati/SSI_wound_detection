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
            'patientName': decoded_body.get('patientName'),
            'patientID': decoded_body.get('patientID'),
            'age': decoded_body.get('age'),
            'gender': decoded_body.get('gender'),
            'dateOfAdmission': decoded_body.get('dateOfAdmission'),
            'dateOfProcedure': decoded_body.get('dateOfProcedure'),
            'admittingDepartment': decoded_body.get('admittingDepartment'),
            'departmentPrimarySurgeon': decoded_body.get('departmentPrimarySurgeon'),
            'procedureName': decoded_body.get('procedureName'),
            'diagnosis': decoded_body.get('diagnosis'),
            'procedureDoneBy': decoded_body.get('procedureDoneBy'),
            'operationTheatre': decoded_body.get('operationTheatre'),
            'outpatientProcedure': decoded_body.get('outpatientProcedure'),
            'scenarioProcedure': decoded_body.get('scenarioProcedure'),
            'woundClass': decoded_body.get('woundClass'),
            'papGiven': decoded_body.get('papGiven'),
            'antibioticsGiven': decoded_body.get('antibioticsGiven'),
            'durationPAP': decoded_body.get('durationPAP'),
            'ssiEventOccurred': decoded_body.get('ssiEventOccurred'),
            'dateOfEvent': decoded_body.get('dateOfEvent')
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


@csrf_exempt
@require_http_methods(["POST"])
def add_microbiology_details(request, *args, **kwargs):
    EVENT = "AddMicrobiologyDetails"
    IP = client_ip(request)
    LOG_PREFIX = f'"EventName":"{EVENT}", "IP":"{IP}"'
    cls_nurse = Nurse()

    try:
        decoded_body = json.loads(request.body.decode())
        form = MicrobiologyForm(decoded_body)

        if not form.is_valid():
            return JsonResponse({"status": "FAILURE", "statuscode": 400, "msg": form.errors})

        data_dict = {
            'micro_organism': decoded_body.get('micro_organism'),
            'antibiotic': []
        }

        for antibiotic in ANTIBIOTIC_CHOICES:
            antibiotic_name = antibiotic[0]
            antibiotic_key = antibiotic_name.lower().replace(' ', '_').replace('-', '_')  # Format key for lookup

            mic_value = decoded_body.get(f"{antibiotic_key}_mic")
            interpretation = decoded_body.get(f"{antibiotic_key}_interpretation")

            log.info(f"Antibiotic: {antibiotic_name}, MIC: {mic_value}, Interpretation: {interpretation}")

            if mic_value or interpretation:
                data_dict['antibiotic'].append({
                    'name': antibiotic_name,
                    'mic_value': mic_value if mic_value else None,
                    'interpretation': interpretation if interpretation else None
                })

        if not data_dict['antibiotic']:
            data_dict['antibiotic'].append({
                'name': 'No antibiotic data provided',
                'mic_value': None,
                'interpretation': None
            })

        log.info(f"Data to insert into _add_microbiology_details: {data_dict}")

        insert_microbiology_details = cls_nurse._add_microbiology_details(LOG_PREFIX, data=data_dict)
        log.info(f"{LOG_PREFIX}, 'Result':'Inserted Microbiology Details', 'Details':{insert_microbiology_details}")

        if insert_microbiology_details:
            return JsonResponse({"status": "SUCCESS", "statuscode": 200, "msg": "Patient's Microbiology details added successfully!"})
        else:
            return JsonResponse({"status": "FAILURE", "statuscode": 500, "msg": "Failed to add patient's microbiology details!"})

    except Exception as e:
        log.error(f'{LOG_PREFIX}, "Result":"Failure", "Reason":"{e}"')
        return JsonResponse({"status": "FAILURE", "statuscode": 500, "msg": "Internal Server Error!"})


@csrf_exempt
@require_http_methods(["POST"])
def add_antibiotic_surveillance(request, *args, **kwargs):
    EVENT = "AddAntibioticSurveillanceDetails"
    IP = client_ip(request)
    LOG_PREFIX = f'"EventName":"{EVENT}", "IP":"{IP}"'
    cls_nurse = Nurse()

    try:
        decoded_body = json.loads((request.body).decode())
        form = AntibioticSurveillanceForm(decoded_body)

        if not form.is_valid():
            return JsonResponse({"status": "FAILURE", "statuscode": 400, "msg": form.errors})

        # unique_id = kwargs.get('unique_id')
        # log.info("UNIQUE ID :%s" % unique_id)
        #
        # if not unique_id:
        #     return JsonResponse({"status": "FAILURE", "statuscode": 400, "msg": "Unique ID is required!"})

        data_dict = {
         # 'unique_id': unique_id,
            'antibiotic_prior_1': decoded_body.get('antibiotic_prior_1'),
            'route_prior_1': decoded_body.get('route_prior_1'),
            'duration_prior_1': decoded_body.get('duration_prior_1'),
            'doses_prior_1': decoded_body.get('doses_prior_1'),
            'antibiotic_prior_2': decoded_body.get('antibiotic_prior_2'),
            'route_prior_2': decoded_body.get('route_prior_2'),
            'duration_prior_2': decoded_body.get('duration_prior_2'),
            'doses_prior_2': decoded_body.get('doses_prior_2'),
            'antibiotic_prior_3': decoded_body.get('antibiotic_prior_3'),
            'route_prior_3': decoded_body.get('route_prior_3'),
            'duration_prior_3' : decoded_body.get('duration_prior_3'),
            'doses_prior_3': decoded_body.get('doses_prior_3'),
            'antibiotic_pre_1': decoded_body.get('antibiotic_pre_1'),
            'route_pre_1': decoded_body.get('route_pre_1'),
            'duration_pre_1': decoded_body.get('duration_pre_1'),
            'doses_pre_1': decoded_body.get('doses_pre_1'),
            'antibiotic_pre_2': decoded_body.get('antibiotic_pre_2'),
            'route_pre_2': decoded_body.get('route_pre_2'),
            'duration_pre_2': decoded_body.get('duration_pre_2'),
            'doses_pre_2' : decoded_body.get('doses_pre_2'),
            'antibiotic_pre_3': decoded_body.get('antibiotic_pre_3'),
            'route_pre_3': decoded_body.get('route_pre_3'),
            'duration_pre_3': decoded_body.get('duration_pre_3'),
            'doses_pre_3': decoded_body.get('doses_pre_3'),
            'antibiotic_post_1': decoded_body.get('antibiotic_post_1'),
            'route_post_1': decoded_body.get('route_post_1'),
            'duration_post_1': decoded_body.get('duration_post_1'),
            'doses_post_1': decoded_body.get('doses_post_1'),
            'antibiotic_post_2': decoded_body.get('antibiotic_post_2'),
            'route_post_2': decoded_body.get('route_post_2'),
            'duration_post_2': decoded_body.get('duration_post_2'),
            'doses_post_2': decoded_body.get('doses_post_2'),
            'antibiotic_post_3': decoded_body.get('antibiotic_post_3'),
            'route_post_3': decoded_body.get('route_post_3'),
            'duration_post_3': decoded_body.get('duration_post_3'),
            'doses_post_3': decoded_body.get('doses_post_3'),
            'antibiotic_post_4': decoded_body.get('antibiotic_post_4'),
            'route_post_4': decoded_body.get('route_post_4'),
            'duration_post_4': decoded_body.get('duration_post_4'),
            'doses_post_4': decoded_body.get('doses_post_4'),
            'antibiotic_post_5': decoded_body.get('antibiotic_post_5'),
            'route_post_5': decoded_body.get('route_post_5'),
            'duration_post_5': decoded_body.get('duration_post_5'),
            'doses_post_5': decoded_body.get('doses_post_5'),
            'antibiotic_post_6': decoded_body.get('antibiotic_post_6'),
            'route_post_6': decoded_body.get('route_post_6'),
            'duration_post_6': decoded_body.get('duration_post_6'),
            'doses_post_6': decoded_body.get('doses_post_6'),
            'time_induction': decoded_body.get('time_induction'),
            'time_incision': decoded_body.get('time_incision'),
            'time_end_surgery': decoded_body.get('time_end_surgery')
        }
        insert_antibiotic_surveillance_details = cls_nurse._add_antibiotic_surveillance(LOG_PREFIX, data=data_dict)
        log.info("INSERT PATIENT ADMINISTRATION DETAILS :%s" % insert_antibiotic_surveillance_details)

        if insert_antibiotic_surveillance_details:
            return JsonResponse({"status": "SUCCESS", "statuscode": 200, "msg": "Patient's Antibiotic Surveillance details added successfully!"})
        else:
            return JsonResponse({"status": "FAILURE", "statuscode": 500, "msg": "Failed to add Patient's Antibiotic Surveillance details!"})

    except Exception as e:
        log.error(f'{LOG_PREFIX}, "Result":"Failure", "Reason":"{e}"')
        return JsonResponse({"status": "FAILURE", "statuscode": 500, "msg": "Internal Server Error!"})


@csrf_exempt
@require_http_methods(["POST"])
def add_post_surgery_details(request, *args, **kwargs):
    EVENT = "AddPostSurgeryDetails"
    IP = client_ip(request)
    LOG_PREFIX = f'"EventName":"{EVENT}", "IP":"{IP}"'
    cls_nurse = Nurse()

    try:
        decoded_body = json.loads(request.body.decode())
        form = PostOpDayForm(decoded_body)

        if not form.is_valid():
            return JsonResponse({"status": "FAILURE", "statuscode": 400, "msg": form.errors})

        data_dict = {
            'date_of_procedure': decoded_body.get('date_of_procedure'),
            'name_of_procedure': decoded_body.get('name_of_procedure'),
            'symptoms': [],
        }

        symptoms = decoded_body.get('symptoms', [])
        for symptom_data in symptoms:
            if not isinstance(symptom_data, dict):
                log.error(f"{LOG_PREFIX} - Invalid symptom data structure: {symptom_data}")
                continue

            symptom_name = symptom_data.get('symptom', 'No symptom data provided')
            symptom_days = symptom_data.get('days', [])

            if not isinstance(symptom_days, list):
                log.error(f"{LOG_PREFIX} - Invalid days data structure for symptom: {symptom_name}")
                continue

            days_list = []
            for day_entry in symptom_days:
                if not isinstance(day_entry, dict):
                    log.error(f"{LOG_PREFIX} - Invalid day entry: {day_entry}")
                    continue

                day = day_entry.get('day')
                status = day_entry.get('status', 'Empty')

                if day and status != 'Empty':
                    days_list.append({'day': day, 'status': status})

            if days_list:
                data_dict['symptoms'].append({
                    'symptom': symptom_name,
                    'days': days_list
                })

        if not data_dict['symptoms']:
            log.info(f"{LOG_PREFIX} - No symptoms data provided. Adding placeholder entry.")
            data_dict['symptoms'].append({
                'symptom': 'No symptom data provided',
                'days': []
            })

        log.info(f"Data to insert into _add_post_op_details: {data_dict}")

        insert_post_op_details = cls_nurse._add_post_op_details(LOG_PREFIX, data=data_dict)

        if insert_post_op_details:
            return JsonResponse({"status": "SUCCESS", "statuscode": 200, "msg": "Post-surgery details added successfully!"})
        else:
            return JsonResponse({"status": "FAILURE", "statuscode": 500, "msg": "Failed to add post-surgery details!"})

    except Exception as e:
        log.error(f'{LOG_PREFIX}, "Result":"Failure", "Reason":"{e}"')
        return JsonResponse({"status": "FAILURE", "statuscode": 500, "msg": "Internal Server Error!"})


@csrf_exempt
@require_http_methods(["POST"])
def add_ssi_evaluation_details(request, *args, **kwargs):
    EVENT = "AddSSIEvaluationDetails"
    IP = client_ip(request)
    LOG_PREFIX = f'"EventName":"{EVENT}", "IP":"{IP}"'
    cls_nurse = Nurse()

    try:
        decoded_body = json.loads(request.body.decode())
        form = SSIEvaluationForm(decoded_body)

        if not form.is_valid():
            return JsonResponse({"status": "FAILURE", "statuscode": 400, "msg": form.errors})

        data_dict = {
            'procedure_name': decoded_body.get('procedure_name'),
            'patient_id': decoded_body.get('patient_id'),
            'patient_name': decoded_body.get('patient_name'),
            'age': decoded_body.get('age'),
            'gender': decoded_body.get('gender'),
            'date_of_procedure': decoded_body.get('date_of_procedure'),
            'evaluation_fields': {},
        }

        # Extract evaluation fields and their remarks
        for field in SSIEvaluationForm.dynamic_fields:
            choice_key = f"{field}_choice"
            remarks_key = f"{field}_remarks"

            data_dict['evaluation_fields'][field] = {
                'choice': decoded_body.get(choice_key),
                'remarks': decoded_body.get(remarks_key),
            }

        log.info(f"{LOG_PREFIX} - Successfully extracted SSI evaluation data: {data_dict}")

        # Insert the extracted data into the system
        insert_ssi_evaluation_details = cls_nurse._add_ssi_evaluation(LOG_PREFIX, data=data_dict)

        if insert_ssi_evaluation_details:
            return JsonResponse({"status": "SUCCESS", "statuscode": 200, "msg": "SSI evaluation details added successfully!"})
        else:
            return JsonResponse({"status": "FAILURE", "statuscode": 500, "msg": "Failed to add SSI evaluation details!"})

    except Exception as e:
        log.error(f'{LOG_PREFIX}, "Result":"Failure", "Reason":"{e}"')
        return JsonResponse({"status": "FAILURE", "statuscode": 500, "msg": "Internal Server Error!"})



# @csrf_exempt
# @require_http_methods(["POST"])
# def add_ssi_evaluation_details(request, *args, **kwargs):
#     EVENT = "AddSSIEvaluationDetails"
#     IP = client_ip(request)
#     LOG_PREFIX = f'"EventName":"{EVENT}", "IP":"{IP}"'
#     cls_nurse = Nurse()
#
#     try:
#         decoded_body = json.loads(request.body.decode())
#         form = SSIEvaluationForm(decoded_body)
#
#         if not form.is_valid():
#             return JsonResponse({"status": "FAILURE", "statuscode": 400, "msg": form.errors})
#
#         data_dict = {
#             'procedure_name': decoded_body.get('procedure_name'),
#             'patient_id': decoded_body.get('patient_id'),
#             'patient_name': decoded_body.get('patient_name'),
#             'age': decoded_body.get('age'),
#             'gender': decoded_body.get('gender'),
#             'date_of_procedure': decoded_body.get('date_of_procedure'),
#             'evaluation_fields': {},
#         }
#
#         # Extract evaluation fields and their remarks
#         for field in SSIEvaluationForm.fields:
#             choice_key = f"{field}_choice"
#             remarks_key = f"{field}_remarks"
#
#             data_dict['evaluation_fields'][field] = {
#                 'choice': decoded_body.get(choice_key),
#                 'remarks': decoded_body.get(remarks_key),
#             }
#
#         log.info(f"{LOG_PREFIX} - Successfully extracted SSI evaluation data: {data_dict}")
#
#         insert_ssi_evaluation_details = cls_nurse._add_ssi_evaluation(LOG_PREFIX, data=data_dict)
#
#         if insert_ssi_evaluation_details:
#             return JsonResponse({"status": "SUCCESS", "statuscode": 200, "msg": "SSI evaluation details added successfully!"})
#         else:
#             return JsonResponse({"status": "FAILURE", "statuscode": 500, "msg": "Failed to add SSI evaluation details!"})
#
#     except Exception as e:
#         log.error(f'{LOG_PREFIX}, "Result":"Failure", "Reason":"{e}"')
#         return JsonResponse({"status": "FAILURE", "statuscode": 500, "msg": "Internal Server Error!"})
