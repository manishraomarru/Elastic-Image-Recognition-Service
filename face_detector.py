import face_recognition
import pickle


class FaceDetector:
    def __init__(self):
        self.encoded_faces = self._open_encoding('encoding')

    @staticmethod
    def _open_encoding(filename):
        file = open(filename, "rb")
        data = pickle.load(file)
        file.close()
        return data

    def detect_faces(self, frame_paths):
        for frame_path in frame_paths:
            frame_image = face_recognition.load_image_file(frame_path)
            face_locations = face_recognition.face_locations(frame_image)
            if len(face_locations) > 0:
                face_encoding = face_recognition.face_encodings(
                    frame_image, face_locations)[0]
                match = face_recognition.compare_faces(
                    self.encoded_faces['encoding'], face_encoding)
                if True in match:
                    name = self.encoded_faces['name'][match.index(True)]
                    return name
        return None
