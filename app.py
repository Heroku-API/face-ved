from face_copy_flask import *
from flask import Flask,Response
app = Flask(__name__)

@app.route("/")
def run_stream():
    source=r'input_1.mp4'




    return Response(main(source), mimetype='multipart/x-mixed-replace; boundary=frame')





if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8087)
