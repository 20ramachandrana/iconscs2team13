from flask import Flask, render_template, request

# the app we use to manage the routes and run the app
app = Flask(__name__)


# main homepage of the website
@app.route('/')
def home():
    return render_template("home.html", message = "Texas Grid Projection Calculator!")

# the user guide
@app.route('/userguide')
def userguide():
    return render_template("userguide.html")

# the interface of the first calculator – 
# defines the "get" request behavior to be loading the page from a template and the "post" request behavior to load a data page
# will have a way to talk to helper.py to get the plotting functions and display the plots on the page
@app.route('/calculator', methods = ['GET', 'POST'])
def calc():
    if request.method == 'GET':
        return render_template("calc.html")
    else:
        return render_template("data.html", data = "")
    

# the interface of the second calculator (autogenerating the number of fields needed) – 
# defines the "get" request behavior to be loading the page from a template and the "post" request behavior to load a data page
# will have a way to talk to helper.py to get the plotting functions and display the plots on the page
@app.route('/calculatorver2', methods = ['GET', 'POST'])
def calcver2():
    if request.method == 'GET':
        return render_template("calcver2.html")
    else:
        return render_template("data2.html", data = "")
    
# runs our app using Flask
if __name__ == "__main__":
    app.run()
