#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import argparse

class RelayCtl():

    """
    Control a 4-channel relay connected to a Raspberry Pi 2 model B v 1.1.
    """

    def __init__(self):

        self.CHANNELS = [18, 17, 22, 27]

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)


    def enable_channel(self, channel):

        # Set GPIO pins to output and turn them off

        for c in self.CHANNELS:
            GPIO.setup(c, GPIO.OUT)
            GPIO.output(c, GPIO.HIGH)

        channel = int(channel)

        # GPIO.setup(channel, GPIO.OUT)
        # GPIO.output(channel, GPIO.HIGH)

        #GPIO.output(channel, GPIO.LOW)

        # Turn on the requested channel

        GPIO.output(channel, GPIO.LOW)

        return "channel enabled"

    def disable_channel(self, channel):

        channel = int(channel)

        GPIO.setup(channel, GPIO.OUT)
        GPIO.output(channel, GPIO.HIGH)

        # GPIO.cleanup()

        return "channel disabled"

def main():

    parser = argparse.ArgumentParser(description="Relay Test Program")
    parser.add_argument("--mode", dest="mode",
                        help="enable | disable",
                        default="enable"
                       )
    parser.add_argument("--channel", type=int, dest="channel", default=18)

    args = parser.parse_args()
    mode = args.mode
    channel = args.channel  

    relay = RelayCtl()

    if mode == "enable":
        relay.enable_channel(channel)
    elif mode == "disable":
        relay.disable_channel(channel)

if __name__ == "__main__":

    main()
