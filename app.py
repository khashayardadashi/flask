from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DataBase.db'
db.init_app(app)

class USERS(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.Text, unique=True, nullable=False)
	date = db.Column(db.DateTime, default=datetime.now)

with app.app_context():
   db.create_all()

@app.route('/home')
def show():
    return render_template('show.html')
