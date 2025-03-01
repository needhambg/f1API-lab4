import requests
from pydantic import ValidationError
from models import Meeting, Session, Position, Menu, DriverMenu
base_api_url = "https://api.openf1.org/v1/"
loopnum = 0
while loopnum != 1:
    # \/ Add Try Catches for Each Option
    #Menu
    usrchc = Menu()
    drvrchc = DriverMenu()
    #drivernum = int(input("Input a Driver Number: "))
    #meeting = requests.get(f"{base_api_url}meetings?year=2023&circuit_short_name=Singapore")
    #data = meeting.json()
    #singapore = Meeting(**data[0])
    #result = requests.get(f"{base_api_url}sessions?meeting_key={singapore.meeting_key}&session_type=Race")
    #sess_data = result.json()
    #session = Session(**sess_data[0])
    #result2 = requests.get(f"{base_api_url}position?session_key={session.session_key}&driver_number={drivernum}")
    #data2 = result2.json()
    #position = Position()
    #print(position.position)
    #Predict Drivers Next Race at A Circuit
        #Give User List of Drivers,take input
    #Find A Driver's Best Race, Quali, Sprint, Or Practice
    #Print Last Two Races