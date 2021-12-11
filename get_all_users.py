"""
This script demonstrates how to get all the users from the network,
and write all the data to a json file for future usage.
"""

import requests
import json

#Use your personal token to request all the profiles from the network.
token = "insert token obtained from login.py"
url = "http://35.242.203.63/api/pre/DEVGetAllProfiles.php"
request = requests.post(url, headers = {"Authorization": token})
response = request.json()
usersArray = response["message"] #The message field will contain an array with all the users in the network.

#Write all users data to a json file.
file = open("firespark_users.json", "w")

file.write(json.dumps(usersArray, indent = 4))
file.close()