import requests
from pydantic import ValidationError
from models import Meeting, Session, Position, Menu, DriverMenu, CircuitMenu
base_api_url = "https://api.openf1.org/v1/"
loopnum = 0
while loopnum != 1:
    # \/ Add Try Catches for Each Option
    #Menu
    usrchc = Menu()
    drvrchc = DriverMenu()
    
    #Switch Case
    match usrchc:
        case 1:
            #1. Predict Drivers Next Race At A Circuit 
            crctchc = CircuitMenu()
            meeting = requests.get(f"{base_api_url}meetings?year=2023&circuit_short_name={crctchc}")
            meeting2 = requests.get(f"{base_api_url}meetings?year=2024&circuit_short_name={crctchc}")
            data = meeting.json()
            r1 = Meeting(**data[0])
            print(r1.meeting_key)
            data2 = meeting2.json()
            r2 = Meeting(**data2[0])
            print(r2.meeting_key)
            #race = Meeting(**data[0])
            #result = requests.get(f"{base_api_url}sessions?meeting_key={race.meeting_key}&session_type=Race")
            #sess_data = result.json()
            #session = Session(**sess_data[0])
            #result2 = requests.get(f"{base_api_url}position?session_key={session.session_key}&driver_number={drvrchc}")
            #position = Position()
            #print(position.position)
            
        case 2:
            #2. Find A Driver's Best At A Circuit
            print
        case 3:
            #3. Print Last Two Races
            print