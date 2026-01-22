from fastapi import FastAPI
from routers import metrics, aws

app = FastAPI(
    title= "Internal DevOps Utilities API",
    description= "This is an Internal API Utilities App for Monitoring metrics, AWS usages, log analysis etc.",
    version= "1.0.0",
    doc_url="/docs",
    redoc_url="/redoc"
)

@app.get("/test")
def hello():
    """
    This is the hello api just for testing.
    """
    return{"message":"Hello, This is a test api."}

app.include_router(metrics.router)
app.include_router(aws.router, prefix="/aws")