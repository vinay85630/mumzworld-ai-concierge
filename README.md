# Mumzworld Voice Shopping Assistant (AI Engineering Prototype)

## The Problem
Moms are some of the busiest people on the planet. Navigating a catalog of 100k+ products while holding a baby or multitasking is a major friction point. Typing "Pampers Size 4" into a search bar is slow.

**The Solution:** A voice-first AI concierge that converts quick, messy voice notes into structured shopping lists and calendar reminders, automatically matched against the Mumzworld catalog.

---

## 🚀 Key Features
- **Multilingual Voice Processing:** Supports English and Arabic (Native flow, not just literal translation).
- **Conversational Voice Feedback:** The assistant speaks recommendations back to the user in their preferred language (EN/AR).
- **Agentic Intent Routing:** Automatically distinguishes between "Shopping" (items to buy) and "Calendar" (tasks/reminders).
- **Multimodal Image-to-PDP:** Scan a product image to generate launch-ready product content in EN and AR with high confidence.
- **Groundedness Guardrails:** "MumzGuard" logic verifies every suggestion against the catalog to prevent hallucinations.
- **Structured Data Extraction:** Converts natural language into validated JSON schema.
- **Product Grounding (RAG):** Matches extracted entities against a real product catalog to suggest specific Mumzworld items.
- **"Moms Verdict" Synthesis:** Aggregates and summarizes customer reviews into a structured pro/con list and rating (multilingual).
- **MumzPulse (Ops View):** Detects operational trends and anomalies from user data to provide business insights.

---

## 🛠 Tech Stack & Architecture
- **Backend:** FastAPI (Python), Pydantic, Uvicorn.
- **Frontend:** Vanilla JS, HTML5 (Web Speech API), CSS3 (Glassmorphism).
- **AI Logic:** Dual-mode Engine (Python Backend + JS Local Fallback).
- **Data Layer:** JSON-based catalog & reviews (Mocked RAG source).

### Why this architecture?
1. **Voice-First:** Minimizes cognitive load for busy parents.
2. **Structured Output:** By converting voice to JSON, we can easily pipe this data into a checkout flow or a CRM.
3. **Multilingual by Design:** Arabic support is not an afterthought; the engine handles RTL layouts and Arabic entity matching.

---

## 🏃 How to Run (Under 5 Minutes)
1. **Quick Start (Windows):** Right-click `start_project.ps1` and select "Run with PowerShell". This will automatically install dependencies and launch both the Backend and Frontend.
2. **Manual Start:**
   - **Backend:** `pip install -r requirements.txt; python main.py` (Port 8001)
   - **Frontend:** `npm run dev` (Port 3000)
3. **Access:** Open [http://localhost:3000](http://localhost:3000) in Chrome/Edge.

---

## 📊 AI Evaluations & Testing
The prototype features a formal data-driven testing approach:
- **`tests/test_suite.json`**: Contains Gold-standard test cases covering multilingual intent and grounding.
- **In-App Runner:** Click the "Run AI Evaluations" button in the UI to see live performance.

---

## 🗺️ Future Roadmap
1. **Real-World Integration:** Replace mock engines with **OpenAI Whisper (Voice)** and **Gemini 1.5 Pro (Vision)** for production-grade accuracy.
2. **Semantic Search:** Implement **Vector Embeddings (using Pinecone or Milvus)** for deep semantic product discovery beyond keyword matching.
3. **Personalization Engine:** Connect user history to the AI to provide milestone-specific proactive suggestions (e.g., "Your baby is 6 months old now—time for weaning essentials!").
4. **Mobile Native App:** Port this prototype to **React Native** or **Flutter** for a true on-the-go experience for moms.

---

**Developed for the AI Engineering Internship at Mumzworld.**
*Focusing on building things that feel like magic, but are grounded in engineering.*
