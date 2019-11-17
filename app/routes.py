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

            # print('-----entry:', entry)

            # print('request.json: ',request.json.get('object'))

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
        res_text = 'Hi! We are motivation! What do you want to learn? Please choose one!'.format(received_message.get('text'))
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

    r = requests.post("https://graph.facebook.com/v5.0/me/messages?access_token=EAALcUGICU5cBAL9aAExF6kCqSNzvreSOsmRBYy4tDZA5RaZCrxsZBnVtZB87IRRD2GvoSWVxIaGRg6vTsWBRvZCdyeFOT6jhuJViPyCtuyq88DGf4MHYShisme9wRJv4Bdkn6YwTzZCCUMsovhIjd8RFiG8K7INHPx1J37o4LAMAZDZD", json=request_body)

    # r = requests.post("https://graph.facebook.com/v5.0/me/messages?access_token=EAALcUGICU5cBAL9aAExF6kCqSNzvreSOsmRBYy4tDZA5RaZCrxsZBnVtZB87IRRD2GvoSWVxIaGRg6vTsWBRvZCdyeFOT6jhuJViPyCtuyq88DGf4MHYShisme9wRJv4Bdkn6YwTzZCCUMsovhIjd8RFiG8K7INHPx1J37o4LAMAZDZD", json={"recipient": {"id": sender_psid},"message": {"text": "im back"}})

    print(r)
    print(r.json())


