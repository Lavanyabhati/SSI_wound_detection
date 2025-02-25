from Nurse.views import verify_auth_token
import json
import os
import pickle
from django.http import JsonResponse
from  .forms import *
from .register_views import *
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from configuration import *
import math
from functools import wraps
from helpers.jwthelper import JWToken
import random
from .models import *


@csrf_exempt
@require_http_methods(["POST"])
@verify_auth_token
def update_jr_doctor_details(request, *args, **kwargs):
    cls_register = JrDoctor()
    EVENT = "UpdateJuniorDoctorDetails"
    IP = client_ip(request)
    LOG_PREFIX = f'"EventName":"{EVENT}", "IP":"{IP}"'
    try:
        decoded_body = json.loads(request.body.decode())
        form = JrDoctorUpdateForm(decoded_body)

        if not form.is_valid():
            return JsonResponse({"status": "FAILURE", "statuscode": 400, "msg": form.errors})

        employee_id = kwargs.get('employee_id')
        log.info("EMPLOYEE ID :%s" % employee_id)

        if not employee_id:
            return JsonResponse({"status": "FAILURE", "statuscode": 400, "msg": "Employee ID is required!"})

        phone_number = kwargs.get('phone_number')
        log.info("PHONE NUMBER :%s" % phone_number)

        if not phone_number:
            return JsonResponse({"status": "FAILURE", "statuscode": 400, "msg": "Phone Number is required!"})

        update_data = {
            'employee_id': employee_id,
            'phone_number': phone_number,
            'name': decoded_body.get('name'),
            'email': decoded_body.get('email'),
            'gender': decoded_body.get('gender'),
            'department': decoded_body.get('department'),
            'date_of_birth': decoded_body.get('date_of_birth'),
            'verification_status': 'APPROVED',
            'updated_at': datetime.now(),
        }

        log.info(f'{LOG_PREFIX}, "UpdateData": {update_data}')

        jr_doctor_details_update = cls_register._update_jr_doctor(LOG_PREFIX, data=update_data)

        log.info(f'{LOG_PREFIX}, "NurseUpdateResult": {jr_doctor_details_update}')

        if jr_doctor_details_update:
            return JsonResponse({"status": "SUCCESS", "statuscode": 200, "msg": "Junior Doctor details updated successfully!"})
        else:
            return JsonResponse({"status": "FAILURE", "statuscode": 500, "msg": "Failed to update Junior Doctor details!"})

    except Exception as e:
        log.error(f'{LOG_PREFIX}, "Result":"Failure", "Reason":"{e}"')
        return JsonResponse({"status": "FAILURE", "statuscode": 500, "msg": "Internal Server Error"})