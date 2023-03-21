from flask import Flask
from flask import render_template
app=Flask(__name__)

def helloworld():
    return render_template("helloworld.html")

if __name__=="__main__":
    app.debug=True
    app.run()