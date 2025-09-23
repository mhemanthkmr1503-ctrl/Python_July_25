from flask import Flask, request
from rich import print
app = Flask(__name__)

@app.route("/post_message", methods=["PUT"])
def post_message():
    data = {
        "status" : 200,
        "message" : "Its Working"
    }
    print(request.get_json())
    return data

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)