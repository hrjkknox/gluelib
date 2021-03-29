import requests

# Removes formatting and converts the API output to a string
def outputBytesToString(outputBytes):
	strVersion = str(outputBytes)
	strVersion = strVersion[:-1]
	strVersion = strVersion[2:]
	strVersion = strVersion.replace("\\r", "")
	strVersion = strVersion.replace("\\n", "\n")
	strVersion = strVersion.replace("\\t", "\t")
	
	return strVersion

def getSessionKey(username, password, devKey):
	# Construct the query
	paramaters = {
		"api_dev_key": devKey,
		"api_user_name": username,
		"api_user_password": password
		}
	# Send request and get response
	response = requests.post(url = "https://pastebin.com/api/api_login.php", data = paramaters)
	# Remove formatting data
	sessionKey = outputBytesToString(response.content)
	return sessionKey

def getPaste(pasteKey, sessionKey, devKey):
	paramaters = {
		"api_dev_key": devKey,
		"api_user_key": sessionKey,
		"api_paste_key": pasteKey,
		"api_option": "show_paste"
		}
	response = requests.post(url = "https://pastebin.com/api/api_raw.php", data = paramaters)
	pasteText = outputBytesToString(response.content)
	return pasteText

# Posts a paste, and returns the paste ID.
# Full details are available at https://pastebin.com/api
def makePaste(pasteName, pasteText, devKey, sessionKey, expiryDate = "N", privacy = "0"):
	paramaters = {
		"api_option": "paste",
		"api_dev_key": devKey,
		"api_paste_code": pasteText,
		"api_paste_private": privacy,
		"api_paste_name": pasteName,
		"api_paste_expire_date": expiryDate,
		"api_user_key": sessionKey
		}
	response = requests.post(url = "https://pastebin.com/api/api_post.php", data = paramaters)
	output = outputBytesToString(response.content)
	return output

def deletePaste(pasteKey, sessionKey, devKey):
	paramaters = {
		"api_dev_key": devKey,
		"api_user_key": sessionKey,
		"api_paste_key": pasteKey,
		"api_option": "delete"
		}
	response = requests.post(url = "https://pastebin.com/api/api_post.php", data = paramaters)
	output = outputBytesToString(response.content)
	return output

def listUserPastes(sessionKey, devKey, resultsLimit=50):
	parameters = {
		"api_dev_key": devKey,
		"api_user_key": sessionKey,
		"api_results_limit": resultsLimit,
		"api_option": "list"
	}
	response = requests.post(url = "https://pastebin.com/api/api_post.php", data = parameters)
	output = outputBytesToString(response.content)
	return output

