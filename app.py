from flask import Flask,render_template,request
import os
import diet

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/sub',methods=['POST'])
def sub():
    if request.method == 'POST':
        name = request.form["person"]
        weight = request.form["weight"]
        height = request.form["height"]
        age = request.form["age"]
        print(weight, height, age)
        exercise = diet.model(weight,height,age)
    return render_template('sub.html',n = name,w = weight, h = height,a = age,exercise=exercise)

if __name__ == '__main__':
    app.run()

