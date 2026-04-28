# Mumzworld AI Concierge - Start Script
# This script launches both the FastAPI backend and the Vite/Serve frontend.

Write-Host "🚀 Starting Mumzworld AI Concierge Stack..." -ForegroundColor Cyan

# 1. Start FastAPI Backend in a new window
Write-Host "📦 Launching Backend (FastAPI) on port 8001..." -ForegroundColor Green
Start-Process powershell -ArgumentList "-NoExit", "-Command", "pip install -r requirements.txt; python main.py"

# 2. Start Frontend
Write-Host "🎨 Launching Frontend on port 3000..." -ForegroundColor Magenta
npm run dev
