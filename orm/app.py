from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

## sqlalchemy 설정
# 현재 폴더에 sqlite라는 프로그램을 사용해서 database를 만들겠다는 의미
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///flask_db.sqlite3"
# 자동으로 파일을 detect하는걸 False로 
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

## sqlalchemy 초기화
# 플라스크 서버를 
db = SQLAlchemy(app)

## 서버와 db를 이주?
migrate = Migrate(app, db)

## 파이썬 코드로 테이블 작성
# db가 가지고 있는 Model을 상속
class User(db.Model):
    __tablename__ = "users"
    # column에 대한 데이터 타입 명시 (byte단위)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable = False) 
    email = db.Column(db.String(50))


@app.route("/")
def hello():
    # 쿼리 보내기
    users = User.query.all()
    return render_template("index.html", users = users)
    
 
@app.route("/new")
def new():
    return render_template("new.html")

@app.route("/create")
def create():
    name = request.args.get("name")
    email = request.args.get("email")
    
    new_user = User(name = name, email = email)
    db.session.add(new_user)
    db.session.commit()
    
    return redirect('/')
    
    
@app.route("/post_new")
def post_new():
    return render_template("post_new.html")
    
@app.route("/post_create", methods=["post"])
def post_create():
    name = request.form.get("name")
    email = request.form.get("email")
    
    new_user = User(name = name, email = email)
    db.session.add(new_user)
    db.session.commit()
    
    return redirect('/')
    
if(__name__ == "__main__"): # 모듈로 불렀는지, 파이썬 파일(main으로)로 실행했는지
    app.run(debug=True,host="0.0.0.0",port=8080) # app은 Flask객체 / debug모드로 호스트, 포트를 설정
    
    