from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

import os

app = FastAPI()





# ✅ Serve React Frontend Build
if os.path.exists("web"):
    app.mount("/", StaticFiles(directory="web", html=True), name="frontend")

@app.get("/")
async def root():
    return {"message": "E-Commerce API is running"}