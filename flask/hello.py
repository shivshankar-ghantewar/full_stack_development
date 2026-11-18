from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
    return "this is home page"

@app.route("/about")
def about():
    return "its me shiv"

@app.route("/contact")
def contact():
    return "thanks for contacting shiv"

@app.route("/skills")
def skills():
    return "full stack python  developer"

if __name__=="__main__":
    app.run(debug=True)