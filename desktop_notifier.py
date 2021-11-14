import datetime
import time 
import requests
from plyer import notification

#let there is no data initially
covidData = None
try:
    covidData = requests.get("https://corona-rest-api.herokuapp.com/Api/india")
except:

    print("Please! Check your internet connection")

#if we fetched data
if (covidData != None):

    data = covidData.json()['Success']

    while(True):
        notification.notify(

            title = "COVID19 Stats on {}".format(datetime.date.today()),

            message = "Total cases : {totalcases}\nToday cases : {todaycases}\nToday deaths :{todaydeaths}\nTotal active :{active}".format(
                        totalcases = data['cases'],
                        todaycases = data['todayCases'],
                        todaydeaths = data['todayDeaths'],
                        active = data["active"]),  


            app_icon = "notifications_icon.ico",

            timeout  = 60
        )

        time.sleep(60*60*10)