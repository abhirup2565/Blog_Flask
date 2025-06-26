from flask import Flask,render_template,url_for

app = Flask(__name__)



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

if __name__=="__main__":
    app.run(debug=True)