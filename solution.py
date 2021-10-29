from flask import request 
import socket, ssl
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    # return 'hello google app engine!'

@app.route('/products')
def products():
    return 'this is product!'

@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.json['file']  
        f.save(f.filename)  
        
        return render_template("success.html", name = f.filename)  


if (__name__=="__main__"):
    app.run(debug=True,  port=8000)
