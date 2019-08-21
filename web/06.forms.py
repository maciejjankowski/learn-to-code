from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/hello/')
@app.route('/hello/<name>')
def hello_again(name=None):
    return render_template('hello.html', signature=name)

@app.route('/vote', methods = ['POST', 'GET'])
def vote():
  result = ''
  if request.method == 'POST':
    result = request.form
    return render_template('thanks.html', result=result)
  else:
    return render_template('03.form.get_post.html', result=result)

if __name__ == '__main__':
  app.run()
