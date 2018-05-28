#!flask/bin/python
from flask import Flask, request, jsonify, make_response
from flask_httpauth import HTTPBasicAuth
from myemail import myemail


auth = HTTPBasicAuth()

app = Flask(__name__)


@auth.get_password
def get_password(username):
    if username == 'miguel':
        return 'python'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)


@app.route('/email', methods=['POST'])
@auth.login_required
def create_task():
    if not request.json or not 'recipient' in request.json:
        abort(400)
   
    emailc = myemail()
    emailc.send_email(request.json['recipient'])
    
    return jsonify({'task': 'succeeded!'}), 201

if __name__ == '__main__':
    app.run(debug=True, threaded=True, port=3000)
