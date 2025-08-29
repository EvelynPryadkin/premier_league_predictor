from fastapi import FastAPI
from predictor import MatchPredictor
from models import Prediction

app = FastAPI()
predictor = MatchPredictor()

@app.get("/")
def root():
    return {"message": "Welcome to Premier League Live Game Predictor!"}

@app.get("/predict")
def get_predictions():
    matches = predictor.fetch_live_matches()
    df = predictor.prepare_data(matches)
    predictor.train(df)

    predictions = {}
    for _, match in df.iterrows():
        outcome = predictor.predict(match["Home Score"], match["Away Score"])
        match_name = f"{match['Home Team']} vs {match['Away Team']}"
        predictions[match_name] = outcome
    return predictions

if __name__ == "__main__":
    print("Fetching live Premier League matches and predicting winners...\n")
    matches = predictor.fetch_live_matches()
    df = predictor.prepare_data(matches)
    predictor.train(df)

    if df.empty:
        print("No live or completed match data available.")
    else:
        for _, match in df.iterrows():
            outcome = predictor.predict(match["Home Score"], match["Away Score"])
            print(f"{match['Home Team']} vs {match['Away Team']} --> {outcome}")
