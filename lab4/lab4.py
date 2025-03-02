import requests
from pydantic import ValidationError
from models import Meeting, Session, Position, Menu, DriverMenu, CircuitMenu,driverlist
base_api_url = "https://api.openf1.org/v1/"
loopnum = 0
while loopnum != 1:
    # \/ Add Try Catches for Each Option
    #Menu
    try:
        usrchc = Menu()
        drvrchc = DriverMenu()
    except Exception as e:
        print(f"Entered Value Must Be an Integer: Exception | {e} | Thrown")
    #Switch Case
    match usrchc:
        case 1:
            try:
                #1. Predict Drivers Next Race At A Circuit 
                crctchc = CircuitMenu()
                meeting = requests.get(f"{base_api_url}meetings?year=2023&meeting_name={crctchc}")
                meeting2 = requests.get(f"{base_api_url}meetings?year=2024&meeting_name={crctchc}")
                if meeting.status_code == 200 and meeting2.status_code == 200:
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
                    print("Request failed. Status Code:",meeting.status_code,meeting2.status_code)
            except ValidationError:
                print("Invalid Input. Please Try Again")
        case 2:
            #2. Find A Driver's Best At A Circuit
            print
            if raceposition1.position < raceposition2.position:
                    print(f"{driverlist[drvrchc]}")
        case 3:
            #3. Print Last Two Races
            #Last meeting key is 1252
            try:
                race1 = requests.get(f"{base_api_url}sessions?meeting_key=1252&session_type=Race")
                race2 = requests.get(f"{base_api_url}sessions?meeting_key=1251&session_type=Race")
                rd1 = race1.json()
                rd2 = race2.json()
                d1 = Session(**rd1[0])
                d2 = Session(**rd2[0])
                r1posreq = requests.get(f"{base_api_url}position?session_key={d1.session_key}&driver_number={drvrchc}")
                r2posreq = requests.get(f"{base_api_url}position?session_key={d2.session_key}&driver_number={drvrchc}")
                r1posjson = r1posreq.json()
                r2posjson = r2posreq.json()
                raceposition1 = Position(**r1posjson[-1])
                raceposition2 = Position(**r2posjson[-1])
                print(f"Most Recent: {driverlist[drvrchc]} | {d1.circuit_short_name} | Position: {raceposition1.position}\nPrevious: {driverlist[drvrchc]} | {d2.circuit_short_name} | Position: {raceposition2.position}")
            except Exception as e:
                print(f"Error Ocurred. Exception: {e}")