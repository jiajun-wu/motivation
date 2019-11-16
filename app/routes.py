from app import app
from flask import Flask, json, jsonify
from flask import request, Response
import requests


pg_id = '110330053759491'
PAGE_ACCESS_TOKEN = 'EAALcUGICU5cBAL9aAExF6kCqSNzvreSOsmRBYy4tDZA5RaZCrxsZBnVtZB87IRRD2GvoSWVxIaGRg6vTsWBRvZCdyeFOT6jhuJViPyCtuyq88DGf4MHYShisme9wRJv4Bdkn6YwTzZCCUMsovhIjd8RFiG8K7INHPx1J37o4LAMAZDZD'

@app.route('/')

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
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
        # body = request.data

        json_obj = request.json.get('object')
        if json_obj == 'page':
            entry = request.json.get('entry')

            print('-----entry:', entry)

            print('request.json: ',request.json.get('object'))

            webhook_event = entry[0].get('messaging')[0]
            sender_psid = webhook_event.get('sender').get('id')
            # get_sender_id(entry[0].get('messaging')[0].get('sender').get('id'))

            print('-'*100)

            if webhook_event.get('message'):
                handleMessage(sender_psid, webhook_event.get('message'))
            elif (webhook_event.get('postback')):
                handlePostback(sender_psid, webhook_event.get('postback'))

            return 'EVENT_RECEIVED', 200
        else:
            return 404

@app.route('/index')
def index():
    return "Hello, World!"



def get_sender_id(in_text):
    print('gotit:', pg_id)

def handleMessage(sender_psid, received_message):
    if (received_message.get('text')):
        # Create the payload for a basic text message
        res_text = 'You sent the message: {}. Now send me an image!'.format(received_message.get('text'))
        response = {
          "text": res_text
        }
        callSendAPI(sender_psid, response)
        print(response)

def handlePostback(sender_psid, received_postback):
    pass

def callSendAPI(sender_psid, response):
    request_body = {
        "recipient": {
            "id": sender_psid
        },
        "message": response
    }

    print(sender_psid)
    print(request_body)


    # r = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=EAALcUGICU5cBAL9aAExF6kCqSNzvreSOsmRBYy4tDZA5RaZCrxsZBnVtZB87IRRD2GvoSWVxIaGRg6vTsWBRvZCdyeFOT6jhuJViPyCtuyq88DGf4MHYShisme9wRJv4Bdkn6YwTzZCCUMsovhIjd8RFiG8K7INHPx1J37o4LAMAZDZD",
    # "messaging_type": "response",
    # json=request_body)

    # r = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=EAALcUGICU5cBAL9aAExF6kCqSNzvreSOsmRBYy4tDZA5RaZCrxsZBnVtZB87IRRD2GvoSWVxIaGRg6vTsWBRvZCdyeFOT6jhuJViPyCtuyq88DGf4MHYShisme9wRJv4Bdkn6YwTzZCCUMsovhIjd8RFiG8K7INHPx1J37o4LAMAZDZD", json={"recipient": {"id": 2484394754962860},"message": {"text": "im back"}})

    # print(r)
    # print(r.json())

    # return r
