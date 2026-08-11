import os
import uvicorn
from fastapi import FastAPI

app = FastAPI(title="Deployment App")

@app.get("/")
def home():
    return {
        "status": "Joothan",
        "message": "Njaan JOOOOTHEEEEESH! Goyim Poristein"
    }

if __name__ == "__main__":
    # Dynamically bind to the platform's assigned PORT and listen on all interfaces
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("app:app", host="0.0.0.0", port=port, reload=False)
