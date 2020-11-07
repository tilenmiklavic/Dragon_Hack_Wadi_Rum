from flask import Flask, render_template, request

app = Flask(__name__)

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')
  
@app.route('/', methods=['POST', 'GET'])
def form():
    data = request.form.get("age")
    return render_template('index.html', name=data)