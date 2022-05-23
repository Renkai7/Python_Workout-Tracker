import os
import requests
from datetime import datetime

APP_ID = os.environ.get("NUTR_ID")
APP_KEY = os.environ.get("NUTR_API_KEY")
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")

exercise_query = input("What exercise(s) did you do? ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
    "x-remote-user-id": "0"
}

auth_headers = {
    "Authorization": AUTH_TOKEN
}

exercise_parameters = {
    "query": exercise_query,
    "gender": "male",
    "weight_kg": 70,
    "height_cm": 180,
    "age": 30
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = os.environ.get("SHEET_ENDPOINT")

post_exercise = requests.post(exercise_endpoint, json=exercise_parameters,  headers=headers)
results = post_exercise.json()
print(results)

today_date = datetime.now().strftime("%Y/%m/%d")
time = datetime.now().strftime("%X")


for exercise in results["exercises"]:

    record_inputs = {
        "workout": {
            "date": today_date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_output = requests.post(
        sheety_endpoint,
        json=record_inputs,
        headers=auth_headers
    )
    print(sheet_output.text)
