from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "If you're reading this, CuteBot is active.<br/> <br/>If you'd like to add CuteBot to your server, you can use this <a href=\"https://discord.com/api/oauth2/authorize?client_id=969093006512754728&permissions=277025410048&scope=bot%20applications.commands\">link</a>."

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()