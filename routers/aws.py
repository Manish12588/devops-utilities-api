from fastapi import APIRouter, HTTPException
from services.aws_services import get_bucket_info

router = APIRouter()

@router.get("/s3",status_code=200)
def get_buckets():
    """
    This API gets informatio of S3 buckets 
    """
    try:
        bucket_info = get_bucket_info()
        return bucket_info
    except:
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error."
        )

@router.get("/ec2",status_code=200)
def get_instances():
    """
    This API gets informatio of EC2 Instances.
    """
    try:
        return {"message":"EC2 Utilities in progress..."}
    except:
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error."
        )
