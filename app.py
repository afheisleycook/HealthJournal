from flask import(Flask, redirect,url_for,render_template,request, request, Response)
import socket
app = Flask(__name__,static_folder="static")
app.config["port"] = 80
@app.route('/',methods=['GET','POST'])
def home():
    return redirect("/journal")
@app.route('/journal')
def index():
    
    return render_template("index.html")

def main():
    app()