import tkinter as tk
import requests
from PIL import Image, ImageTk #TK image support
from pathlib import Path
import os

API_KEY = os.getenv("API_KEY")
BASE_URL = "http://api.weatherapi.com/v1/current.json"

#Function to get API calls
def get_weather(city):
    url = f"{BASE_URL}?key={API_KEY}&q={city}&aqi=no"
    response = requests.get(url)
    return response.json()

#Show Weather Funtion
def show_weather():
    city= entry.get()
    weather = get_weather(city)

    #Check if city is real
    if "error" in weather:
        result_label.config(text = "Error! Please Enter Valid City")
    else:
        location = weather["location"]["name"] + ", " + weather["location"]["country"]
        condition = weather["current"]["condition"]["text"]
        temp_f = weather["current"]["temp_f"]
        feelslike = weather["current"]["feelslike_f"]
        result_label.config(text= f"{location}\n{condition}\nTemp:{temp_f}°F (Feels like {feelslike}°F)")





#Create Window and Entry
root = tk.Tk()
root.title("Simple Weather App")

#Entry Variable
entry = tk.Entry(root,width=40, font=("Helevetica",12))
entry.pack(pady=10)

#Button Instanciate
button = tk.Button(root,text = "Get Weather",command = show_weather)
button.pack(pady=5)

#Create label for showing weather
result_label = tk.Label(root,text ="", font=("Helvetica",12))
result_label.pack(pady=20)

#Create Picture for weather type
curr_dir = Path(__file__).parent.resolve()
img = Image.open(str(curr_dir)+"\sunny.png")
img = ImageTk.PhotoImage(img) # conver to TK image
weather_picture = tk.Button(root,image=img,command=None)
weather_picture.pack()

#Start Application Loop
root.mainloop()
