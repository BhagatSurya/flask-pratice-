from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route('/')
def hello():
    return "heloo my life "

@app.route("/pass/<int:score>")
def  sucess(score):
    return " the person has pass" + str(score)


@app.route("/ fail/<int:score>")
def fail(score):
    return " the person has fail" + str(score)


@app.route("/result/<int:mark>")
def result(mark):
    result = ""
    if mark < 50:
        result = "fail"
    else:
        result = "pass"
    return redirect(url_for(result,score=mark))

if __name__ == "__main__":
    app.run(debug=True)