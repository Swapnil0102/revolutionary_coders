from flask import Flask, jsonify, request, redirect, url_for, render_template, flash
from flask_restful import Resource,Api

#from werkzeug import secure_filename
import urllib.request,json

app = Flask(__name__)
api = Api(app)

@app.before_request
def before():
    print("Request Executed")

@app.route('/',methods=['GET','POST'])
def upload()    
    print("html works")
    return render_template('upload.html')
    #data=request.json
#def upload():
 #   return render_template(url_for('templates',filename'upload.html'))

@app.route('/success',methods=['GET','POST'])
def upload_file():
    if request.method=='POST':
    f = request.files['file']
    f.save(secure_filename(f.filename))
    return "file uploaded successfully"

if __name__ == '__main__':
    app.run(debug=True,ssl_context=True)

#defining all functions and work that will take place here

#Function to take input
#def take_input():
    #see how to make web request
    #input will be requested as a single line json format input
    #[{"FirstName":"John","LastName":"Doe","IDNumber":"123","Message":"None"},{"FirstName":"George","LastName":"Washington","IDNumber":"001","Message":"Something"}]
    #print("give input")
    #output format will also be a single line with address:"Whatever the address is"
    #
 #   return "12"

#function to run code line by line

#function to check language, if not english, use translation

#Function for translation

#Function to deal with duplicates
#def checkDup():
    #if line needs to be removed, put NA, replace all null values with NA also

 #   return

#function to convert output into a json file

#function to return output

    #execute all desired functions and throw output
