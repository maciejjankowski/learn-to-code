from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def voteing_page():
    return render_template('04.form.template.html')


@app.route('/vote', methods=['POST'])
def vote():
    result = request.form
    candidate = result.get("candidate")
    return render_template('05.form.passing_to_js.html',
                           passed_data=candidate)


app.run(debug=True)
