import requests
import pandas as pd
from sklearn.linear_model import LogisticRegression
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("FOOTBALL_API_KEY")
API_URL = "https://api.football-data.org/v4/competitions/PL/matches"

class MatchPredictor:
    def __init__(self):
        self.model = LogisticRegression()
        self.trained = False

    def fetch_live_matches(self):
        headers = {"X-Auth-Token": API_KEY}
        response = requests.get(API_URL, headers=headers)
        matches = response.json().get("matches", [])
        return matches

    def prepare_data(self, matches):
        data = []
        for match in matches:
            home_team = match["homeTeam"]["name"]
            away_team = match["awayTeam"]["name"]
            home_score = match["score"]["fullTime"]["home"] or 0
            away_score = match["score"]["fullTime"]["away"] or 0
            data.append([home_team, away_team, home_score, away_score])
        df = pd.DataFrame(data, columns=["Home Team", "Away Team", "Home Score", "Away Score"])
        return df

    def train(self, df):
        df["Home Win"] = df["Home Score"] > df["Away Score"]
        X = df[["Home Score", "Away Score"]]
        y = df["Home Win"]
        if len(X) > 0:
            self.model.fit(X, y)
            self.trained = True

    def predict(self, home_score, away_score):
        if not self.trained:
            return "Model not trained yet"
        prediction = self.model.predict([[home_score, away_score]])
        return "Home Win" if prediction == 1 else "Away Win"
