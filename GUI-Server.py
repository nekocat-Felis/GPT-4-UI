#-*- coding: utf8 -*-
from flask import Flask, request
import GPT

app = Flask(__name__)
chat = GPT.Chat()

@app.route("/")
def HTML_Display():
    with open("entry.html", encoding="utf_8") as f:
        html = f.read()
    fake_options = '<option value="gpt-3.5-turbo">fake-01</option>\n<option value="gpt-3.5-turbo">fake-02</option>'
    options = ""
    for id, name in chat.model_list.items():
        options += f'<option value="{id}">{name}</option>\n'
    html = html.replace(fake_options, options)
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
    input()