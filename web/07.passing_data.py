from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def vote():
    if request.method == 'POST':
        result = request.form
        candidate = result.get("candidate")
        return render_template('05.form.passing_to_js.html', 
                                passed_data=candidate)
    else: 
        return render_template('04.form.template.html')

app.run(debug=True)
