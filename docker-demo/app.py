from flask import Flask
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
	return "Hello World" 

app.run(host="127.0.0.1", port=5000)