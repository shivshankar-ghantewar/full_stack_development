from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
    return "<h1> this is homepage </h1>"

@app.route("/name")
def name():
    name="shiv"
    return "my name is %s" %name

@app.route("/age/<int:num>")
def age(num):
    return "my age is:%d" %num


if __name__=="__main__":
    app.run(debug=True)