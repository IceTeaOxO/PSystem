from flask import Flask, render_template
import DB.sqlite as sql


app = Flask(__name__)
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/home")
def home():
    return render_template('homepage.html')

@app.route("/tem")
def tem():
    return render_template('tem.html')

#simple backend
@app.route("/backend")
def backend():
    appInfo = {
        'id':1,
        'version':"1.1",
        'name':"Python",
    }
    return render_template('backend.html',appInfo=appInfo,text="this is text")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)