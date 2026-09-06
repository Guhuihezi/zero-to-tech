from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from pypinyin import lazy_pinyin,Style
from snownlp import SnowNLP
from datetime import datetime, timezone
from storage import  init_db, save_record, get_history


init_db()

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

def score_label(score):
    if score >=0.6:
        return "偏积极"
    elif score <=0.4:
        return "偏消极"
    else:
        return "中性"

@app.get("/api/profile")
def get_profile():
    return profile

@app.post("/api/analyze")
def analyze(req:AnalyzeRequest):
    text = req.text
    score = round(SnowNLP(text).sentiments,2)
    res = {
        "text": req.text,
        "score": score,
        "label": score_label(score),
        "pinyin":" ".join(lazy_pinyin(text,style=Style.TONE)),
        "created_at": datetime.now(timezone.utc).isoformat(timespec="seconds")
    }
    save_record(res)
    return res

@app.get("/api/history") 
def history():
    return get_history(10)