from flask import Flask, request , jsonify
from flask_cors import CORS
from time import sleep
app = Flask(__name__)

CORS(app)
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/postdata',methods=['POST'])
def postdata():
    
    data = request.get_json()
    submitted={

            "Name":"Sucess"
        }
    print(data)
    sleep(5)
    return jsonify(submitted)
    # return "<p>I am here</p>"


if __name__ =="__main__":
    app.run(debug=True,host="0.0.0.0")