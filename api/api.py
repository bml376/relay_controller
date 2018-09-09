#!/usr/bin/python

import sys

sys.path = ["../"] + sys.path

from lib import RelayController
from flask import Flask, request, jsonify

app = Flask(__name__)

relay = RelayController.RelayCtl()

@app.route("/api/enable", methods=["POST"])
def enable_channel():

    channel = request.args.get("channel")

    response = relay.enable_channel(channel)

    return jsonify({"response": response})

@app.route("/api/disable", methods=["POST"])
def disable_channel():

    channel = request.args.get("channel")

    response = relay.disable_channel(channel)

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
