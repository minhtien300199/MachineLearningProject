from flask import Flask, request, jsonify, make_response
app = Flask(__name__)
@app.route("/")
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run()