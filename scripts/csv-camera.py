# Import necessary modules
from flask import Flask, render_template, Response, request, jsonify, redirect, url_for, send_file
import cv2

# Create a Flask app instance
app = Flask(__name__, static_url_path='/static')




def gen_frames():  # generate frame by frame from camera
    camera = cv2.VideoCapture('http://127.0.0.1:8082')
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('tmp/output.avi', fourcc, 20.0, (640,  480))
    while True:
        # Capture frame-by-frame
        #success, frame = camera.read()  # read the camera frame
        ret, frame = camera.read()
        if not ret:
            break
        else:
            out.write(frame)
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

# Route to stream video frames
@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route("/video")
def video():
    return send_file("./tmp/alprVideo.mp4")
# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')