# Connecting to AWS DynamoDB and EC2 Instance (MySQL) using Python:
#AWS DynamoDB (NoSQL):

import boto3

# Initialize a DynamoDB client
dynamodb = boto3.client("dynamodb")

# Use DynamoDB operations
response = dynamodb.list_tables()
print("DynamoDB Tables:", response["TableNames"])


# AWS EC2 Instance (MySQL):

import mysql.connector

# Connect to the MySQL server on your EC2 instance
connection = mysql.connector.connect(
    host="ec2_public_ip_or_hostname",
    user="your_username",
    password="your_password",
    database="your_database_name"
)

# Perform database operations as needed

# Close the cursor and connection
cursor.close()
connection.close()
