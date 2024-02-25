import boto3

# Configure AWS credentials (replace with your actual credentials)
#AWS_ACCESS_KEY_ID = 'YOUR_AWS_ACCESS_KEY_ID'
#AWS_SECRET_ACCESS_KEY = 'YOUR_AWS_SECRET_ACCESS_KEY'

# Specify the file to upload, S3 bucket name, and desired key (object name)
file_to_upload = '/path/to/your/local/file.txt'  # Replace with your file path
bucket_name = 'your-s3-bucket-name'  # Replace with your bucket name
s3_key = 'key/for/file/in/s3.txt'  # Replace with your desired object name

# Create an S3 client
#s3 = boto3.client('s3',
#                  aws_access_key_id=AWS_ACCESS_KEY_ID,
#                  aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

# Upload the file
try:
    response = s3.upload_file(file_to_upload, bucket_name, s3_key)
    print("File uploaded successfully:", response)
except Exception as e:
    print("Error uploading file:", e)
