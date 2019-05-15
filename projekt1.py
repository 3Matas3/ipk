#!/usr/bin/env python3
import socket
import json
import sys


#passing arguments
api_key = sys.argv[1]
city = sys.argv[2]

host = 'api.openweathermap.org' #the server host name
port =  80 #the port used by the server

#preparing http request
msg = "/data/2.5/weather?q=" + city + '&appid=' + api_key + '&units=metric'
msg = 'GET ' + msg + ' HTTP/1.1\r\nHost: ' + host + '\r\n\r\n'

#APi call
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((host, port))
except:
    print("can not connect")
    print(sys.exit)
s.sendall(msg.encode())
weather_data = s.recv(1024)
try:
    s.close()
except:
    print("socket can not close")
    print(sys.exit)

weather_data = weather_data.decode()
data = json.dumps(weather_data)
test = "{" + weather_data.partition('{')[2] #splitting of recieved message

data = json.loads(test)

if data["cod"] == 200:
        if "name" in data:
            print(data["name"])
        else:
            print("none")

        if "weather" in data:
            for weather in data["weather"]:
                if "description" in weather:
                    print(weather["description"])
                else:
                    print('description: N/A')

        if "main" in data:
            if "temp" in data["main"]:
                print("temp: " + str(data["main"]["temp"]) + "°C")
            else:
                print('temp: N/A')
            if "humidity" in data["main"]:
                print("humidity: " + str(data["main"]["humidity"]) + "%")
            else:
                print('humidity: N/A')
            if "pressure" in data["main"]:
                print("pressure: " + str(data["main"]["pressure"]) + " hPa")
            else:
                print('pressure: N/A')
        
        if "wind" in data:
            if "speed" in data["wind"]:
                print("wind-speed: " + str(data["wind"]["speed"]*3.6) + "km/h")
            else:
                print('wind-speed: N/A')
            if "deg" in data["wind"]:
                print("wind-deg: " + str(data["wind"]["deg"]))
            else:
                print('wind-deg: N/A')
else:
        print("Invalid key or city name")
        print(sys.exit)
