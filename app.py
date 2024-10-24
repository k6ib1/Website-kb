import numpy as np
from flask import Flask, render_template

app = Flask(__name__)

# Route for the home page
@app.route("/")
def home():
    return render_template("index.html")  # Renders the main page

# Route for the graphs page
@app.route("/graphs")
def graphs():
    return render_template("graphs.html")  # Renders the graphs page

if __name__ == "__main__":
    app.run(debug=True)
