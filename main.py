from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.upload import router as upload_router
from routes.query import router as query_router

app = FastAPI(
    title="SmartDocQA API",
    description="Multi-company document Q&A system",
    version="1.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later restrict for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#  Routes
app.include_router(upload_router)
app.include_router(query_router)


#  Root check
@app.get("/")
def home():
    return {
        "status": "running 🚀",
        "message": "SmartDocQA API is live"
    }


# Health check (useful later)
@app.get("/health")
def health():
    return {"status": "ok"}