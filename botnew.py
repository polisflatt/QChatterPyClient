import os
import sys

import json

import threading

from libqchatterpy import *

import QChatterChannel
import QChatterPyFunctions
import QChatterServer
import QChatterUser

import math

def on_message(login, channel):
    while True:
        try:
            messages = json.loads(login.obtainUserMessageFromChannel(channel.channel))
            for message in messages:
                if (str(message) != "50000"):
                    json_decode = message
                    title = json_decode["title"]
                    title_status = json_decode["title_status"]
                    content = json_decode["content"]
                    
                    print(content)
                    print(title_status)

                    if (title != login.username):
                        if (content.startswith("$")):
                            command = content.split(" ")

                            if (command[1] == "hi"):
                                channel.sendMessage("Hello, there!")

                            elif (command[1] == "say"):
                                if (title_status != str(1)):
                                    channel.sendMessage("You are not operator. Not sending the message.")
                                    continue

                                channel.sendMessage(" ".join(command[2:]))

                            elif (command[1] == "dosquareroot"):
                                channel.sendMessage(str(math.sqrt(int(command[2]))))
        except Exception as ex:
                pass

username = "bot"
password = "3313"

r_channel = input("Channel: ")

login = QChatterUser.QChatterUser(username, password)
channel = QChatterChannel.QChatterChannel(r_channel, login)

login.joinChannel(channel.channel)

threading._start_new_thread(on_message, (login, channel,))

while True:
    inpu = input("cmd>")

