from flask import Flask,render_template,url_for,flash,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime,timezone

from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY']='b20a5a92c16612725adbb34de5abb341'
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///site.db"

db=SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20),unique = True ,nullable=False)
    email = db.Column(db.String(120),unique=True ,nullable=False)
    image_file = db.Column(db.String(20) ,nullable=False, default='default.jpg')
    password = db.Column(db.String(60),nullable =False)
    posts = db.relationship('Post', backref='author',lazy=True)

    def __repr__(self):
        return f"user('{self.username}','{self.email}','{self.image_file}')"
    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20),nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone.utc))
    content = db.Column(db.Text,nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)

    def __repr__(self):
        return f"user('{self.title}','{self.date_posted}')"


posts = [
    {
        'author':'Abhirup Singh',
        'title':'First blog post',
        'date_posted': 'June 23',
        'content':'content 1',
    },
    {
        'author':'Abhipreet Singh',
        'title':'First blog post',
        'date_posted': 'october 23',
        'content':'content 2',
    },
    ]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html",posts=posts)


@app.route("/about")
def about():
    return render_template("about.html",title="About")


@app.route("/register", methods=["POST","GET"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"account created for {form.username.data}!","success")
        return redirect(url_for('register'))
    return render_template('register.html',title='Register',form=form)


@app.route("/login",methods=["POST","GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data=="admin@blog.com" and form.password.data=="password":
            flash("you have been logged in ","success")
            return redirect(url_for('home'))
        else:
            flash("Login failed check username or password","danger")
    return render_template('login.html',title='Login',form=form)






if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)