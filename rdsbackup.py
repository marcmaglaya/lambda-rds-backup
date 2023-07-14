import boto3

def get_current_timestamp():
    # Return the current timestamp in a specific format
    import datetime
    return datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

# Define the RDS instance and snapshot identifier
rds_instance_id = 'YOUR_RDS_INSTANCE_ID'
snapshot_identifier = 'snapshot-{}'.format(get_current_timestamp())

# Create a new RDS client
rds_client = boto3.client('rds')

# Create the RDS instance snapshot
response = rds_client.create_db_snapshot(
    DBInstanceIdentifier=rds_instance_id,
    DBSnapshotIdentifier=snapshot_identifier
)

# Print the response for debugging purposes
print(response)


