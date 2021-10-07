from flask import Flask
import logging

app = Flask(__name__)

@app.route("/")
def hello():
    return {"message": f"Hello!"} 

@app.route("/hello/<name>")
def hello_you(name):
    return {"message": f"hello {name}"}

if __name__ == "__main__":
    app.run(host='0.0.0.0')
