import os


class FrameExtractor:
    def __init__(self, s3_client, temp_path):
        self.s3_client = s3_client
        self.temp_path = temp_path

    def extract_frames(self, bucket_name, object_key):
        file_name = object_key.split('/')[-1]
        video_file_path = f'{self.temp_path}{file_name}'
        self.s3_client.download_file(bucket_name, object_key, video_file_path)

        frame_paths = []
        path = self.temp_path
        os.system("ffmpeg -i " + str(video_file_path) +
                  " -r 1 " + str(path) + "image-%3d.jpeg")
        for file in os.listdir(path):
            if file.endswith(".jpeg"):
                frame_paths.append(os.path.join(path, file))

        return frame_paths
