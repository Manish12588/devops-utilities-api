import boto3
from datetime import datetime, timezone, timedelta


def get_bucket_info():
    s3_client = boto3.client("s3")
    buckets = s3_client.list_buckets()["Buckets"]

    current_date =datetime.now(timezone.utc).astimezone()
    print(current_date)

    new_bukcets=[]
    old_bukcets=[]
    for bucket in buckets:
        bucket_name = bucket["Name"]
        creation_date = bucket["CreationDate"]

        days_ago_90 = current_date - timedelta(days=90)
        if creation_date < days_ago_90:
            old_bukcets.append(bucket_name)
        else:
            new_bukcets.append(bucket_name)
    return {
        "total_buckets":len(buckets),
        "new_buckets": len(new_bukcets),
        "old_buckets": len(old_bukcets),
        "new_bucket_names":new_bukcets,
        "old_bucket_names":old_bukcets
    }