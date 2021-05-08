from flask import Flask, render_template, request
from helper import getPlots
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import math
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
# the assumptions
@app.route('/assumptions')
def userguide():
    return render_template("assumptions.html")
# the interface of the first calculator – 
# defines the "get" request behavior to be loading the page from a template and the "post" request behavior to load a data page
# will have a way to talk to helper.py to get the plotting functions and display the plots on the page
@app.route('/calculator', methods = ['GET', 'POST'])
def calc():
    if request.method == 'GET':
        return render_template("calc.html")
    else:
        # start and end year data
        startYear = int(request.form.get("start"))
        endYear = int(request.form.get("end"))
        if (startYear >= endYear):
          return render_template("error.html", error = " you need to make the start year come before the end year.")  
        
        
        # initial conditions data in format used by helper.py
        initial = np.array([float(request.form.get("cinit")), float(request.form.get("nginit")), float(request.form.get("soinit")), float(request.form.get("winit")), float(request.form.get("ninit")), float(request.form.get("winginit"))])
        
        # throws an error if the percents for the initial value aren't close enough to 100%
        if not math.isclose(sum(initial), 100.0, rel_tol=1e-3):
            return render_template("error.html", error = " your initial percentages do not add up to 100%.")
        
        # first derivative data
        firsderv = np.array([float(request.form.get("cd")), float(request.form.get("ngd")), float(request.form.get("sod")), float(request.form.get("wd")), float(request.form.get("nd")), float(request.form.get("wid"))])
        
        # second derivative data
        secderv = np.array([float(request.form.get("cd2")), float(request.form.get("ngd2")), float(request.form.get("sod2")), float(request.form.get("wd2")), float(request.form.get("nd2")), float(request.form.get("wid2"))])
        
        # effectiveness %
        effec = float(request.form.get("eff"))
        
        imgs = getPlots(startYear, endYear, initial, firsderv, secderv, effec)
        
        
        return render_template("data.html", energy = imgs[0], emm = imgs[1], prod = imgs[2], rel = imgs[3], construct = imgs[4], consum = imgs[5], net=imgs[6])
    
# runs our app using Flask
if __name__ == "__main__":
    app.run(debug = True)
