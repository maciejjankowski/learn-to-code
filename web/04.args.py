from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/hello/')
@app.route('/hello/<name>')
def hello_again(name=None):
    return render_template('hello.html', signature=name)

app.run()
