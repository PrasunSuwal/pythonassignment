import requests;
import json
response_API = requests.get('https://api.openweathermap.org/data/2.5/weather?units=metric&q=Patan,NP&appid=09195acd9dfbb927b7f6b925bba707ed')
if(response_API.status_code==200):
    data=response_API.text
    weatherData=json.loads(data)
    print(weatherData['main']['temp'])

else:
    print("Fetch api error %d"%response_API.status_code)