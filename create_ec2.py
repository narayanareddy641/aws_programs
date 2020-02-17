import boto3
ec2 = boto3.resource('ec2')

# create a new EC2 instance
instances = ec2.create_instances(
     ImageId='ami-09a4a9ce71ff3f20b',
     MinCount=1,
     MaxCount=1,
     InstanceType='t2.micro',
     KeyName='reddy-key'
 )
print(instances)
