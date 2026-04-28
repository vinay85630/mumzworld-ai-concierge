from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import json
import uvicorn

app = FastAPI(title="Mumzworld AI Concierge Backend")

# Enable CORS for the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mock Databases
with open('data/products.json', 'r', encoding='utf-8') as f:
    products_db = json.load(f)

with open('data/reviews.json', 'r', encoding='utf-8') as f:
    reviews_db = json.load(f)

class ShoppingItem(BaseModel):
    item: str
    priority: str
    suggested_product: Optional[dict] = None

class CalendarItem(BaseModel):
    event: str
    date: str

class AIResponse(BaseModel):
    shopping_list: List[ShoppingItem]
    calendar: List[CalendarItem]

@app.post("/process-text", response_model=AIResponse)
async def process_text(data: dict):
    text = data.get("text", "").lower()
    
    # Simple Agent Logic
    response = {"shopping_list": [], "calendar": []}
    
    if "remind" in text or "tomorrow" in text or "غداً" in text:
        response["calendar"].append({
            "event": text,
            "date": "2026-05-01"
        })
    else:
        # Match against catalog
        matched = None
        for p in products_db:
            if p["name"].lower() in text or any(t in text for t in p["tags"]):
                matched = p
                break
        
        response["shopping_list"].append({
            "item": text,
            "priority": "high" if "urgent" in text else "medium",
            "suggested_product": matched
        })
        
    return response

@app.get("/verdict/{product_id}")
async def get_verdict(product_id: str, lang: str = "en"):
    # In a real app, this would trigger an LLM synthesis
    is_ar = lang == "ar"
    return {
        "rating": 4.8,
        "summary": "تثق الأمهات بهذا المنتج..." if is_ar else "Moms trust this product...",
        "pros": ["Gentle", "Soft"] if not is_ar else ["لطيف", "ناعم"],
        "cons": ["Expensive"] if not is_ar else ["غالي"]
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
