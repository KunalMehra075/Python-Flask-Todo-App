from flask import Flask,redirect,request,render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"

db = SQLAlchemy(app)



class Todo(db.Model):
    sno = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(200),nullable=False)
    desc = db.Column(db.String(500),nullable=False)
    date_created = db.Column(db.DateTime,default=datetime.now())
    
    def __repr__(self)-> str:
        return f"{self.sno} -  {self.title}"    

        

@app.route('/',methods=['GET',"POST"])
def hello_world(): 
    if request.method == "POST" and request.form["title"]:
        title = request.form["title"]
        desc= request.form["desc"]
        todo = Todo(title=title,desc=desc)
        db.session.add(todo)
        db.session.commit()
    
    allTodo = Todo.query.all()
    return render_template('index.html',allTodo=allTodo)


@app.route('/delete/<int:sno>')
def delete_todo(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")

@app.route('/update/<int:sno>',methods=['GET','POST'])
def update_todo(sno):
    if request.method == 'POST':
        title = request.form["title"]
        desc= request.form["desc"]
        todo = Todo.query.filter_by(sno=sno).first()
        todo.title = title
        todo.desc = desc
        db.session.add(todo)
        db.session.commit()
        return redirect("/")
    todo = Todo.query.filter_by(sno=sno).first()
    return  render_template('update.html',todo=todo)

if __name__ == "__main__":
    app.run(debug=True,port=8000)
    