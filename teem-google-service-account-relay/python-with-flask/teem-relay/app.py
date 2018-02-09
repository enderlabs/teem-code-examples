import requests
import json
from flask import Flask, request

app = Flask(__name__)

GCAL_PUSH_CALLBACK = 'https://push.teem.com/connect/google/pushcb/{}/'


def clean_headers(headers):
    """Takes headers dict and removes irrelivant headers."""
    response = dict()
    for k, v in headers.items():
        if k.upper().startswith('X'):
            response[k] = v
    return response


@app.route('/connect/google/pushcb/<watch_uuid>/', methods=['POST'])
def relay(watch_uuid):
    headers = clean_headers(request.headers)
    url = GCAL_PUSH_CALLBACK.format(watch_uuid)
    requests.post(url, headers=headers)
    return json.dumps({'success': True}), 200, {'ContentType':
                                                'application/json'}
