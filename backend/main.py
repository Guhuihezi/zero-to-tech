from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["GET", "POST"],
)

profile = {
  "heroTitle": "About me",
  "heroSubtitle": "Projects, ideas, inspirations, insights, my works",
  "featuredWork": {
    "kicker": "作品", 
    "title": "文字实验室",
    "copy": "拼音和情绪，挖掘中文里的细节",
    "linkLabel": "打开作品",
  },
  "identity": {
    "motto": "已识乾坤大，尤怜草木青",
    "learning": "零到全栈",
  }
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