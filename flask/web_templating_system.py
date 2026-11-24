from flask import Flask,render_template

app=Flask(__name__,template_folder="templates")

@app.route("/")
def home():
    return "<h1> this is home page</h1>"

@app.route("/welcome/<name>")
def welcome(name):
    return render_template("welcome.html", username=name)

@app.route("/age/<int:num>")
def age(num):
    name="shiv"
    return render_template("welcome2.html",n=num,s=name)

@app.route("/list")
def list():
    stu_list=[11,1.34,"shiv",True]
    new_dict={"name":"shiv","age":23,"course":"python"}
    return render_template("list.html",list= stu_list, dict=new_dict)

@app.route("/login/<name'>")
def login(name):
    if name=="hr":
     return  "hr dashboard"
    elif name=="student":
        return "student dashboard"
    else:
        return " page not found "


if __name__ =="__main__":
    app.run(debug=True)