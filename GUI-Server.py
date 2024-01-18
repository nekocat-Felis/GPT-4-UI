#-*- coding: utf8 -*-
from flask import Flask, request
import GPT

app = Flask(__name__)
chat = GPT.Chat("ここにAPIキーを入れる")

@app.route("/")
def HTML_Display():
    with open("entry.html", encoding="utf_8") as f:
        html = f.read()
    return html

@app.route("/access/", methods=["POST"])
def GPT_Access():
    req = request.json
    mod = req["model"]
    sys = req["system"]
    usr = req["user"]

    chat.system_input(sys)

    return chat.completion(model=mod, user_input=usr)

@app.route("/reset/")
def Log_Reset():
    chat.reset()
    return "reset"

if __name__ == "__main__":
    app.run(host="::1", port="53535", debug=True, threaded=True)