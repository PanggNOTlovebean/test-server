from flask import Flask,render_template,jsonify,request
import socket

app = Flask(__name__)

@app.route("/")
def index():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        return render_template('index.html', hostname=host_name, ip=host_ip)
    except:
        return render_template('error.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    print(username)
    print(password)
    if(username=='admin' and password=='123456'):
        return jsonify({'message':'login success'}), 200
    else:
        return jsonify({'message':'login fail'}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
