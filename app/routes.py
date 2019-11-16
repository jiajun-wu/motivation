from app import app
from flask import Flask, json, jsonify
from flask import request, Response
import requests

# r_id=2484394754962860
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


            for e in entry:
                webhook_event = e.get('messaging')[0]
                sender_psid = webhook_event.get('sender').get('id')
            # get_sender_id(entry[0].get('messaging')[0].get('sender').get('id'))

                print('-'*100)

                if webhook_event.get('message'):
                    handleMessage(sender_psid, webhook_event.get('message'))
                elif (webhook_event.get('postback')):
                    handlePostback(sender_psid, webhook_event.get('postback'))

            return 'EVENT_RECEIVED', 200
        else:
            return 200

@app.route('/index')
def index():
    return "Hello, World!"



def get_sender_id(in_text):
    print('gotit:', pg_id)

def handleMessage(sender_psid, received_message):
    if (received_message.get('text')):
        # Create the payload for a basic text message
        res_text = '{}! What do you want to learn? Please choose one!'.format(received_message.get('text'))
        response = {
          "text": res_text,
          "quick_replies":[
              {
                "content_type":"text",
                "title":"Music",
                "payload":"music"
              },{
                "content_type":"text",
                "title":"Cooking",
                "payload":"cooking"
              },{
                "content_type":"text",
                "title":"Art",
                "payload":"art"
              }
          ]
        }

    if received_message.get('text') and received_message.get('quick_reply'):
        payload = received_message.get('quick_reply').get('payload')
        # switch_payload(payload)
        res_text = 'here are options for you'
        response = switch_payload(payload)

        print('\nim in the quick_reply\n')



    callSendAPI(sender_psid, response)


def handlePostback(sender_psid, received_postback):
    print('\n-------handlePostback\n')
    pass

def callSendAPI(sender_psid, response):
    print('---callSendAPI\n')
    request_body = {
        "recipient": {
            "id": sender_psid
        },
        "message": response
    }

    print(sender_psid)
    print(request_body)

    r = requests.post("https://graph.facebook.com/v5.0/me/messages?access_token=EAALcUGICU5cBAL9aAExF6kCqSNzvreSOsmRBYy4tDZA5RaZCrxsZBnVtZB87IRRD2GvoSWVxIaGRg6vTsWBRvZCdyeFOT6jhuJViPyCtuyq88DGf4MHYShisme9wRJv4Bdkn6YwTzZCCUMsovhIjd8RFiG8K7INHPx1J37o4LAMAZDZD",json=request_body)

    # r = requests.post("https://graph.facebook.com/v5.0/me/messages?access_token=EAALcUGICU5cBAL9aAExF6kCqSNzvreSOsmRBYy4tDZA5RaZCrxsZBnVtZB87IRRD2GvoSWVxIaGRg6vTsWBRvZCdyeFOT6jhuJViPyCtuyq88DGf4MHYShisme9wRJv4Bdkn6YwTzZCCUMsovhIjd8RFiG8K7INHPx1J37o4LAMAZDZD", json={"recipient": {"id": sender_psid},"message": {"text": "im back"}})

    print(r)
    print(r.json())




def switch_payload(payload):
    payload_json = ''
    if payload == 'music':
        payload_json = {
            "attachment":{
              "type":"template",
              "payload":{
                "template_type":"button",
                "text":"Try the URL button!",
                "buttons":[
                  {
                    "type":"web_url",
                    "url":"https://www.google.com/",
                    "title":"URL Button",
                    "webview_height_ratio": "full"
                  },{
                    "type":"web_url",
                    "url":"https://www.google.com/",
                    "title":"URL Button",
                    "webview_height_ratio": "full"
                  },{
                    "type":"web_url",
                    "url":"https://www.google.com/",
                    "title":"URL Button",
                    "webview_height_ratio": "full"
                  }
                ]
              }
            }
        }
    elif payload == 'cooking':
        res_text = 'here we go for other options'
        payload_json = {
          "text": res_text,
          "quick_replies":[
              {
                "content_type":"text",
                "title":"A",
                "payload":"a"
              },{
                "content_type":"text",
                "title":"B",
                "payload":"b"
              },{
                "content_type":"text",
                "title":"C",
                "payload":"c"
              }
          ]
        }
    elif payload == 'art':
        pass

    elif payload == 'a':
        payload_json = {
            "attachment":{
              "type":"template",
              "payload":{
                "template_type":"button",
                "text":"under cooking card!",
                "buttons":[
                  {
                    "type":"web_url",
                    "url":"https://www.google.com/",
                    "title":"URL Button",
                    "webview_height_ratio": "full"
                  },{
                    "type":"web_url",
                    "url":"https://www.google.com/",
                    "title":"URL Button",
                    "webview_height_ratio": "full"
                  },{
                    "type":"web_url",
                    "url":"https://www.google.com/",
                    "title":"URL Button",
                    "webview_height_ratio": "full"
                  }
                ]
              }
            }
        }

    return payload_json
