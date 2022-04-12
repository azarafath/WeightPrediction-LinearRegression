from flask import Flask, render_template, request, jsonify
import joblib

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def weight_prediction():
    if request.method == 'GET':
        return render_template("weight-prediction.html")
    elif request.method == 'POST':
        height = request.form['height']
        height = float(height) / 2.54
        weight = joblib.load('model-development/weight_height.pkl')
        weight = weight.predict([[height]])
        weight = str(weight / 2.205)[1:6]
        return render_template("weight-prediction.html", weight= weight, unit= "Kg")

if __name__ == '__main__':
    app.run(port=5000, debug=True)