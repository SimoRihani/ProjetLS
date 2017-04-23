from flask import Flask
from flask import render_template
from flask import request
from flask import json
import sys
#import helpers
from foo import content
from foo import method
from foo import param
from algo import algorithme_2
from algo import algorithme_1

app = Flask(__name__)

# @app.route('/')
# def index():
#     return 'Hello world'

@app.route("/")
def hello():
    return "Welcome to Python Flask!"

@app.route('/tst')
def cakes():
    return 'Test!'

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/signUp')
def signUp():
    return render_template('signUp.html')

@app.route('/signUpUser', methods=['GET', 'POST'])
def signUpUser():
    user =  request.form['username'];
    password = request.form['password'];
    return json.dumps({'status':'OK','user':user,'pass':password});

@app.route('/indexAct', methods=['GET', 'POST'])
def indexAct():
    #  return request.form['header'];
    #print(request.get_json()['Content']);
    #print('Method :');
    #print(method(request.get_json()));
    #print('Content :');
    #print(content(request.get_json()));
    # print('Param :');
    # print(param(request.get_json()));
    print('Rendu : ');
    # print(algorithme_2(request.get_json()));
    print(algorithme_1(request.get_json()));
    return json.dumps(request.get_json());
    #return(json.dumps(bar2().get_json())
    #return request.form['output'];


    # user =  request.form['username'];
    # password = request.form['password'];
    #return json.dumps({'status':'OK','user':"hehe",'pass':"ho"});

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0')

if __name__ == "__main__":
    app.run(debug=True)
