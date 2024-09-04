from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config["SECRET_KEY"] = "29a4b8c7a50d7000d80788c4f06a0822"

posts_list = [
    {
        "author": "Durgesh Pandit",
        "title": "Blog Post 1",
        "content": "Content of Blog Post 1",
        "date_posted": "August 31, 2024"
    },
    {
        "author": "John Doe",
        "title": "Blog Post 2",
        "content": "Content of Blog Post 2",
        "date_posted": "September 1, 2024"
    }
]

@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html", posts = posts_list)

@app.route("/about")
def about():
    return render_template("about.html", title = "About")

@app.route("/register")
def register():
    return 

@app.route("/login")
def login():
    return 

if __name__ == "__main__":
    app.run(debug=True)