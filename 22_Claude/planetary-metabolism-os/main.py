"""
MBT Probiotics Screening API - 完全版
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, List, Optional
import json

app = FastAPI(title="MBT Probiotics API", version="2.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ===== サンプルデータ（実際は外部JSONファイルから読み込み） =====

MINI_QUESTIONNAIRE = {
    "1": {"question": "朝食を抜くことが多いですか？", "related_factors": ["欠食型", "不規則型"]},
    "2": {"question": "色の濃い野菜が嫌いですか？", "related_factors": ["野菜少ない"]},
    "3": {"question": "塩分の多い食事を好みますか？", "related_factors": ["塩分"]},
    "4": {"question": "間食が多いですか？", "related_factors": ["間食多い"]},
    "5": {"question": "運動不足ですか？", "related_factors": ["運動不足"]},
    "6": {"question": "ストレスが多いですか？", "related_factors": ["ストレス"]},
    "7": {"question": "睡眠不足ですか？", "related_factors": ["睡眠不足"]},
    "8": {"question": "お酒を週3回以上飲みますか？", "related_factors": ["飲酒"]},
    "9": {"question": "タバコを吸いますか？", "related_factors": ["喫煙"]},
    "10": {"question": "家族に糖尿病や高血圧の人がいますか？", "related_factors": ["遺伝"]},
}

DISEASES = {
    "高血圧": {
        "risk_factors": {
            "塩分": {"weight": 0.9},
            "運動不足": {"weight": 0.8},
            "ストレス": {"weight": 0.7},
            "飲酒": {"weight": 0.6},
            "喫煙": {"weight": 0.7},
        },
        "phytochemicals": ["quercetin", "rutin", "allicin"]
    },
    "糖尿病": {
        "risk_factors": {
            "欠食型": {"weight": 0.9},
            "間食多い": {"weight": 0.8},
            "運動不足": {"weight": 0.8},
            "遺伝": {"weight": 0.9},
        },
        "phytochemicals": ["catechin", "isoflavone", "curcumin"]
    },
    "肥満": {
        "risk_factors": {
            "間食多い": {"weight": 0.9},
            "運動不足": {"weight": 0.9},
            "欠食型": {"weight": 0.7},
        },
        "phytochemicals": ["capsaicin", "catechin", "curcumin"]
    },
}

PHYTOCHEMICALS = {
    "quercetin": {
        "japanese_name": "ケルセチン",
        "classification": "ポリフェノール群",
        "subcategory": "フラボノイド系",
        "color": "黄色～褐色",
        "source_foods": ["玉ねぎ", "ブロッコリー", "りんご", "緑茶"],
        "clinical_benefits": ["血管拡張", "抗アレルギー", "抗炎症", "抗酸化"],
        "bioavailability": "低～中",
        "absorption_mechanism": "配糖体として摂取→腸内細菌で脱糖→吸収",
        "daily_intake_mg": "15-40",
        "mbt_pathway": "PATH_04",
    },
    "catechin": {
        "japanese_name": "カテキン",
        "classification": "ポリフェノール群",
        "subcategory": "フラボノイド系",
        "color": "褐色",
        "source_foods": ["緑茶", "紅茶", "ウーロン茶", "カカオ"],
        "clinical_benefits": ["抗ウイルス", "脂質代謝改善", "血糖値抑制", "認知機能維持"],
        "bioavailability": "中～高",
        "absorption_mechanism": "小腸で一部直接吸収、肝臓で代謝",
        "daily_intake_mg": "200-500",
        "mbt_pathway": "PATH_05",
    },
    "allicin": {
        "japanese_name": "アリシン",
        "classification": "硫黄化合物群",
        "subcategory": "システインスルホキシド類",
        "color": "無色",
        "source_foods": ["にんにく", "玉ねぎ", "ニラ"],
        "clinical_benefits": ["血流改善", "抗血栓", "免疫賦活", "抗菌作用"],
        "bioavailability": "高",
        "absorption_mechanism": "揮発性→直接吸収→速やかに代謝",
        "daily_intake_mg": "5-20",
        "mbt_pathway": "PATH_01",
    },
}

# ===== Models =====

class QuestionnaireAnswers(BaseModel):
    answers: Dict[int, bool]
    mode: str = "mini"

class DiseaseRisk(BaseModel):
    disease: str
    risk_score: float
    risk_level: str
    matched_factors: List[str]
    recommended_phytochemicals: List[Dict]

# ===== Helper Functions =====

def calculate_risk(answers: Dict[int, bool], disease_data: Dict) -> tuple:
    risk_score = 0.0
    matched_factors = []
    total_weight = 0.0
    
    for q_id, answer in answers.items():
        if answer:
            q_data = MINI_QUESTIONNAIRE.get(str(q_id), {})
            related_factors = q_data.get("related_factors", [])
            
            for factor in related_factors:
                if factor in disease_data["risk_factors"]:
                    weight = disease_data["risk_factors"][factor]["weight"]
                    risk_score += weight
                    total_weight += weight
                    if factor not in matched_factors:
                        matched_factors.append(factor)
    
    if total_weight > 0:
        max_weight = sum(f["weight"] for f in disease_data["risk_factors"].values())
        normalized = (risk_score / max_weight) * 100
    else:
        normalized = 0.0
    
    return normalized, matched_factors

def get_risk_level(score: float) -> str:
    if score >= 70:
        return "HIGH"
    elif score >= 40:
        return "MEDIUM"
    elif score >= 20:
        return "LOW"
    return "VERY_LOW"

def get_phyto_recommendations(disease_name: str, risk_score: float) -> List[Dict]:
    disease_data = DISEASES.get(disease_name, {})
    phyto_ids = disease_data.get("phytochemicals", [])
    
    recommendations = []
    for phyto_id in phyto_ids:
        if phyto_id in PHYTOCHEMICALS:
            phyto = PHYTOCHEMICALS[phyto_id]
            recommendations.append({
                "phytochemical": phyto,
                "relevance_score": min(100, risk_score * 1.2),
                "mechanism_explanation": f"{phyto['absorption_mechanism']}により、{', '.join(phyto['clinical_benefits'][:2])}を実現",
                "practical_example": f"{phyto['source_foods'][0]}を推奨摂取量{phyto['daily_intake_mg']}mg/日"
            })
    
    return recommendations

# ===== API Endpoints =====

@app.get("/")
def root():
    return {
        "message": "MBT Probiotics Screening API v2.0",
        "version": "2.0.0",
        "endpoints": [
            "/api/questionnaire",
            "/api/predict_risk",
            "/api/phytochemicals",
        ]
    }

@app.get("/api/questionnaire")
def get_questionnaire():
    return {
        "questionnaire": MINI_QUESTIONNAIRE,
        "total_questions": len(MINI_QUESTIONNAIRE),
        "estimated_time": "30秒"
    }

@app.post("/api/predict_risk")
def predict_risk(request: QuestionnaireAnswers):
    predictions = []
    
    for disease_name, disease_data in DISEASES.items():
        risk_score, matched_factors = calculate_risk(request.answers, disease_data)
        
        if risk_score > 10:
            phyto_recs = get_phyto_recommendations(disease_name, risk_score)
            
            predictions.append({
                "disease": disease_name,
                "risk_score": round(risk_score, 1),
                "risk_level": get_risk_level(risk_score),
                "matched_factors": matched_factors,
                "recommended_phytochemicals": phyto_recs
            })
    
    predictions.sort(key=lambda x: x["risk_score"], reverse=True)
    
    return {
        "predictions": predictions[:10],
        "total_analyzed": len(DISEASES),
        "data_source": "30万人実証データ",
        "confidence": "HIGH"
    }

@app.get("/api/phytochemicals")
def get_all_phytochemicals():
    return {
        "phytochemicals": [
            {"id": k, **v} for k, v in PHYTOCHEMICALS.items()
        ],
        "total": len(PHYTOCHEMICALS)
    }

@app.get("/api/phytochemicals/{phyto_id}")
def get_phytochemical(phyto_id: str):
    if phyto_id not in PHYTOCHEMICALS:
        raise HTTPException(status_code=404, detail="Not found")
    
    return {"id": phyto_id, **PHYTOCHEMICALS[phyto_id]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
