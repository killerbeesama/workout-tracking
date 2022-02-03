import requests
import datetime

GENDER = "<your gender>"
WEIGHT_KG = "<your weight>"
HEIGHT_CM = "<your height in cm>"
AGE = "<your age in int>"

exercise_text = input("Tell me which exercises you did: ")

NUTRITIONIX_ID = "<your id>"
NUTRITIONIX_API = "<you api key>"

SHEETY_BEARER_API = "<you api key>"

header = {
    "x-app-id": NUTRITIONIX_ID,
    "x-app-key": NUTRITIONIX_API,
}

parameter = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

nutrix_response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise", json=parameter,headers=header)
nutrix_data = nutrix_response.json()['exercises'][0]

duration_data = nutrix_data['duration_min']
calories_data = nutrix_data['nf_calories']
exercise_name = nutrix_data['name']

dt = datetime.datetime.now()
formated_date = dt.date().strftime('%d/%m/%Y')
formated_time = dt.time().strftime("%X")

sheety_parameter = {
    "workout": {
        "date": formated_date,
        "time": formated_time,
        "exercise": exercise_name.title(),
        "duration": duration_data,
        "calories": calories_data,
    }
}

sheety_header = {
    "Authorization": f"Bearer {SHEETY_BEARER_API}"
}

sheety_response = requests.post(url="<your endpoint>",
                                json=sheety_parameter, headers=sheety_header)
print(sheety_response.text)
