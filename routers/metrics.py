from fastapi import APIRouter, HTTPException
from services.metrics_service import get_system_metrics

router = APIRouter()

@router.get("/metrics",status_code=200)
def get_metrics():
    """
    This API gets the system metrics (CPU, Memory, Disk, System Health)
    based on CPU threshold i.e 10 (configurable)
    """
    try:
        metrics = get_system_metrics()
        return metrics
    except:
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error."
        )
