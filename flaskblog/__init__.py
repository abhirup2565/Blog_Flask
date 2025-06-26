from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY']='b20a5a92c16612725adbb34de5abb341'
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///site.db"
db=SQLAlchemy(app)

from flaskblog import routes