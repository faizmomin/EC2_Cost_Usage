import boto3

client = boto3.client('ce')

response = client.get_cost_and_usage(
    TimePeriod={
        'Start': '2020-01-01',
        'End': '2020-10-05'
        },
        Ganularity='Monthly',
        Filters = [{
                'Resource' : 'EC2'  
            }],
        Metrics=['BlendedCost'],
        GroupBy=[
            {
                'Type': Tag,
                'Key': Project
            }
        ]   
    )



ec2 = bot3.resource('ec2')

instances = ec2.instances.filter(
    Filters = [ {
        'Name' : 'instance-state-name',
        'Values' : [ 'running' ]
    } ]
)

for intance in instances:
    print(instance.id, instance.type)
                     
