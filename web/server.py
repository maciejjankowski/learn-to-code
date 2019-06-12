from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"



@app.route('/hello')
def hello_again():
    return render_template('hello.html')

@app.route('/kursy')
def pokaz_kursy():
    notowania = {"table":"A","currency":"funt szterling","code":"GBP",
    "rates":
    [{"no":"100/A/NBP/2019","effectiveDate":"2019-05-24","mid":4.8768},
    {"no":"101/A/NBP/2019","effectiveDate":"2019-05-27","mid":4.8759},
    {"no":"102/A/NBP/2019","effectiveDate":"2019-05-28","mid":4.8641},
    {"no":"103/A/NBP/2019","effectiveDate":"2019-05-29","mid":4.8744},{"no":"104/A/NBP/2019","effectiveDate":"2019-05-30","mid":4.8672},{"no":"105/A/NBP/2019","effectiveDate":"2019-05-31","mid":4.8572},{"no":"106/A/NBP/2019","effectiveDate":"2019-06-03","mid":4.8410},{"no":"107/A/NBP/2019","effectiveDate":"2019-06-04","mid":4.8144},{"no":"108/A/NBP/2019","effectiveDate":"2019-06-05","mid":4.8221},{"no":"109/A/NBP/2019","effectiveDate":"2019-06-06","mid":4.8274}]}
    return render_template('kursy.html', notowania=notowania)

app.run()
