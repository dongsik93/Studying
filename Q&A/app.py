from flask import Flask, render_template, redirect, request
import csv

app = Flask(__name__)

@app.route("/")
def hello():
    f = open("board.csv", "r", encoding="utf-8")
    boards = csv.reader(f)
    return render_template("index.html",boards=boards)



@app.route("/write")
def write():
    return render_template("write.html")
    
    
@app.route("/post_create",  methods=["post"])
def post_create():
    title = request.form.get("title")
    contents = request.form.get("contents")
    
    f = open("board.csv","a+",encoding="utf-8",newline="")
    csv_write = csv.writer(f)
    csv_write.writerow([title,contents])
    f.close()    
    
    return redirect("/")
    


    
if(__name__ == "__main__"): 
    app.run(debug=True,host="0.0.0.0",port=8080)
    