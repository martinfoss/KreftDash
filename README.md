
# KreftDash

## Struktur
- `backend/` – FastAPI med CSV-data og API-endpoints
- `frontend/` – React-app med komponenter og visualisering

## Lokal kørsel

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm start
```

## Deployment på Render
1. Opret to services:
   - Web Service (backend)
   - Static Site (frontend)
2. Backend:
   - Build: `pip install -r requirements.txt`
   - Start: `uvicorn main:app --host 0.0.0.0 --port $PORT`
3. Frontend:
   - Build: `npm install && npm run build`
   - Publish dir: `build`

## API-endpoints
- `/kreftformer`
- `/regioner`
- `/data`
- `/statistikk`
