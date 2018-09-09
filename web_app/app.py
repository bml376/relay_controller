#!/usr/bin/python

import requests

from flask import Flask, request, render_template, flash
from wtforms import Form, TextField, validators

app = Flask(__name__)
app.config.from_object(__name__)
app.config["SECRET_KEY"] = "relay"

# Map GPIO channels to sequential logical order
gpio_channel_map = {
    "1": 17,
    "2": 18,
    "3": 22,
    "4": 27
}

# api service URL

service_url = "http://192.168.0.10:5000"

class ReusableForm(Form):
    pass

@app.route("/")
def home():
    
    """ Render a table showing the channels with an on and off switch
    for the channel.
    """
    
    channels = sorted(gpio_channel_map.keys())

    return render_template("home.html", channels=channels)

@app.route("/_on", methods=["POST"])
def _on():
    # Get requested channel
    channel = request.form["channel"]

    # Get GPIO for channel

    gpio = gpio_channel_map[channel]

    # Request /api/enable

    uri = "/api/enable?channel=%s" % (gpio)

    url = "".join([service_url, uri])

    response = requests.post(url)

    flash(response.json())

    return render_template("home.html")

@app.route("/_off", methods=["POST"])
def _off():
    # Get requested channel
    channel = request.form["channel"]

    # Get GPIO for channel

    gpio = gpio_channel_map[channel]

    # Request /api/enable

    uri = "/api/disable?channel=%s" % (gpio)

    url = "".join([service_url, uri])

    response = requests.post(url)

    flash(response.json())

    return render_template("home.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080", debug=True) 
