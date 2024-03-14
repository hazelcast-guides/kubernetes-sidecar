from hazelcast import HazelcastClient
from flask import Flask
from flask import request

import logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)


hazelcastClient = HazelcastClient(
    cluster_name="dev"
)

@app.route("/put")
def put():
    key = request.args.get('key')
    value = request.args.get('value')

    map = hazelcastClient.get_map("map")
    oldValue = map.put(key, value)

    return to_string(oldValue)


@app.route("/get")
def get():
    key = request.args.get('key')

    map = hazelcastClient.get_map("map")
    value = map.get(key)

    return to_string(value)


def to_string(value):
    if value is None:
        return ''
    if value.result() is None:
        return ''
    return str(value.result())


if __name__ == '__main__':
    app.run(host='0.0.0.0')