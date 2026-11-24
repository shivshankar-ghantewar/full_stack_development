from flask import Flask,redirect,url_for

app=Flask(__name__)

@app.route("/")
def home():
    return "this is home page"

@app.route("/about")
def about():
    # redirect=> use to redirect url to another url
    # url_for()=> generates a URL using the name of a Flask view function (endpoint).
    return redirect(url_for("welcome"))

@app.route("/welcome")
def welcome():
    return "this is welcome page"


if __name__=="__main__":
    app.run(debug=True)