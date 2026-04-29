import uvicorn
from fastapi import FastAPI
from app.Controller.agent_controller import router as agent_router

app = FastAPI(
    title="Speech Therapy Agent",
    description="AI Agent for Child Speech Therapy",
    version="1.0.0"
)

# register routes
app.include_router(agent_router)


@app.get("/")
def health_check():
    return {"status": "Speech Therapy Agent Running"}


if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )