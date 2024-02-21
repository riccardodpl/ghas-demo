from flask import Flask
import requests

vulnerable_app = Flask(__name__)

@vulnerable_app.route('/greeting')
def greeting():
    return 'Hello, World!'

@vulnerable_app.route('/vulnerable-route')
def vulnerable_route():
    # url = request.args.get('url', '')
    # if url:
    #     return requests.get(url).text

    return "No URL parameter provided."

@vulnerable_app.route('/')
def home():
    return 'vulnerable home route'
    # return '''<h1>SSRF</h1>
    #             <br>
    #             Usage:
    #                 <br><code>http://127.0.0.1:80/follow?url=https://api.github.com/events</code><br>
    #             Running:
    #             <br><code>
    #                 sudo apt install -y python3-pip
    #                 sudo pip3 install flask requests;
    #                 FLASK_APP=ssrf.py flask run --host=0.0.0.0 --port=80
    #             </code></br>
    # '''


if __name__ == '__main__':
    vulnerable_app.run(debug=True)