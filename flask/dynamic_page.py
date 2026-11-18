from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def home():
    return "<h1> this is home page</h1>"

@app.route("/welcome/<name>")
def welcome(name):
    return render_template("welcome.html", username=name)


if __name__ =="__main__":
    app.run(debug=True)