import cv2

# defining face detector
# face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
ds_factor = 0.6


class VideoCamera(object):
    def __init__(self):
        # capturing video
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        # releasing camera
        self.video.release()

    async def get_frame(self):
        # extracting frames
        ret, frame = self.video.read()
        frame = cv2.resize(
            frame, None, fx=ds_factor, fy=ds_factor, interpolation=cv2.INTER_AREA
        )
        # gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # encode OpenCV raw frame to jpg and displaying it
        ret, jpeg = cv2.imencode(".jpg", frame)
        return jpeg.tobytes()
