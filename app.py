from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html", message = "Texas Grid Projection Calculator!")
@app.route('/userguide')
def userguide():
    return render_template("userguide.html")
@app.route('/calculator', methods = ['GET', 'POST'])
def calc():
    if request.method == 'POST':
        return render_template("calc.html")
    else:
        return render_template("data.html")

if __name__ == "__main__":
    app.run()
