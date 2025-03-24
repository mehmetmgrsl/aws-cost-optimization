import boto3
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name='us-east-1')  # ensure correct region

    print("Step 1: Delete snapshots that are completed and linked to available volumes.")

    # List all snapshots
    snapshots_response = ec2.describe_snapshots(OwnerIds=['self'])

    # List all available (unattached) volumes
    volumes_response = ec2.describe_volumes(Filters=[
        {'Name': 'status', 'Values': ['available']}
    ])

    available_volume_ids = set(v['VolumeId'] for v in volumes_response['Volumes'])

    for snapshot in snapshots_response['Snapshots']:
        snapshot_id = snapshot['SnapshotId']
        volume_id = snapshot.get('VolumeId')
        state = snapshot.get('State')

        if volume_id in available_volume_ids and state == "completed":
            try:
                ec2.delete_snapshot(SnapshotId=snapshot_id)
                print(f"Deleted snapshot: {snapshot_id} (volume: {volume_id})")
            except ClientError as e:
                print(f"Failed to delete snapshot {snapshot_id}: {e}")
        else:
            print(f"Skipped snapshot: {snapshot_id} (state: {state}, volume: {volume_id})")

    print("\n Step 2: Delete volumes in 'available' state.")

    # Refresh volumes (in case something changed)
    volumes_response = ec2.describe_volumes(Filters=[
        {'Name': 'status', 'Values': ['available']}
    ])

    for volume in volumes_response['Volumes']:
        volume_id = volume['VolumeId']
        try:
            ec2.delete_volume(VolumeId=volume_id)
            print(f"Deleted volume: {volume_id}")
        except ClientError as e:
            print(f"Failed to delete volume {volume_id}: {e}")

if __name__ == "__main__":
    lambda_handler({}, {})
