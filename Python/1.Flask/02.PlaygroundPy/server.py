from flask import Flask, render_template
app = Flask(__name__)


@app.route('/play')
def initialize():
    return render_template("index.html", phrase="blue", times=3)

@app.route('/play/<number>')
def make_boxes(number):
    if (number.isnumeric()):
        number = int(number)
        return render_template("index.html", phrase="blue", times=number)


@app.route('/play/<number>/<color>')
def make_more_boxes(number, color):
    if (number.isnumeric()):
        number = int(number)
        return render_template("index.html", phrase=color, times=number)

if __name__ == "__main__":
    app.run(debug=True)
