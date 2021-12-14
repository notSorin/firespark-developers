API_URL = "http://35.242.203.63/api/"

#Versions of the REST API.
API_V1_URL = API_URL + "v1/"
API_PRE_URL = API_URL + "pre/"

#Change the value of USING_API_URL with the version of the API to use.
USING_API_URL = API_PRE_URL

SIGN_UP_URL = USING_API_URL + "RegisterUser.php" #Used for registering users.
LOG_IN_URL = USING_API_URL + "LoginUser.php" #Used for logging into the network.
GET_ALL_USERS_URL = USING_API_URL + "DEVGetAllProfiles.php" #Used for getting all the users in the network.

TOKEN_FILE = "token.txt"
USERS_FILE = "firespark_users.json"