def switch_payload(payload):
    payload_json = ''
    if payload == 'music':
        res_text = 'We got some instruments for you.'
        payload_json = {
          "text": res_text,
          "quick_replies":[
              {
                "content_type":"text",
                "title":"Piano",
                "payload":"piano"
              },{
                "content_type":"text",
                "title":"Guitar",
                "payload":"guitar"
              }
          ]
        }
    elif payload == 'piano':
        payload_json = {
            "attachment":{
              "type":"template",
              "payload":{
                "template_type":"generic",
                "elements":[
                    {
                        "title":"Yiruma's Greatest Hits ~ Best Piano",
                        "image_url":"https://i.ytimg.com/vi/8Z5EjAmZS1o/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLCYg-UGKZKc9p37VbUYn0eWZmjJTg",
                        "subtitle":"The Case for Christ (2017)",
                        "default_action": {
                          "type": "web_url",
                          "url": "https://youtu.be/8Z5EjAmZS1o",
                          "webview_height_ratio": "tall",
                        }
                    },{
                        "title":"Maksim plays Original of Flight of the Bumble Bee",
                        "image_url":"https://i.ytimg.com/vi/QM0p5bxWQnQ/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLA6nn50ZiHY_XIIIrxZUZ2Xbo8F4w",
                        "subtitle":"MAKSIM The World Premiere Performance.",
                        "default_action": {
                          "type": "web_url",
                          "url": "https://youtu.be/h6A-JYbu1Os?t=12",
                          "webview_height_ratio": "tall",
                        }
                    }
                ]
              }
            }
        }

    elif payload == 'guitar':
        payload_json = {
            "attachment":{
              "type":"template",
              "payload":{
                "template_type":"generic",
                "elements":[
                    {
                        "title":"Señorita - Shawn Mendes, Camila Cabello - Cover (fingerstyle guitar) Andrew Foy",
                        "image_url":"https://i.ytimg.com/vi/FmsM9PbqN_I/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLBExLJK5ltb5KEBaEjzbtOnPfOIsA",
                        "subtitle":"",
                        "default_action": {
                          "type": "web_url",
                          "url": "https://youtu.be/FmsM9PbqN_I",
                          "webview_height_ratio": "tall",
                        }
                    },{
                        "title":"Top 40 Acoustic Guitar Covers Of Popular Songs",
                        "image_url":"https://i.ytimg.com/vi/_UucPr2M-qU/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLARWg_Q9276IibYjsH3PaAwLBVb1g",
                        "subtitle":"Music can be magic and powerful, managing to touch our emotions.",
                        "default_action": {
                          "type": "web_url",
                          "url": "https://youtu.be/_UucPr2M-qU",
                          "webview_height_ratio": "tall",
                        }
                    }
                ]
              }
            }
        }

    elif payload == 'cooking':
        res_text = 'What type of cooking do you want to do?'
        payload_json = {
            "text": res_text,
            "quick_replies": [
                {
                    "content_type": "text",
                    "title": "Asian",
                    "payload": "asian"
                }, {
                    "content_type": "text",
                    "title": "Baking",
                    "payload": "baking"
                }, {
                    "content_type": "text",
                    "title": "European",
                    "payload": "european"
                }
            ]
        }
    elif payload == 'art':
        res_text = 'What style of art do you want to learn?'
        payload_json = {
            "text": res_text,
            "quick_replies": [
                {
                    "content_type": "text",
                    "title": "Pencil",
                    "payload": "pencil"
                }, {
                    "content_type": "text",
                    "title": "Painting",
                    "payload": "painting"
                }
            ]
        }

    elif payload == 'pencil':
        payload_json = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                        {
                            "title": "How to Draw Easy and Simple Landscape For Beginners with PENCIL",
                            "image_url": "https://i.ytimg.com/vi/UVTbFp_7L0E/maxresdefault.jpg",
                            "subtitle": "Draw beautiful landscapes.",
                            "default_action": {
                                "type": "web_url",
                                "url": "https://www.youtube.com/watch?v=UVTbFp_7L0E",
                                "webview_height_ratio": "full"
                            }
                        },
                        {
                            "title": "Portrait Drawing Basics 1/3 - How To Draw A Simple Head",
                            "image_url": "https://www.google.com/url?sa=i&source=images&cd=&ved=2ahUKEwjcnIeMh_DlAhWPuZ4KHf9XCawQjRx6BAgBEAQ&url=https%3A%2F%2Fwww.udemy.com%2Fcourse%2Fportrait-drawing-fundamentals-made-simple%2F&psig=AOvVaw1H5VBsX3jwgftZeAIIj0Gy&ust=1574039198577580",
                            "subtitle": "Learn to draw faces.",
                            "default_action": {
                                "type": "web_url",
                                "url": "https://www.youtube.com/watch?v=wz5HDRMEF1E",
                                "webview_height_ratio": "full"
                            }
                        }
                    ]
                }
            }

        }
    elif payload == 'pencil':
        payload_json = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                        {
                            "title": "How I'm Painting Simple Landscapes",
                            "image_url": "https://www.google.com/url?sa=i&source=images&cd=&ved=2ahUKEwig95fEh_DlAhVPvJ4KHY2VCMQQjRx6BAgBEAQ&url=https%3A%2F%2Fforums.artrage.com%2Fshowthread.php%3F42448-a-simple-landscape&psig=AOvVaw25ogda5RVnHWYUG8g16MRe&ust=1574038937655783",
                            "subtitle": "Paint beautiful landscapes.",
                            "default_action": {
                                "type": "web_url",
                                "url": "https://www.youtube.com/watch?v=anQ6ekGzB6s",
                                "webview_height_ratio": "full"
                            }
                        },
                        {
                            "title": "How to Paint a Portrait in 7 Steps",
                            "image_url": "https://www.google.com/url?sa=i&source=images&cd=&ved=2ahUKEwjcnIeMh_DlAhWPuZ4KHf9XCawQjRx6BAgBEAQ&url=https%3A%2F%2Fwww.udemy.com%2Fcourse%2Fportrait-drawing-fundamentals-made-simple%2F&psig=AOvVaw1H5VBsX3jwgftZeAIIj0Gy&ust=1574039198577580",
                            "subtitle": "Learn to paint faces.",
                            "default_action": {
                                "type": "web_url",
                                "url": "https://www.youtube.com/watch?v=EUeujbQRuU0",
                                "webview_height_ratio": "full"
                            }
                        }
                    ]
                }
            }

        }

    elif payload == 'asian':
        payload_json = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                        {
                            "title": "Japanese Chicken Curry チキンカレー",
                            "image_url": "https://www.justonecookbook.com/wp-content/uploads/2013/03/Simple-Chicken-Curry.jpg",
                            "subtitle": "Delicious Japanese chicken curry recipe.",
                            "default_action": {
                                "type": "web_url",
                                "url": "https://www.justonecookbook.com/wp-content/uploads/2013/03/Simple-Chicken-Curry.jpg",
                                "webview_height_ratio": "full"
                            }
                        },
                        {
                            "title": "Asian Garlic Noodles",
                            "image_url": "https://s23209.pcdn.co/wp-content/uploads/2015/12/IMG_0304edit_preview.jpg",
                            "subtitle": "Awesome garlic noodles.",
                            "default_action": {
                                "type": "web_url",
                                "url": "https://damndelicious.net/2015/12/27/asian-garlic-noodles/",
                                "webview_height_ratio": "full"
                            }
                        },
                        {
                            "title": "Fried Rice",
                            "image_url": "https://www.gimmesomeoven.com/wp-content/uploads/2017/07/How-To-Make-Fried-Rice-Recipe-2-1-1100x1650.jpg",
                            "subtitle": "The best fried rice.",
                            "default_action": {
                                "type": "web_url",
                                "url": "https://www.gimmesomeoven.com/fried-rice-recipe/",
                                "webview_height_ratio": "full"
                            }
                        }
                    ]
                }
            }
        }

    elif payload == 'baking':
        payload_json = {
            "attachment":{
              "type":"template",
              "payload":{
                "template_type":"generic",
                "elements":[
                    {
                        "title":"Chocolate Chip Cookies",
                        "image_url":"https://images.media-allrecipes.com/userphotos/720x405/7238000.jpg",
                        "subtitle":"Crisp edges, chewy middles.",
                        "default_action": {
                          "type": "web_url",
                          "url": "https://www.allrecipes.com/recipe/10813/best-chocolate-chip-cookies/",
                          "webview_height_ratio": "full",
                        }
                    },
                    {
                        "title":"chocolate cake",
                        "image_url":"https://images.media-allrecipes.com/userphotos/720x405/708879.jpg",
                        "subtitle":"This is a rich and moist chocolate cake. It only takes a few minutes to prepare the batter. Frost with your favorite chocolate frosting.",
                        "default_action": {
                          "type": "web_url",
                          "url": "https://www.allrecipes.com/recipe/17981/one-bowl-chocolate-cake-iii/",
                          "webview_height_ratio": "full",
                        }
                    },
                    {
                        "title":"Muffins",
                        "image_url":"https://images.media-allrecipes.com/userphotos/720x405/7115277.jpg",
                        "subtitle":"Crisp edges, chewy middles.",
                        "default_action": {
                          "type": "web_url",
                          "url": "https://www.allrecipes.com/recipe/6874/best-ever-muffins/",
                          "webview_height_ratio": "full",
                        }
                    }
                ]
              }
            }
        }

    elif payload == 'european':
        payload_json = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                        {
                            "title": "Pork Schnitzel",
                            "image_url": "https://i0.wp.com/natashaskitchen.com/wp-content/uploads/2016/02/Pork-Schnitzel-Recipe-7.jpg",
                            "subtitle": "Crispy pork.",
                            "default_action": {
                                "type": "web_url",
                                "url": "https://natashaskitchen.com/pork-schnitzel-recipe/",
                                "webview_height_ratio": "full"
                            }
                        },
                        {
                            "title": "Fettuccine Alfredo",
                            "image_url": "https://images-gmi-pmc.edge-generalmills.com/d6555a9d-686b-4341-9260-f3d337089802.jpg",
                            "subtitle": "Creamy pasta.",
                            "default_action": {
                                "type": "web_url",
                                "url": "https://www.allrecipes.com/recipe/23431/to-die-for-fettuccine-alfredo/",
                                "webview_height_ratio": "full"
                            }
                        }
                    ]
                }
            }
        }
    return payload_json
