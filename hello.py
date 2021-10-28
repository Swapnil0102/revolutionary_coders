from flask import Flask

app = Flask(__name__)

file=[]

@app.route('/get_json',methods=['POST'])
def get_json():
    if request.method=='POST':
        file.append(request.get_json())
        return 'hello',204

if __name__ == '__main__':
    app.run(debug=True)
