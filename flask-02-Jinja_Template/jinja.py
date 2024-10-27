from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def head():
     return render_template('index.html', number1=35, number2=36)

@app.route('/mult')
def number():
     x=35
     y=36
     return render_template('body.html', value1=x, value2=y, sum=x*y)

if __name__== "__main__":
     # app.run(debug=True)
     app.run(host= '0.0.0.0', port=80)