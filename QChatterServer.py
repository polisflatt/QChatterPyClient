import requests
import os
from constants import *


def getMotd():
    return requests.post("{ip}/Server/motd.php".format(ip = SERVER_IP_DNS)).text