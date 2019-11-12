from flask import Flask,render_template
# from flask_sqlalchemy import  SQLAlchemy
app=Flask(__name__)

val=[11,22,33,44,556]
@app.route("/page/")
def wel():
    return render_template("sample.html",val=val)

if __name__== "__main__":
    app.run(debug=True)