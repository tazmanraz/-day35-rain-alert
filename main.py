import requests
from twilio.rest import Client
import os


api_key = "XXXXX"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

account_sid = "XXXXX"
auth_token = "XXXXXX"

# FOR TORONTO - UNCOMMENT AND COMMENT OUT BUENOS AIRES
# weather_params = {
#     "lat":43.653225,
#     "lon":-79.383186,
#     "appid": api_key,
#     "exclude": "current,minutely,daily,alerts"

# }

# FOR BUENOS AIRES TESTING RAIN
weather_params = {
    "lat":-34.603683,
    "lon":-58.381557,
    "appid": api_key,
    "exclude": "current,minutely,daily,alerts"
}

response = requests.get(OWM_Endpoint, params = weather_params)
response.raise_for_status()

weather_data =response.json()

derp = weather_data["hourly"][0]["weather"][0]["id"]
print(derp)

weather_slice = weather_data["hourly"][:12]
will_rain=False
will_snow=False

for n in weather_slice:
    if n["weather"][0]["id"] < 600:
        print("ITS RAINING SIDEWAYS")
        will_rain = True
    if 700 < n["weather"][0]["id"] <= 600:
        will_snow = True
    else:
        print("NO MORE RAIN")

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="Its gonna rain today. Please remember to send an umbrella",
        from_='+15614048649',
        to='+16475028583'
    )

    print(message.status)

if will_snow:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="Its gonna snow today. Leave earlier and bundle up",
        from_='+15614048649',
        to='+16475028583'
    )

    print(message.status)
