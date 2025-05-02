import pickle
import os
import numpy as np
import logging

# Logger setup
log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
LOG_PREFIX = "SSI_PREDICTION"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, '..', 'ml_model')

try:
    with open(os.path.join(MODEL_DIR, 'ssi_model_1.pkl'), 'rb') as f:
        model = pickle.load(f)
    log.info(f"{LOG_PREFIX} - Model loaded successfully")

    with open(os.path.join(MODEL_DIR, 'scaler.pkl'), 'rb') as f:
        scaler = pickle.load(f)
    log.info(f"{LOG_PREFIX} - Scaler loaded successfully")

    with open(os.path.join(MODEL_DIR, 'label_encoders.pkl'), 'rb') as f:
        label_encoders = pickle.load(f)
    log.info(f"{LOG_PREFIX} - Label encoders loaded successfully")

except Exception as e:
    log.error(f'{LOG_PREFIX} - "Result":"Failure", "Reason":"{e}"')
    raise RuntimeError(f"Model/scaler/encoder loading failed: {e}")

def predict_ssi(patient_data):
    try:
        log.info(f"{LOG_PREFIX} - Starting prediction with data: {patient_data}")

        # Encode categorical fields
        for col in ['Sex', 'Patient on Steroid (Last 3 Months)', 'Regular Smoker',
                    'Regular Alcohol Consumer', 'Diabetic (HB1C)', 'E.coli']:
            encoder = label_encoders.get(col)
            if encoder and patient_data[col] in encoder.classes_:
                patient_data[col] = encoder.transform([patient_data[col]])[0]
            else:
                log.warning(f'{LOG_PREFIX} - Unknown or missing value for "{col}", defaulting to 0')
                patient_data[col] = 0

        # Get numeric fields
        numeric_values = [
            patient_data['Age (years)'],
            patient_data['Sex'],
            patient_data['Patient on Steroid (Last 3 Months)'],
            patient_data['Regular Smoker'],
            patient_data['Regular Alcohol Consumer'],
            patient_data['Diabetic (HB1C)'],
            patient_data['BMI_Final'],
            patient_data['Surgery_Duration_Final'],
            patient_data['E.coli']
        ]
        log.debug(f"{LOG_PREFIX} - Numeric values for scaling: {numeric_values}")

        # Add MIC values
        for i in range(1, 5):
            mic = patient_data.get(f'mic{i}', 0)
            interpretation = patient_data.get(f'interpretation{i}', '')
            try:
                mic = float(mic)
            except Exception as ex:
                log.warning(f'{LOG_PREFIX} - Invalid mic{i} value "{mic}", defaulting to 0: {ex}')
                mic = 0
            interpretation_val = 1 if interpretation == 'Resistant' else 0
            numeric_values.append(mic)
            numeric_values.append(interpretation_val)

        log.debug(f"{LOG_PREFIX} - Complete feature vector before scaling: {numeric_values}")

        # Scale input
        log.info(f"{LOG_PREFIX} - Expected scaler input size: {scaler.mean_.shape[0]}")
        log.info(f"{LOG_PREFIX} - Current input size: {len(numeric_values)}")

        scaled_input = scaler.transform([numeric_values])
        log.debug(f"{LOG_PREFIX} - Scaled input: {scaled_input}")

        # Predict
        prediction = model.predict(scaled_input)[0]
        log.info(f'{LOG_PREFIX} - "Result":"Success", "Prediction":{prediction}')
        return prediction

    except Exception as e:
        log.error(f'{LOG_PREFIX} - "Result":"Failure", "Reason":"{e}"')
        raise RuntimeError(f"Internal server error: {e}")


# def predict_ssi(patient_data):
#     try:
#         log.info(f"{LOG_PREFIX} - Starting prediction with data: {patient_data}")
#
#         # Encode categorical fields
#         for col in ['Sex', 'Patient on Steroid (Last 3 Months)', 'Regular Smoker',
#                     'Regular Alcohol Consumer', 'Diabetic (HB1C)', 'E.coli']:
#             encoder = label_encoders.get(col)
#             if encoder and patient_data[col] in encoder.classes_:
#                 patient_data[col] = encoder.transform([patient_data[col]])[0]
#             else:
#                 log.warning(f'{LOG_PREFIX} - Unknown or missing value for "{col}", defaulting to 0')
#                 patient_data[col] = 0
#
#         # Prepare final input features (exactly what the model was trained on — 13 features)
#         numeric_values = [
#             patient_data['Age (years)'],
#             patient_data['Sex'],
#             patient_data['Patient on Steroid (Last 3 Months)'],
#             patient_data['Regular Smoker'],
#             patient_data['Regular Alcohol Consumer'],
#             patient_data['Diabetic (HB1C)'],
#             patient_data['BMI_Final'],
#             patient_data['Surgery_Duration_Final'],
#             float(patient_data.get('mic1', 0)),
#             1 if patient_data.get('interpretation1') == 'Resistant' else 0,
#             float(patient_data.get('mic2', 0)),
#             1 if patient_data.get('interpretation2') == 'Resistant' else 0,
#             float(patient_data.get('mic3', 0))  # <- Stop here for 13 features
#             # (Note: mic4 and interpretation4 are ignored if model expects 13 features)
#         ]
#
#         log.info(f"{LOG_PREFIX} - Expected model input size: {len(model.feature_importances_)}")
#         log.info(f"{LOG_PREFIX} - Current input size: {len(numeric_values)}")
#
#         scaled_input = scaler.transform([numeric_values])
#
#         prediction = model.predict(scaled_input)[0]
#         log.info(f'{LOG_PREFIX} - "Result":"Success", "Prediction":{prediction}')
#         return prediction
#
#     except Exception as e:
#         log.error(f'{LOG_PREFIX} - "Result":"Failure", "Reason":"{e}"')
#         raise RuntimeError(f"Internal server error: {e}")
