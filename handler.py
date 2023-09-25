import boto3
from frame_extractor import FrameExtractor
from face_detector import FaceDetector
from student_info import StudentInfo
from s3_client import S3Client

input_bucket = "cloud-project-2-input"
output_bucket = "cloud-project-2-output"

s3 = boto3.client('s3')
dynamodb = boto3.client('dynamodb')
temp_path = "/tmp/"


def face_recognition_handler(event, context):
    input_bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    frame_extractor = FrameExtractor(s3, temp_path)
    frame_paths = frame_extractor.extract_frames(input_bucket, key)

    face_detector = FaceDetector()
    name = face_detector.detect_faces(frame_paths)

    student_info = StudentInfo(dynamodb).get_student_info(name)

    s3_client = S3Client(s3)
    output_key = key.split('.')[0] + '.csv'
    s3_client.write_to_s3(output_bucket, output_key, student_info)
    print(student_info)


# face_recognition_handler({
#     "Records": [
#         {
#             "s3": {
#                 "bucket": {
#                     "name": "546proj2-rasengan"
#                 },
#                 "object": {
#                     "key": "test_98.mp4"
#                 }
#             }
#         }
#     ]
# }, "")
