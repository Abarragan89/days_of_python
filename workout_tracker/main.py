from dotenv import load_dotenv
import os
import requests
from datetime import datetime

load_dotenv()

NUTRITION_API_KEY = os.getenv("NUTRITION_API_KEY")
NUTRITION_ID = os.getenv("NUTRITION_ID")


# Add exercise data to Google Sheets using Sheety
def add_workout(workout):
    """Creates workout instance in Sheety"""
    today = datetime.now()
    date = today.strftime("%b-%8-%Y")
    time = today.strftime("%-I:%M%p")

    sheety_post_endpoint = "https://api.sheety.co/dfdd26d04cb8a8c2d20e1e57a8d70b8b/workouts/workouts"
    sheety_post_headers = {
        "Content-Type": "application/json",
    }
    sheety_post_payload = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": workout["name"],
            "duration": workout["duration_min"],
            "calories": workout["nf_calories"]
        }
    }
    sheety_response = requests.post(url=sheety_post_endpoint, json=sheety_post_payload, headers=sheety_post_headers)
    sheety_response.raise_for_status()


# Create exercise data using natural language
add_exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

add_exercise_headers = {
    "x-app-id": NUTRITION_ID,
    "x-app-key": NUTRITION_API_KEY,
    "x-remote-user-id": "0"
}

add_exercise_post_data = {
    "query": input("What were your exercises today?"),
    "gender": "male",
    "weight_kg": "72.5",
    "height_cm": "165",
    "age": "33"
}

response = requests.post(url=add_exercise_endpoint, json=add_exercise_post_data, headers=add_exercise_headers)
response.raise_for_status()
response = response.json()
workout_list = response['exercises']

for workout in workout_list:
    add_workout(workout)
