from flask import Flask
from flask import Response
from flask import request
from requests import get

app = Flask(__name__)
SITE_NAME = 'http://pastebin.com'


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def proxy(path):
    url = SITE_NAME + request.full_path
    c = get(url).content
    r = Response(response=c, status=200)
    r.headers["Content-Type"] = "text/plain; charset=utf-8"
    return r


if __name__ == '__main__':
    app.run()
