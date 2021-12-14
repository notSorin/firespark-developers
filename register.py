"""
This scripts demonstrates how to register on the network using a POST
request.
"""

import requests
import constants

#Fill the next fields with the new user's data.
email = "insert email"
password = "insert password"
username = "insert username"
firstLastName = "insert first and last name"
postData = {
    "email": email,
    "password": password,
    "username": username,
    "firstlastname": firstLastName
    }

response = requests.post(constants.SIGN_UP_URL, data = postData)

#The response will indicate whether the user was successfully registered,
#or if an error occurred.
print(response.json())