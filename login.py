"""
This script demonstrates how to log into the network using a POST request,
and how to grab the token required for future requests.
"""

import requests

#Make a POST request to log in using your email (or username) and password.
url = "http://35.242.203.63/api/pre/LoginUser.php"
postData = {
    "email_or_username": "insert email or username",
    "password": "insert password"
    }

response = requests.post(url, data = postData)

#The response will contain a "token" key; make a copy of it,
#and keep it secure; it will be needed for future requests.
print(response.json())