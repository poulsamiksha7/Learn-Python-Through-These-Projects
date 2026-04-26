import requests
import json
import pyttsx3

if __name__ == '__main__':
    text_to_speech = pyttsx3.init()

    city = input("Enter the name of the city: ")

    url = f"http://api.weatherapi.com/v1/current.json?key=f15f0748b6cb4039b26200800252909&q={city}"

    try:
        r = requests.get(url)
        r.raise_for_status()
        wdic = r.json()

        w = wdic["current"]["temp_c"]
        message = f"The current weather in {city} is {w} degrees Celsius."

        print(message)
        text_to_speech.say(message)
        text_to_speech.runAndWait()

    except Exception as e:
        print("Error fetching weather:", e)
