

from flask import Flask,render_template,request
from chatbot import chatbot



app = Flask(__name__)

app.static_folder = 'static'
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def responseBot(): 
    userText  = request.args.get('message')
    return str(chatbot.get_response(userText))


if __name__ == "__main__":
    app.run() 