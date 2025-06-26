from flask import Flask,render_template,url_for,flash,redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY']='b20a5a92c16612725adbb34de5abb341'



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
    app.run(debug=True)