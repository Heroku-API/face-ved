from face_copy_flask import *
from flask import Flask,Response
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)


@app.route("/")
def run_stream():
    source=r'C:\Users\Keerthika\Desktop\face_recognition\input_1.mp4'




    return Response(main(source), mimetype='multipart/x-mixed-replace; boundary=frame')





if __name__ == "__main__":
    app.run()
