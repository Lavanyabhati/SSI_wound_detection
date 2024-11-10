from datetime import datetime
# from bson.objectid import ObjectId
from helpers.dbhelper import DBOperation
import random
from .forms import *
from configuration import *

class Nurse:

    def __init__(self):
        self.db = DBOperation(DB_NAME)
        self.db_patient_admin = DBOperation(COLLECTION_PATIENT_ADMINISTRATION_DETAILS)
        self.db_microbiology = DBOperation(COLLECTION_MICROBIOLOGY_DETAILS)
        self.db_antibiotic_surveillance = DBOperation(COLLECTION_ANTIBIOTIC_SURVEILLANCE_DETAILS)
        self.db_post_surgery_details = DBOperation(COLLECTION_POST_SURGERY_DETAILS)
        self.db_ssi_evaluation_details = DBOperation(COLLECTION_SSI_EVALUATION_DETAILS)

    def _add_patient_administration_details(self, LOG_PREFIX, data):
        try:
            patientName = data.get('patientName')
            patientID = data.get('patientID')
            age = data.get('age')
            gender = data.get('gender')
            dateOfAdmission = data.get('dateOfAdmission')
            dateOfProcedure = data.get('dateOfProcedure')
            admittingDepartment = data.get('admittingDepartment')
            departmentPrimarySurgeon = data.get('departmentPrimarySurgeon')
            procedureName = data.get('procedureName')
            diagnosis = data.get('diagnosis')
            procedureDoneBy = data.get('procedureDoneBy')
            operationTheatre = data.get('operationTheatre')
            outpatientProcedure = data.get('outpatientProcedure')
            scenarioProcedure = data.get('scenarioProcedure')
            woundClass = data.get('woundClass')
            papGiven = data.get('papGiven')
            antibioticsGiven = data.get('antibioticsGiven')
            durationPAP = data.get('durationPAP')
            ssiEventOccurred = data.get('ssiEventOccurred')
            dateOfEvent = data.get('dateOfEvent')
            data_dict = {
                'patientName': patientName,
                'patientID': patientID,
                'age': age,
                'gender': gender,
                'dateOfAdmission': dateOfAdmission,
                'dateOfProcedure': dateOfProcedure,
                'admittingDepartment': admittingDepartment,
                'departmentPrimarySurgeon': departmentPrimarySurgeon,
                'procedureName': procedureName,
                'diagnosis': diagnosis,
                'procedureDoneBy': procedureDoneBy,
                'operationTheatre': operationTheatre,
                'outpatientProcedure': outpatientProcedure,
                'scenarioProcedure': scenarioProcedure,
                'woundClass': woundClass,
                'papGiven': papGiven,
                'antibioticsGiven': antibioticsGiven,
                'durationPAP': durationPAP,
                'ssiEventOccurred': ssiEventOccurred,
                'dateOfEvent': dateOfEvent,
                'created_at': datetime.now(),
                'updated_at': datetime.now(),
            }

            insert_patient_admin_details = self.db_patient_admin._insert(data=data_dict)

            return True if insert_patient_admin_details.inserted_id else False

        except Exception as e:
            logging.error(f'{LOG_PREFIX}, "Result":"Failure", "Reason":"{e}"')
            return None

    def _add_microbiology_details(self, LOG_PREFIX, data):
        try:
            log.info(f"{LOG_PREFIX} - Received data: {data}")

            micro_organism = data.get('micro_organism')
            antibiotics_data = data.get('antibiotic', [])

            data_dict = {
                'micro_organism': micro_organism,
                'antibiotic': [],
                'created_at': datetime.now(),
                'updated_at': datetime.now()
            }

            for antibiotic in antibiotics_data:
                antibiotic_name = antibiotic.get('name', None)
                mic_value = antibiotic.get('mic_value', 0)
                interpretation_value = antibiotic.get('interpretation', None)
                log.info(
                    f"{LOG_PREFIX} - Processing antibiotic: {antibiotic_name}, MIC: {mic_value}, Interpretation: {interpretation_value}")

                data_dict['antibiotic'].append({
                    'name': antibiotic_name,
                    'mic_value': mic_value,
                    'interpretation': interpretation_value
                })

            if not data_dict['antibiotic']:
                log.info(f"{LOG_PREFIX} - No antibiotic data provided. Adding placeholder entry.")
                data_dict['antibiotic'].append({
                    'name': 'No antibiotic data provided',
                    'mic_value': None,
                    'interpretation': None
                })

            log.info(f"{LOG_PREFIX} - Final data dict to insert: {data_dict}")

            insert_microbiology_details = self.db_microbiology._insert(data=data_dict)

            log.info(f"{LOG_PREFIX} - Insert result: {insert_microbiology_details}")

            return True if insert_microbiology_details.inserted_id else False

        except Exception as e:
            logging.error(f'{LOG_PREFIX} - "Result":"Failure", "Reason":"{e}"')
            return None

    def _add_antibiotic_surveillance(self, LOG_PREFIX, data):
        try:
            antibiotic_prior_1 = data.get('antibiotic_prior_1')
            route_prior_1 = data.get('route_prior_1')
            duration_prior_1 = data.get('duration_prior_1')
            doses_prior_1 = data.get('doses_prior_1')
            antibiotic_prior_2 = data.get('antibiotic_prior_2')
            route_prior_2 = data.get('route_prior_2')
            duration_prior_2 = data.get('duration_prior_2')
            doses_prior_2 = data.get('doses_prior_2')
            antibiotic_prior_3 = data.get('antibiotic_prior_3')
            route_prior_3 = data.get('route_prior_3')
            duration_prior_3 = data.get('duration_prior_3')
            doses_prior_3 = data.get('doses_prior_3')
            antibiotic_pre_1 = data.get('antibiotic_pre_1')
            route_pre_1 = data.get('route_pre_1')
            duration_pre_1 = data.get('duration_pre_1')
            doses_pre_1 = data.get('doses_pre_1')
            antibiotic_pre_2 = data.get('antibiotic_pre_2')
            route_pre_2 = data.get('route_pre_2')
            duration_pre_2 = data.get('duration_pre_2')
            doses_pre_2 = data.get('doses_pre_2')
            antibiotic_pre_3 = data.get('antibiotic_pre_3')
            route_pre_3 = data.get('route_pre_3')
            duration_pre_3 = data.get('duration_pre_3')
            doses_pre_3 = data.get('doses_pre_3')
            antibiotic_post_1 = data.get('antibiotic_post_1')
            route_post_1 = data.get('route_post_1')
            duration_post_1 = data.get('duration_post_1')
            doses_post_1 = data.get('doses_post_1')
            antibiotic_post_2 = data.get('antibiotic_post_2')
            route_post_2 = data.get('route_post_2')
            duration_post_2 = data.get('duration_post_2')
            doses_post_2 = data.get('doses_post_2')
            antibiotic_post_3 = data.get('antibiotic_post_3')
            route_post_3 = data.get('route_post_3')
            duration_post_3 = data.get('duration_post_3')
            doses_post_3 = data.get('doses_post_3')
            antibiotic_post_4 = data.get('antibiotic_post_4')
            route_post_4 = data.get('route_post_4')
            duration_post_4 = data.get('duration_post_4')
            doses_post_4 = data.get('doses_post_4')
            antibiotic_post_5 = data.get('antibiotic_post_5')
            route_post_5 = data.get('route_post_5')
            duration_post_5 = data.get('duration_post_5')
            doses_post_5 = data.get('doses_post_5')
            antibiotic_post_6 = data.get('antibiotic_post_6')
            route_post_6 = data.get('route_post_6')
            duration_post_6 = data.get('duration_post_6')
            doses_post_6 = data.get('doses_post_6')
            time_induction = data.get('time_induction')
            time_incision = data.get('time_incision')
            time_end_surgery = data.get('time_end_surgery')

            data_dict = {
                'antibiotic_prior_1': antibiotic_prior_1,
                'route_prior_1': route_prior_1,
                'duration_prior_1': duration_prior_1,
                'doses_prior_1': doses_prior_1,
                'antibiotic_prior_2': antibiotic_prior_2,
                'route_prior_2': route_prior_2,
                'duration_prior_2': duration_prior_2,
                'doses_prior_2' : doses_prior_2,
                'antibiotic_prior_3': antibiotic_prior_3,
                'route_prior_3': route_prior_3,
                'duration_prior_3': duration_prior_3,
                'doses_prior_3': doses_prior_3,
                'antibiotic_pre_1': antibiotic_pre_1,
                'route_pre_1': route_pre_1,
                'duration_pre_1': duration_pre_1,
                'doses_pre_1': doses_pre_1,
                'antibiotic_pre_2': antibiotic_pre_2,
                'route_pre_2': route_pre_2,
                'duration_pre_2': duration_pre_2,
                'doses_pre_2': doses_pre_2,
                'antibiotic_pre_3': antibiotic_pre_3,
                'route_pre_3': route_pre_3,
                'duration_pre_3': duration_pre_3,
                'doses_pre_3': doses_pre_3,
                'antibiotic_post_1': antibiotic_post_1,
                'route_post_1': route_post_1,
                'duration_post_1': duration_post_1,
                'doses_post_1': doses_post_1,
                'antibiotic_post_2': antibiotic_post_2,
                'route_post_2': route_post_2,
                'duration_post_2': duration_post_2,
                'doses_post_2': doses_post_2,
                'antibiotic_post_3': antibiotic_post_3,
                'route_post_3': route_post_3,
                'duration_post_3': duration_post_3,
                'doses_post_3': doses_post_3,
                'antibiotic_post_4': antibiotic_post_4,
                'route_post_4': route_post_4,
                'duration_post_4': duration_post_4,
                'doses_post_4': doses_post_4,
                'antibiotic_post_5': antibiotic_post_5,
                'route_post_5': route_post_5,
                'duration_post_5': duration_post_5,
                'doses_post_5': doses_post_5,
                'antibiotic_post_6': antibiotic_post_6,
                'route_post_6': route_post_6,
                'duration_post_6': duration_post_6,
                'doses_post_6': doses_post_6,
                'time_induction': time_induction,
                'time_incision': time_incision,
                'time_end_surgery': time_end_surgery,
                'created_at': datetime.now(),
                'updated_at': datetime.now(),
            }
            insert_antibiotics_surveillance_details = self.db_antibiotic_surveillance._insert(data=data_dict)

            return True if insert_antibiotics_surveillance_details.inserted_id else False

        except Exception as e:
            logging.error(f'{LOG_PREFIX}, "Result":"Failure", "Reason":"{e}"')
            return None



        #event details
            # specific_event_sip = data.get('specific_event_sip')
            # specific_event_sis = data.get('specific_event_sis')
            # specific_event_dip = data.get('specific_event_dip')
            # specific_event_dis = data.get('specific_event_dis')
            # organ_space = data.get('organ_space')
            # detected = data.get('detected')
            # death_by_bsi = data.get('death_by_BSI')

    def _add_post_op_details(self, LOG_PREFIX, data):
        try:
            log.info(f"{LOG_PREFIX} - Received data: {data}")

            date_of_procedure = data.get('date_of_procedure')
            name_of_procedure = data.get('name_of_procedure')
            symptoms_data = data.get('symptoms', [])

            data_dict = {
                'date_of_procedure': date_of_procedure,
                'name_of_procedure': name_of_procedure,
                'symptoms': [],
                'created_at': datetime.now(),
                'updated_at': datetime.now()
            }

            for symptom_data in symptoms_data:
                symptom = symptom_data.get('symptom', 'No symptom data provided')
                days = symptom_data.get('days', [])

                symptom_entry = {
                    'symptom': symptom,
                    'days': [{'day': day.get('day'), 'status': day.get('status', 'Empty')} for day in days]
                }

                data_dict['symptoms'].append(symptom_entry)

            if not data_dict['symptoms']:
                log.info(f"{LOG_PREFIX} - No symptoms data provided. Adding placeholder entry.")
                data_dict['symptoms'].append({
                    'symptom': 'No symptom data provided',
                    'days': []
                })

            insert_post_op_details = self.db_post_surgery_details._insert(data=data_dict)

            log.info(f"{LOG_PREFIX} - Insert result: {insert_post_op_details}")

            return bool(insert_post_op_details.inserted_id)

        except Exception as e:
            log.error(f'{LOG_PREFIX} - "Result":"Failure", "Reason":"{e}"')
            return None


    # def _add_ssi_evaluation(self, LOG_PREFIX, data):
    #     try:
    #         log.info(f"{LOG_PREFIX} - Received data: {data}")
    #
    #         # Extract patient details
    #         patient_details = {
    #             'procedure_name': data.get('procedure_name', 'Not Provided'),
    #             'patient_id': data.get('patient_id', 'Not Provided'),
    #             'patient_name': data.get('patient_name', 'Unknown'),
    #             'age': data.get('age', 'Unknown'),
    #             'gender': data.get('gender', 'Not Specified'),
    #             'date_of_procedure': data.get('date_of_procedure', 'Not Provided'),
    #         }
    #
    #         # Log to verify received data for evaluation fields
    #         log.info(
    #             f"{LOG_PREFIX} - Evaluation Fields in Data: {data.get('evaluation_fields', 'No Evaluation Fields Found')}")
    #
    #         # Prepare evaluation fields by extracting dynamic keys
    #         evaluation_fields = {}
    #         for field in SSIEvaluationForm.dynamic_fields:
    #             choice_key = f"{field}_choice"
    #             remarks_key = f"{field}_remarks"
    #
    #             # Check if choice and remarks keys exist, else set to placeholders
    #             choice_value = data.get(choice_key, 'Not Specified')
    #             remarks_value = data.get(remarks_key, 'No Remarks')
    #
    #             # Log to see how the evaluation fields are being populated
    #             log.info(f"{LOG_PREFIX} - Field: {field}, Choice: {choice_value}, Remarks: {remarks_value}")
    #
    #             evaluation_fields[field] = {
    #                 'choice': choice_value,
    #                 'remarks': remarks_value
    #             }
    #
    #         # Construct the full SSI evaluation data object
    #         ssi_evaluation_data = {
    #             'patient_details': patient_details,
    #             'evaluation_fields': evaluation_fields,
    #             'created_at': datetime.now(),
    #             'updated_at': datetime.now()
    #         }
    #
    #         log.info(f"{LOG_PREFIX} - Successfully extracted SSI evaluation data: {ssi_evaluation_data}")
    #
    #         # Insert the evaluation data into the database
    #         insert_ssi_evaluation_details = self.db_ssi_evaluation_details._insert(data=ssi_evaluation_data)
    #
    #         log.info(f"{LOG_PREFIX} - Insert result: {insert_ssi_evaluation_details}")
    #
    #         # Check if the insertion was successful
    #         return bool(insert_ssi_evaluation_details.inserted_id)
    #
    #     except Exception as e:
    #         log.error(f'{LOG_PREFIX} - "Result":"Failure", "Reason":"{e}"')
    #         return None
    #

    def _add_ssi_evaluation(self, LOG_PREFIX, data):
        try:
            log.info(f"{LOG_PREFIX} - Received data: {data}")

            # Extract patient details with defaults if not provided
            patient_details = {
                'procedure_name': data.get('procedure_name', 'Not Provided'),
                'patient_id': data.get('patient_id', 'Not Provided'),
                'patient_name': data.get('patient_name', 'Unknown'),
                'age': data.get('age', 'Unknown'),
                'gender': data.get('gender', 'Not Specified'),
                'date_of_procedure': data.get('date_of_procedure', 'Not Provided'),
            }

            # Log to verify received data for evaluation fields
            log.info(
                f"{LOG_PREFIX} - Evaluation Fields in Data: {data.get('evaluation_fields', 'No Evaluation Fields Found')}")

            # Prepare evaluation fields by extracting dynamic keys
            evaluation_fields = {}

            # Iterate over dynamic fields and extract both choice and remarks for each
            for field in SSIEvaluationForm.dynamic_fields:
                choice_key = f"{field}_choice"
                remarks_key = f"{field}_remarks"

                # Check if the keys exist in data (log them for debugging)
                if choice_key in data:
                    choice_value = data.get(choice_key)
                    log.info(f"{LOG_PREFIX} - Found {choice_key}: {choice_value}")
                else:
                    choice_value = 'Not Specified'
                    log.warning(f"{LOG_PREFIX} - {choice_key} not found in data, defaulting to 'Not Specified'")

                if remarks_key in data:
                    remarks_value = data.get(remarks_key)
                    log.info(f"{LOG_PREFIX} - Found {remarks_key}: {remarks_value}")
                else:
                    remarks_value = 'No Remarks'
                    log.warning(f"{LOG_PREFIX} - {remarks_key} not found in data, defaulting to 'No Remarks'")

                # Log to see how the evaluation fields are being populated
                log.info(f"{LOG_PREFIX} - Field: {field}, Choice: {choice_value}, Remarks: {remarks_value}")

                # Add the evaluation field to the dictionary
                evaluation_fields[field] = {
                    'choice': choice_value,
                    'remarks': remarks_value
                }

            # Construct the full SSI evaluation data object
            data_dict = {
                'patient_details': patient_details,
                'evaluation_fields': evaluation_fields,
                'created_at': datetime.now(),
                'updated_at': datetime.now()
            }

            log.info(f"{LOG_PREFIX} - Successfully extracted SSI evaluation data: {data_dict}")

            # Insert the evaluation data into the database
            insert_ssi_evaluation_details = self.db_ssi_evaluation_details._insert(data=data_dict)

            log.info(f"{LOG_PREFIX} - Insert result: {insert_ssi_evaluation_details}")

            # Check if the insertion was successful
            if insert_ssi_evaluation_details and insert_ssi_evaluation_details.inserted_id:
                log.info(
                    f"{LOG_PREFIX} - SSI evaluation data inserted successfully with ID: {insert_ssi_evaluation_details.inserted_id}")
                return True
            else:
                log.error(f"{LOG_PREFIX} - Failed to insert SSI evaluation data.")
                return False

        except Exception as e:
            log.error(f'{LOG_PREFIX} - Error: {e}')
            return False

