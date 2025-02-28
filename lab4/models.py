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