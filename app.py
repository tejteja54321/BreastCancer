from flask import Flask, render_template, request, redirect, url_for, session
import pickle


app = Flask(__name__)
app.secret_key = "abcdefgh123456789"  


users = {}


def check_password(stored_password, provided_password):
    return stored_password == provided_password

@app.route("/")
def login():
    if 'email' in session:
        return redirect(url_for('home'))
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        # Save user data (In real apps, use a database)
        if email in users:
            return redirect(url_for('register'))
        users[email] = {'username': username, 'password': password}
        return redirect(url_for('login'))
    return render_template("register.html")

@app.route("/login", methods=["POST"])
def login_post():
    email = request.form["email"]
    password = request.form["password"]
    if email in users and check_password(users[email]['password'], password):
        session['email'] = email
        return redirect(url_for('home'))
    return redirect(url_for('login'))

@app.route("/logout")
def logout():
    session.pop('email', None)
    return redirect(url_for('login'))

@app.route("/home")
def home():
    if 'email' not in session:
        return redirect(url_for('login'))
    return render_template("home.html")

@app.route("/input", methods=["POST", "GET"])
def input():
    if 'email' not in session:
        return redirect(url_for('login'))
    if request.method == "POST":
        radius = float(request.form["radius"])
        texture_mean = float(request.form["texture_mean"])
        perimeter_mean = float(request.form["perimeter_mean"])
        area_mean = float(request.form["area_mean"])
        smoothness_mean = float(request.form["smoothness_mean"])
        concavity_mean = float(request.form["concavity_mean"])
        concave_points_mean = float(request.form["concave_points_mean"])
        symmetry_mean = float(request.form["symmetry_mean"])
        fractal_dimension_mean = float(request.form["fractal_dimension_mean"])
        data = [[radius, texture_mean, perimeter_mean, area_mean, smoothness_mean, concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean]]
        with open("SVM_model1.pkl", 'rb') as file:
            model = pickle.load(file)
            result = model.predict(data)
        return render_template("result.html", data=int(result))
    return render_template("input.html")

if __name__ == '__main__':
    app.run(debug=True)
