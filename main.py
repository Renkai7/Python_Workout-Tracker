import os
import requests

APP_ID = os.environ.get("NUTR_ID")
APP_KEY = os.environ.get("NUTR_API_KEY")

exercise_query = input("What exercise(s) did you do?")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
    "x-remote-user-id": "0"
}

exercise_parameters = {
    "query": exercise_query,
    "gender": "male",
    "weight_kg": 70,
    "height_cm": 180,
    "age": 30
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

post_exercise = requests.post(exercise_endpoint, json=exercise_parameters,  headers=headers)
results = post_exercise.json()
print(results)
