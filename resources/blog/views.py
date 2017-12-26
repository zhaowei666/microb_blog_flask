from flask import render_template, g
from models import User


def homepage():
    users = g.session.query(User).all()
    return render_template('index.html',
                           title='Home',
                           users=users)