from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

import os

app = FastAPI()

# Allow CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://contact-u87u.onrender.com"],  # your frontend domain
    allow_credentials=True,
    allow_methods=["*"],   # or ["POST", "GET"] if you want to restrict
    allow_headers=["*"],
)



# ✅ Serve React Frontend Build
if os.path.exists("web"):
    app.mount("/", StaticFiles(directory="web", html=True), name="frontend")

@app.get("/")
async def root():
    return {"message": "E-Commerce API is running"}