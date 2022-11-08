from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def initializeBoard():
    return render_template('index.html', width=8, height=8)


@app.route('/4')
def eightByFour():
    return render_template('index.html', width=8, height=4)


@app.route('/<x>/<y>')
def xByY(x, y):
    return render_template('index.html', width=int(x), height=int(y))


@app.route('/<x>/<y>/<color1>/<color2>')
def hellaColors(x, y, color1, color2):
    return render_template('index.html', width=int(x), height=int(y), color1=color1, color2=color2)

if __name__ == "__main__":
    app.run(debug=True)
