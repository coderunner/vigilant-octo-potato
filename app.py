from flask import Flask
from flask import request
from flask import render_template
from flask import make_response
from datetime import datetime
import uuid

app = Flask(__name__)

SESSIONS = {}
SESSION_ID_COOKIE_KEY = 'sessionId'
HTTP_ONLY_COOKIE_KEY = 'httpOnly'


@app.route("/cookies")
def index():
    sessionId = request.cookies.get(SESSION_ID_COOKIE_KEY)
    if sessionId == None:
        sessionId = str(uuid.uuid4())

    count = SESSIONS.get(sessionId, 0)
    SESSIONS[sessionId] = count + 1
    response = make_response(render_template(
        'cookies/index.html', nb_cookies=SESSIONS[sessionId]))
    print (SESSIONS)
    response.headers['cache-control'] = 'no-cache'
    response.set_cookie(SESSION_ID_COOKIE_KEY, sessionId)
    response.set_cookie(HTTP_ONLY_COOKIE_KEY, 'seulement visible sur http - non accessible dans le js - ' + str(datetime.now()), httponly=True)
    return response
