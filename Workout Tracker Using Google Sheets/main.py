import requests
import datetime as dt
import os

NUTRITIONIX_APP_ID = os.environ["APPID"]
NUTRITIONIX_API_KEY = os.environ["APIKEY"]
SHEETY_URL = os.environ["URL"]
BEARER_TOKEN =os.environ["BEARERTOKEN"]


DATE = str(dt.datetime.now()).split(' ')[0]
TIME = str(dt.datetime.now()).split(' ')[1].split('.')[0]

exercise_text = input("How did you exercise (example: I swam for 45 mins): ")
PARAMETER={
 "query":exercise_text,
 "gender":"female",
 "weight_kg":72.5,
 "height_cm":167.64,
 "age":30
}

headers = { "x-app-id" : NUTRITIONIX_APP_ID, "x-app-key" : NUTRITIONIX_API_KEY, "Content-Type" : "application/json"}

response = requests.post(url='https://trackapi.nutritionix.com/v2/natural/exercise',json=PARAMETER, headers=headers )
result = response.json()

sheet_inputs = {
        "workout": {
            "date": DATE,
            "time": TIME,
            "exercise": str(result['exercises'][0]["name"]).title(),
            "duration": result['exercises'][0]["duration_min"],
            "calories": result['exercises'][0]["nf_calories"]
        }
    }
sheet_headers={
     "Authorization" : f"Bearer {BEARER_TOKEN}"
}
sheet_response = requests.post(SHEETY_URL, json=sheet_inputs, headers = sheet_headers)

get_from_sheet = requests.get(url= SHEETY_URL)
