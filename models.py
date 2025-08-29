from pydantic import BaseModel

class Match(BaseModel):
    home_team: str
    away_team: str
    home_score: int
    away_score: int

class Prediction(BaseModel):
    match: str
    predicted_winner: str
