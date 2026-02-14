from fastapi import FastAPI

app = FastAPI(
    title="Kortex API",
    description="The brain behind the Student Operating System",
    version="0.1.0"
)

@app.get("/")
async def root():
    return {"message": "Welcome to Kortex API", "status": "online"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}