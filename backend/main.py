from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

profile = {
    "heroTitle":"About Me",
    "heroSubtitle":"Projects, ideas, inspirations, insights, my works"
}

class AnalyzeRequest(BaseModel): 
    text: str

@app.get("/api/profile")
def get_profile():
    return profile

@app.post("/api/analyze")
def analyze(req:AnalyzeRequest):
    return {
        "text": req.text,
        "score": 0.6,
        "label":"偏平静",
        "pinyin":"暂无"
    }