from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'abcdefg' # Required for session

@app.route('/')
def index():
    session.clear()
    return render_template("index.html")

@app.route("/users", methods=["POST"])
def create_user():
    session['name'] = request.form['name']
    session['gender'] = request.form['gender']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    # session['belts'] = request.form['belts']
    session['comments'] = request.form['comments']
    return redirect("/show")

@app.route("/show")
def show_user():
    print("Showing the User Info From the Form")
    print(request.form)
    return render_template("show.html")

@app.route('/destroy_session', methods=["POST"])
def destroy_session():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)