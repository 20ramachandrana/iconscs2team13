from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html", message = "Texas Grid Projection Calculator!")
@app.route('/userguide')
def userguide():
    return render_template("userguide.html")
@app.route('/calculator', methods = ['GET', 'POST'])
def calc():
    if request.method == 'GET':
        return render_template("calc.html")
    else:
        return render_template("data.html")
@app.route('/calculatorver2', methods = ['GET', 'POST'])
def calc():
    if request.method == 'GET':
        return render_template("calcver2.html")
    else:
        return render_template("data.html")
if __name__ == "__main__":
    app.run(debug=True)
