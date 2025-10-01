import tkinter as tk
import requests

API_KEY = "593a3d11a2684a56959214937250110"
BASE_URL = "http://api.weatherapi.com/v1/current.json"

def get_weather(city):
    url = f"{BASE_URL}?key={API_KEY}&q={city}&aqi=no"
    response = requests.get(url)
    return response.json()

def show_weather():
    city = entry.get()   # <-- this only works if entry is declared already
    weather = get_weather(city)

    if "error" in weather:
        result_label.config(text="❌ City not found!")
    else:
        location = weather["location"]["name"] + ", " + weather["location"]["country"]
        condition = weather["current"]["condition"]["text"]
        temp_c = weather["current"]["temp_c"]
        feelslike = weather["current"]["feelslike_c"]

        result_label.config(
            text=f"{location}\n{condition}\nTemp: {temp_c}°C (Feels like {feelslike}°C)"
        )

root = tk.Tk()
root.title("Weather App")

entry = tk.Entry(root, width=30, font=("Helvetica", 12))  # <-- declare BEFORE using it
entry.pack(pady=10)

button = tk.Button(root, text="Get Weather", command=show_weather)
button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=20)

root.mainloop()

