from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, login_required,  current_user
from flask_sqlalchemy import SQLAlchemy
#from config import DevConfig
from app.forms import LoginForm, PlanetParamsForm, CamQueryForm
from app.models import Planet, User
from app import app, db

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route("/blog")
def blog():
    user = {}
    posts = []
    return render_template("blog.html", title='Home', user=user, posts=posts)

@app.route('/images', methods=["GET"])
def images():
    return render_template('images.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))

    form = LoginForm()
    if request.method == "POST":
        user = User.query.filter_by(username = form.username.data).first()
        if (form.validate_on_submit() and
            user.password == form.password.data):
            login_user(user)
            flash('Successful Login, Welcome Alejandro!', 'success')
            next_page = request.args.get("next")

            return redirect(next_page) if next_page else redirect(url_for('images'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')

    return render_template('login.html', title='Sign In', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))

@app.route("/cam_query", methods = ["GET", "POST"])
def cam_query():
    form = CamQueryForm()
    if request.method == "POST":
        if form.validate_on_submit():
            pass
        else:
            flash('you messed something up. Make sure all fields are filled', 'danger')

    return render_template("cam_query.html", title="Security Video", form=form)