"""
This script demonstrates how to get all the users from the network,
and write all the data to a json file for future usage.
"""

import requests
import json
import os.path
import constants

#Paste your token here, or let the script read it from the token file.
token = None

#Try to read the token from file.
if os.path.isfile(constants.TOKEN_FILE):
    with open(constants.TOKEN_FILE) as file:
        token = file.readline()

if not token:
    print("Use login.py to log into the network and get your API Token first.")
    exit()

#Make a POST request to the server to get the users.
response = requests.post(constants.GET_ALL_USERS_URL, headers = {"Authorization": token}).json()
usersArray = response["message"] #The message field will contain an array with all the users in the network.

#Write all the users data to a json file.
file = open(constants.USERS_FILE, "w")

file.write(json.dumps(usersArray, indent = 4))
file.close()

print("Users data has been written to", constants.USERS_FILE)