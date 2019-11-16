from app import app
from flask import Flask, json, jsonify
from flask import request,Response

@app.route('/')

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    pg_id = '110330053759491'
    if request.method == "GET":
        VERIFY_TOKEN = 'fbsfhachatohon2019'
        mode = request.args.get('hub.mode')
        challenge = request.args.get('hub.challenge')
        verify_token = request.args.get('hub.verify_token')

        print(mode)
        print(challenge)
        print(verify_token)


        if (mode == "subscribe" and verify_token == VERIFY_TOKEN):
          # Responds with the challenge token from the request
          print("WEBHOOK_VERIFIED")
          # response.jsonify(challenge), 200
          return challenge, 200
        else:
            return 403
          # Responds with '403 Forbidden' if verify tokens do not match
          # response.sendStatus(403)
        # return 'here'
    else:
        body = request.data
        print(body)
        return 'post..........'

@app.route('/index')
def index():
    return "Hello, World!"
