from flask import Flask, render_template, jsonify, session, g
import requests
app = Flask(__name__)

@app.route('/')
def base():
    common = []
    obj = ['http://localhost:5000','http://localhost:5001','http://localhost:5002','https://www.google.com/']
    for j,i in enumerate(obj):
        total =  {}
        try:
            data = requests.get(i)
            data = True
        except requests.ConnectionError:
            data = False
        total['id']=j+1
        
        total['name']=i.replace('localhost','mani')
        total['status']=data
        common.append(total)
    return render_template('index.html',**locals())




if __name__=='__main__':
    app.run(host="localhost", port=8000, threaded=True) 

