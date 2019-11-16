from app import app
from flask import request, response

@app.route('/')
@app.route('/webhook', methods=['GET'])
def webhook():
    VERIFY_TOKEN = 'fbsfhachatohon2019'
    challenge = request.args.get('hub.challenge')
    print challenge
    return 'here'

@app.route('/index')
def index():
    return "Hello, World!"
