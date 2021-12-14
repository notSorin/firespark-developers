"""
This script demonstrates how to log into the network using a POST request,
and how to grab the token required for future requests.
"""

import requests
import constants

#Make a POST request to log in using your email (or username) and password.
postData = {
    "email_or_username": "insert email or username",
    "password": "insert password"
    }

response = requests.post(constants.LOG_IN_URL, data = postData).json()

#The response will contain a "token" key; make a copy of it,
#and keep it secure; it will be needed for future requests.
print(response)

#Write token to file.
with open(constants.TOKEN_FILE, "w") as file:
    file.write(response["message"]["token"])
    print("API Token has been written to", constants.TOKEN_FILE)