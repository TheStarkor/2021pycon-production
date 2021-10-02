import os
import flask
import boto3
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)

def s3_connection():
    s3 = boto3.client('s3',
        aws_access_key_id = os.environ.get("ACCESS_KEY"),
        aws_secret_access_key = os.environ.get("SECRET_KEY"))
    return s3

@app.route("/", methods=["GET"])
def hello():
    return "hello"

@app.route("/", methods=["POST"])
def upload():
    # try:
    if flask.request.files.get("img"):
        flask.request.files["img"].save('pycon2021.jpg')
        s3 = s3_connection()
        s3.upload_file('pycon2021.jpg', os.environ.get("BUCKET_NAME"), 'pycon2021.jpg', ExtraArgs={'ACL':'public-read'})
    return flask.jsonify({
        'uri': f'https://{os.environ.get("BUCKET_NAME")}.s3.ap-northeast-2.amazonaws.com/pycon2021.jpg'
    })
    # except:
    #     return flask.abort(404)
            
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)