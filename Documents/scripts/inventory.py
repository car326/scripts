import boto3

region_list = [
    "us-east-1",
    "us-east-2",
    "us-west-1",
    "us-west-2",
    "ap-south-1",
    "ap-northeast-2",
    "ap-southeast-1",
    "ap-northeast-1",
    "ca-central-1",
    "eu-central-1",
    "eu-west-1",
    "eu-west-2",
    "eu-west-3",
    "sa-east-1"
    ]

    gEC2 = 0

    for item in region_list:

       ec2c = boto3.client("ec2", region_name=item)
       ec2r = boto3.resource("ec2", region_name=item)

       EC2 = 0

         response