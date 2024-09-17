from datetime import datetime
from bson.objectid import ObjectId
from helpers.dbhelper import DBOperation
import random
from configuration import *

class Nurse:

    def __init__(self):
        self.db = DBOperation(DB_NAME)
        self.db_patient_admin = DBOperation(COLLECTION_PATIENT_ADMINISTRATION_DETAILS)

    def _add_patient_administration_details(self, LOG_PREFIX, data):
        try:
            patient_name = data.get('patient_name')
            patient_id = data.get('patient_id')
            age = data.get('age')
            gender = data.get('gender')
            date_of_admission = data.get('date_of_admission')
            date_of_procedure = data.get('date_of_procedure')
            admitting_department = data.get('admitting_department')
            department_primary_surgeon = data.get('department_primary_surgeon')
            name_of_procedure = data.get('name_of_procedure')
            diagnosis = data.get('diagnosis')
            procedure_done_by = data.get('procedure_done_by')
            operation_theatre = data.get('operation_theatre')
            outpatient_procedure = data.get('outpatient_procedure')
            scenario_of_procedure = data.get('scenario_of_procedure')
            wound_class = data.get('wound_class')
            pap_given = data.get('pap_given')
            antibiotics_given = data.get('antibiotics_given')
            duration_of_pap = data.get('duration_of_pap')
            ssi_event_occurred = data.get('ssi_event_occurred')
            date_of_event = data.get('date_of_event')
            specific_event_sip = data.get('specific_event_sip')
            specific_event_sis = data.get('specific_event_sis')
            specific_event_dip = data.get('specific_event_dip')
            specific_event_dis = data.get('specific_event_dis')
            organ_space = data.get('organ_space')
            detected = data.get('detected')
            death_by_bsi = data.get('death_by_BSI')
            microorganism_1 = data.get('microorganism_1')
            microorganism_2 = data.get('microorganism_2')
            isolate_1_sensitive = data.get('isolate_1_sensitive')
            isolate_2_sensitive = data.get('isolate_2_sensitive')

            data_dict = {
                'patient_name': patient_name,
                'patient_id': patient_id,
                'age': age,
                'gender': gender,
                'date_of_admission': date_of_admission,
                'date_of_procedure': date_of_procedure,
                'admitting_department': admitting_department,
                'department_primary_surgeon': department_primary_surgeon,
                'name_of_procedure': name_of_procedure,
                'diagnosis': diagnosis,
                'procedure_done_by': procedure_done_by,
                'operation_theatre': operation_theatre,
                'outpatient_procedure': outpatient_procedure,
                'scenario_of_procedure': scenario_of_procedure,
                'wound_class': wound_class,
                'pap_given': pap_given,
                'antibiotics_given': antibiotics_given,
                'duration_of_pap': duration_of_pap,
                'ssi_event_occurred': ssi_event_occurred,
                'date_of_event': date_of_event,
                'specific_event_sip': specific_event_sip,
                'specific_event_sis': specific_event_sis,
                'specific_event_dip': specific_event_dip,
                'specific_event_dis': specific_event_dis,
                'organ_space': organ_space,
                'detected': detected,
                'death_by_bsi': death_by_bsi,
                'microorganism_1': microorganism_1,
                'microorganism_2': microorganism_2,
                'isolate_1_sensitive': isolate_1_sensitive,
                'isolate_2_sensitive': isolate_2_sensitive,
                'created_at': datetime.now(),
                'updated_at': datetime.now(),
            }

            insert_patient_admin_details = self.db_patient_admin._insert(data=data_dict)

            return True if insert_patient_admin_details.inserted_id else False

        except Exception as e:
            logging.error(f'{LOG_PREFIX}, "Result":"Failure", "Reason":"{e}"')
            return None