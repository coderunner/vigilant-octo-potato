from flask import Flask
from flask import request
from flask import render_template
from flask import make_response

app = Flask(__name__)

NB_COOKIES_KEY = 'nb_cookies'

@app.route("/cookies")
def index():
    nb_cookies = int(request.cookies.get(NB_COOKIES_KEY, "0"))
    nb_eaten = nb_cookies + 1
    response = make_response(render_template( 'cookies/index.html', nb_cookies = nb_eaten))
    response.headers['cache-control'] = 'no-cache'
    response.set_cookie(NB_COOKIES_KEY, str(nb_eaten))
    return response
