from flask import Flask
from flask import request
from flask import render_template
from flask import make_response
import uuid

app = Flask(__name__)

SESSIONS = {}
SESSION_ID_COOKIE_KEY = 'sessionId'

@app.route("/cookies")
def index():
    sessionId = request.cookies.get(SESSION_ID_COOKIE_KEY)
    if sessionId == None:
        sessionId = str(uuid.uuid4())
    
    cookies = SESSIONS.get(sessionId, 0)
    SESSIONS[sessionId] = cookies + 1
    response = make_response(render_template( 'cookies/index.html', nb_cookies = SESSIONS[sessionId]))
    response.headers['cache-control'] = 'no-cache'
    response.set_cookie(SESSION_ID_COOKIE_KEY, sessionId)
    return response
