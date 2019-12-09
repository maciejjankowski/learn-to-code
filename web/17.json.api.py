from flask import Flask, render_template, request, make_response
import json
import os

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.after_request
def apply_kr_hello(response):
    """Adds some headers to all responses."""

    # Made by Kenneth Reitz.
    if 'MADE_BY' in os.environ:
        response.headers["X-Was-Here"] = os.environ.get('MADE_BY')

    # Powered by Flask.
    response.headers["X-Powered-By"] = os.environ.get('POWERED_BY')
    response.headers.add(
        "Access-Control-Allow-Origin", "https://oferia.pl")
    response.headers.add("Access-Control-Allow-Credentials", "true")
    response.headers.add("Access-Control-Allow-Methods",
                         "GET,HEAD,OPTIONS,POST,PUT")
    response.headers.add("Access-Control-Allow-Headers",
                         "Access-Control-Allow-Headers, Origin,Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers")

    return response


@app.route('/save/img', methods=['OPTIONS'])
@app.route('/save', methods=['OPTIONS'])
def votex():
    response = make_response()
    return response


@app.route('/post/img', methods=['POST', 'GET'])
def votey():
    # print(json.loads(request.args['o']))
    return('ok')


@app.route('/save', methods=['POST', 'GET'])
def vote():
    result = ''
    if request.method == 'POST':
        result = request.data
        print(json.loads(result))
        return('ok')
        # return render_template('thanks.html', result=result)
    elif request.method == 'OPTIONS':
        return("ok")
    else:
        return('no!')


if __name__ == '__main__':
    # , ssl_context=('./cert.pem', './key.pem'))
    app.run(port=9000, host="0.0.0.0")
