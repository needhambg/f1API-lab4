from pydantic import BaseModel

class Meeting(BaseModel):
    circuit_short_name:str
    meeting_key:int
    year:int
class Session(BaseModel):
    circuit_short_name:str
    year:int
    session_key:int
class Position(BaseModel):
    position:int
    session_key:int
driverlist = {
        1: "Max Verstappen",
        2: "Logan Sargeant",
        3: "Daniel Ricciardo",
        4: "Lando Norris",
        10: "Pierre Gasly",
        11: "Sergio Perez",
        14: "Fernando Alonso",
        16: "Charles Leclerc",
        18: "Lance Stroll",
        20: "Kevin Magnussen",
        22: "Yuki Tsunoda",
        23: "Alexander Albon",
        24: "Zhou Guanyu",
        27: "Nico Hulkenberg",
        30: "Liam Lawson",
        31: "Esteban Ocon",
        38: "Oliver Bearman",
        43: "Franco Colapinto",
        44: "Lewis Hamilton",
        50: "Oliver Bearman",
        55: "Carlos Sainz",
        61: "Jack Doohan",
        63: "George Russell",
        77: "Valtteri Bottas",
        81: "Oscar Piastri"
    }
circuitlist = {
    1: "Bahrain Grand Prix",
    2: "Saudi Arabian Grand Prix",
    3: "Australian Grand Prix",
    4: "Azerbaijan Grand Prix",
    5: "Miami Grand Prix",
    6: "Monaco Grand Prix",
    7: "Spanish Grand Prix",
    8: "Canadian Grand Prix",
    9: "Austrian Grand Prix",
    10: "British Grand Prix",
    11: "Hungarian Grand Prix",
    12: "Belgian Grand Prix",
    13: "Dutch Grand Prix",
    14: "Italian Grand Prix",
    15: "Singapore Grand Prix",
    16: "Japanese Grand Prix",
    17: "Qatar Grand Prix",
    18: "United States Grand Prix",
    19: "Mexico City Grand Prix",
    20: "São Paulo Grand Prix",
    21: "Las Vegas Grand Prix",
    22: "Abu Dhabi Grand Prix"
}
def Menu():
    print("-----------F1 API-----------")
    usrinput = int(input("1. Predict Drivers Next Race At A Circuit\n2. Find A Driver's Best At A Circuit\n3. Print Last Two Races\n4. Exit\n--------------------------\n"))
    return usrinput
def DriverMenu():
    drvrlpnum = 0
    while drvrlpnum == 0:
        print("----------Drivers----------")
        for val in driverlist:
            print(f"{val}: {driverlist[val]}")
        print("---------------------------")
        drivernum = int(input("Please Input A Driver Number: "))
        if drivernum in driverlist:
            drvrlpnum = 1
            return drivernum
        else:
            print("Number Is Not In Drivers' List")
def CircuitMenu():
    crctloopnum = 0
    while crctloopnum == 0:
        print("----------Circuits-----------\n")
        for val in circuitlist:
            print(f"{val}: {circuitlist[val]}")
        print("----------------------------")
        crctchc = int(input())
        if crctchc in circuitlist:
            crctloopnum = 1
            return circuitlist[crctchc]
        else:
            print("Circuit Num Not in List")   