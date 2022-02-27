from quart import Quart, render_template, Response
from camera import VideoCamera

app = Quart(__name__)


@app.route("/")
async def index():
    # rendering webpage
    return await render_template("index.html")


async def gen(camera: VideoCamera):
    while True:
        # get camera frame
        frame = await camera.get_frame()
        yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n\r\n")


@app.route("/video_feed")
async def video_feed():
    return Response(
        gen(VideoCamera()), mimetype="multipart/x-mixed-replace; boundary=frame"
    )


if __name__ == "__main__":
    # defining server ip address and port
    app.run(host="0.0.0.0", port="8009", debug=True)
