import requests
from pydantic import ValidationError
from models import Meeting, Session, Position, Menu, DriverMenu, CircuitMenu,driverlist
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
            try:
                #1. Predict Drivers Next Race At A Circuit 
                crctchc = CircuitMenu()
                meeting = requests.get(f"{base_api_url}meetings?year=2023&meeting_name={crctchc}")
                meeting2 = requests.get(f"{base_api_url}meetings?year=2024&meeting_name={crctchc}")
                if meeting.status_code == 200:
                    data = meeting.json()
                    r1 = Meeting(**data[0])
                    data2 = meeting2.json()
                    r2 = Meeting(**data2[0])
                    s1 = requests.get(f"{base_api_url}sessions?meeting_key={r1.meeting_key}&session_type=Race")
                    s2 = requests.get(f"{base_api_url}sessions?meeting_key={r2.meeting_key}&session_type=Race")
                    sesjson = s1.json()
                    sesjson2 = s2.json()
                    session1 = Session(**sesjson[0])
                    session2 = Session(**sesjson[0])
                    p1 = requests.get(f"{base_api_url}position?session_key={session1.session_key}&driver_number={drvrchc}")
                    pos1 = p1.json()
                    position1 = Position(**pos1[-1])
                    p2 = requests.get(f"{base_api_url}position?session_key={session2.session_key}&driver_number={drvrchc}")
                    pos2 = p2.json()
                    position2 = Position(**pos2[-1])
                    predpos = round((position1.position + position2.position)/2)
                    print(f"{driverlist[drvrchc]} is predicted to place {predpos} at {crctchc} 2025!")
                else:
                    print("Request failed. Status Code:",meeting.status_code)
            except ValidationError:
                print("Invalid Input. Please Try Again")
        case 2:
            #2. Find A Driver's Best At A Circuit
            print
        case 3:
            #3. Print Last Two Races
            print