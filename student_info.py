import boto3


class StudentInfo:
    def __init__(self, dynamodb):
        self.dynamodb = dynamodb

    def get_student_info(self, name):
        response = self.dynamodb.get_item(
            TableName='cloud-project-1-faces-table',
            Key={
                'name': {'S': name}
            }
        )
        item = response.get('Item')
        if item is not None:
            return f"{name}," + item['major']['S'] + "," + item['year']['S']
