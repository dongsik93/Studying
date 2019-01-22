from flask import Flask, render_template, request, redirect
import csv
import datetime
app = Flask(__name__)



@app.route("/")
def index():
    f = open("todos.csv", "r", encoding="utf-8")
    todos = csv.reader(f)
    # todos = todos[::-1]
    
    return render_template("index.html", todos=todos)

@app.route("/new")
def new():
    return render_template("new.html")


# crud 중 c (create)
@app.route("/create")
def create():
    # print(request.args)
    title = request.args.get("title")
    Contents = request.args.get("Contents")
    now = datetime.datetime.now()
    
    f = open("todos.csv","a+", encoding="utf-8", newline="")
    csv_w = csv.writer(f)
    csv_w.writerow([title,Contents,now])
    f.close()
    
    return redirect("/")
    # return render_template("create.html",title = title, Contents=Contents)
        
    
    
@app.route("/post_new")
def post_new():
    return render_template("post_new.html")


@app.route("/post_create", methods=["post"])
def post_create():
    title = request.form.get("title")
    Contents = request.form.get("Contents")
    now = datetime.datetime.now()
    
    f = open("todos.csv", "a+",encoding="utf-8", newline="")
    post_csv_w = csv.writer(f)
    post_csv_w.writerow([title, Contents, now])
    f.close()
    
    return redirect("/")
    # return render_template("post_create.html", title=title, Contents=Contents)


if(__name__ == "__main__"): 
    app.run(debug=True,host="0.0.0.0",port=8080)
    
