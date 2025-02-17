from google.cloud import aiplatform

test_values1 = {
    'Amount': "9",
    'Time': "9:00 AM",
    'V1': "30",
    'V2': "29",
    'V3': "23",
    'V4': "21",
    'V5': "23",
    'V6': "23",
    'V7': "32",
    'V8': "45",
    'V9': "26"
}

test_values2 = {
    'Amount': "9",
    'Time': "9:00 AM",
    'V1': "25",
    'V2': "35",
    'V3': "40",
    'V4': "4",
    'V5': "50",
    'V6': "90",
    'V7': "30",
    'V8': "44",
    'V9': "20"
}

endpoint = aiplatform.Endpoint(
    endpoint_name='projects/PROJ_ID/locations/REGION/endpoints/ENDPOINT_ID'
    #endpoint_name='projects/PROJECT_ID/locations/REGION/endpoints/ENDPOINT_ID'
)

predec_responses = endpoint.predict([test_values2, test_values1])
print("Predection for both Dictionaries")
predec_responses




# Predection for both Dictionaries
# Prediction(predictions=[{'classes': ['1', '0'], 'scores': [0.4792671799659729, 0.5207328200340271]}, {'classes': ['1', '0'], 'scores': [0.5003806352615356, 0.4996193945407867]}], 
# deployed_model_id='ID', metadata=None, model_version_id='1', model_resource_name='projects/NUM/locations/REGION/models/ID', explanations=None)

# COMMAND fetching the endpoint ID
# gcloud ai endpoints list