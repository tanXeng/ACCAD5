from flask import Flask

app = Flask(__name__)

@app.route("/")
def helloworld():
    return "Hello World. Please workkkkkkk"

if __name__ == "__main__":
    app.run(port=8000, host='0.0.0.0')
