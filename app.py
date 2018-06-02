#!flask/bin/python
from flask import Flask, abort, request, jsonify, make_response, current_app
from myemail import myemail
from cors_decorator import crossdomain

app = Flask(__name__)


@app.route("/email", methods=['POST','GET','OPTIONS'])
@crossdomain(origin=['*'],headers=['Content-Type'],methods=["GET","POST","OPTIONS"])
def create_task():
    print(request.json['recipient'])
    print("here3")
    try:
        emailc = myemail()
        emailc.send_email(request.json['recipient'])
        myreturn = jsonify({'task': 'succeeded!'}), 201 
        return myreturn
    except:
	return jsonify({'task': 'fail'}),201


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True, threaded=True, port=3000)
