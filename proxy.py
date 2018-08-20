from flask import Flask
from flask import Response
from flask import request
from requests import get

app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def proxy(path):
    written_host = request.host_url
    real_site = written_host.replace(".seyahdoo","")
    url = real_site + request.full_path[1:]
    c = get(url)
    r = Response(response=c.content, status=200)
    r.headers["Content-Type"] = c.headers["Content-Type"]
    return r


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
