#Step 1: create our visrtual Envioroment
#Step 2: import boto3 and setup default session
import boto3
boto3. setup_default_session(profile_name='johnnytrinh47')
#Step 3: look at Python API documentation for S3 SDK
#Step 4: Create a Function
def createS3Bucket():
    #Step 5: Create a client
    client = boto3.client('s3')
#Step 6: look for the create bucket reference
    response = client.create_bucket(
         Bucket = "sdkjtrinh"
    )

    print(response)
createS3Bucket()