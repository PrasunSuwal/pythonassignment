import requests;
import json

def info(city,temp):
 
    if temp>40:
      print("Too hot don't go.");
    elif temp>=30:
      print("Go It's fine.");
    elif temp>=20:
      print("Chill. But you can make it work.");
    elif temp>=10:
      print("It's starting to get cold in here. Don't go maybe.");
    else:
        print("Damnn, It's too cold in %s. Don't go." %city)


count=0;


while 1 or count==5 :
    count +=1;
    city=input("Input city name:");
    url='https://api.openweathermap.org/data/2.5/weather?units=metric&q=%s&appid=09195acd9dfbb927b7f6b925bba707ed'

    response_API = requests.get(url % city)
    if(response_API.status_code==200):
        
        data=response_API.text
        weatherData=json.loads(data)
        info(city,weatherData['main']['temp'])
        break

    else:
        print("Fetch api error %d"%response_API.status_code)
        print("Try again. Make sure that the spelling is correct.")
        continue;

