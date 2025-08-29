# Premier League Live Game Predictor

Predict live Premier League match outcomes using Python, FastAPI, and machine learning. The project fetches real-time match data from the Football-Data.org API, processes it with Pandas, and predicts results using a logistic regression model.

## Features
- Live Premier League match data (teams, scores, fixtures)
- Data processing and ML predictions
- FastAPI endpoints (`/` welcome, `/predict` for JSON predictions)
- Terminal output for quick predictions
- Easily extensible with team form, head-to-head stats, or player data

## Project Structure
```
premier_league_predictor/
├── app/
│   ├── main.py       # FastAPI server + terminal script
│   ├── predictor.py  # Data fetching and ML predictions
│   ├── models.py     # API data models
│   ├── requirements.txt
│   └── .gitignore
├── README.md
└── .env.example      # Template for API key
```

## Setup
1. Clone the repo:  
```bash
git clone https://github.com/your-username/premier-league-predictor.git
cd premier-league-predictor
```
2. Create & activate a virtual environment:  
```bash
python -m venv .venv
source .venv/bin/activate  # Mac/Linux
.venv\Scripts\activate     # Windows
```
3. Install dependencies:  
```bash
pip install -r app/requirements.txt
```
4. Add your API key in `.env`:  
```
FOOTBALL_API_KEY=your_api_key_here
```
5. Run in terminal:  
```bash
python app/main.py
```
6. Or start the FastAPI server:  
```bash
uvicorn app.main:app --reload
```
Visit `http://127.0.0.1:8000/predict` for live predictions in JSON format.

## Why This Project is Impressive
- Demonstrates **API integration** with live sports data  
- Shows **data processing and machine learning** skills  
- Includes **backend development** with FastAPI  
- Fully extensible for more accurate predictions

## License
MIT License
