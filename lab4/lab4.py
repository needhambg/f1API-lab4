import requests
from pydantic import ValidationError
from models import Meeting, Session
base_api_url = "https://api.openf1.org/v1/"
drivernum = int(input("Input a Driver Number: "))
meeting = requests.get(f"{base_api_url}meetings?year=2023&circuit_short_name=Singapore")
if meeting.status_code == 200:
    data = meeting.json()
    
    if data:  
        try:
            singapore = Meeting(**data[0])
            result = requests.get(f"{base_api_url}sessions?meeting_key={singapore.meeting_key}&session_type=Race")
            print(result.json())
            sess_data = result.json()
            session = Session(**sess_data[0])
            result2 = requests.get(f"{base_api_url}position?session_key={session.session_key}&driver_number={drivernum}")
            data2 = result2.json()
            objlst = data2[-1]
            print(objlst)
        except ValidationError as e:
            print("Validation Error:", e)
    else:
        print("No meeting found.")
else:
    print