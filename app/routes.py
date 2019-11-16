from app import app

@app.route('/')
@app.route('/webhook')
def webhook():
    VERIFY_TOKEN = 'fbsfhachatohon2019'
    return "you here"

@app.route('/index')
def index():
    return "Hello, World!"
