from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username' : 'Pedro'}
    posts = [
        {
            "author":{"username" : "João"},
         "body" : "Grande dia em João Pessoa!"
         },
         {
             "author":{"username":"Maria"},
             "body":"O filme dos Vingadores foi massa"
         }
    ]
    return render_template("index.html", title="Home", user=user, posts=posts)
