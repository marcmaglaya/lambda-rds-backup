import boto3
import os
from datetime import datetime, timedelta, timezone

def lambda_handler(event, context):
    rds_instance_id=os.getenv('RDS_INSTANCE_ID')
    # Define the RDS instance and the maximum age of snapshots to be deleted
    max_snapshot_age = 35

    # Calculate the deletion threshold timestamp
    threshold_timestamp = datetime.now(timezone.utc) - timedelta(days=max_snapshot_age)
    print(threshold_timestamp)
    # Create a new RDS client
    rds_client = boto3.client('rds')

    # Retrieve all snapshots for the RDS instance
    response = rds_client.describe_db_snapshots(
        DBInstanceIdentifier=rds_instance_id
    )

    # Store snapshots that exceed the threshold
    snapshots_to_delete = []

    # Iterate over the snapshots and delete those that exceed the threshold
    for snapshot in response['DBSnapshots']:
        snapshot_identifier = snapshot['DBSnapshotIdentifier']
        snapshot_create_time = snapshot['SnapshotCreateTime']
        
        if snapshot_create_time < threshold_timestamp:
            print(f"Snapshot: {snapshot_identifier}, Created At: {snapshot_create_time}")

        if snapshot_create_time < threshold_timestamp:
            # Delete the RDS snapshot
            response = rds_client.delete_db_snapshot(
                DBSnapshotIdentifier=snapshot_identifier
            )
    # Print all snapshots
    print("All Snapshots:")
    for snapshot in response['DBSnapshots']:
        snapshot_identifier = snapshot['DBSnapshotIdentifier']
        snapshot_create_time = snapshot['SnapshotCreateTime']
        print(f"Snapshot: {snapshot_identifier}, Created At: {snapshot_create_time}")
    
    # Print the snapshots that will be deleted
    print("Snapshots to Delete:")
    for snapshot_identifier in snapshots_to_delete:
        print(snapshot_identifier)


    # Delete the identified snapshots
    for snapshot_identifier in snapshots_to_delete:
        response = rds_client.delete_db_snapshot(
            DBSnapshotIdentifier=snapshot_identifier
        )


# Print the response for debugging purposes
    print(response)
    
