# gluelib
This is a simple library for interacting with the pastebin API. The code is fairly simple and self-documenting, and all other information needed is contained within this file. Install with `pip3 install gluelib`.

(It's called gluelib because pastelib was taken)

## Terminology
### Session Keys
When using this library, the first thing to do is generate a session key. This is what you will use instead of a username and password. Call `getSessionKey` with your pastebin username, password, and developer key, and you will receive a session key. This is used in all future API calls. Keep it in memory, and generate a new one for every session. You do not need to use your username and password again.

### Paste Keys
These are the parts of a pastebin URL that identify a specific paste. (e.g. `zvwcdXyn` in `https://pastebin.com/zvwcdXyn`)

## Functions

### `getPaste(pasteKey, sessionKey, devKey)`
Returns the text of a paste given the above parameters.

### `makePaste(pasteName, pasteText, sessionKey, devKey, expiryDate = "N", privacy = "0")`
Uploads a paste to pastebin with the above parameters. See [the pastebin API page](https://pastebin.com/doc_api "the pastebin API page") for more detail.

### `deletePaste(pasteKey, sessionKey, devKey)`
Deletes a paste given the above parameters.

### `listUserPastes(sessionKey, devKey, resultsLimit=50)`
Returns information about your pastes in XML format. Will only display last `resultslimit` results.

### `getUserData(sessionKey, devKey)`
Returns information about your user profile in XML format.

### `getSessionKey(username, password, devKey)`
Returns a session key when given a pastebin username, password, and developer key. See the section on session keys for more.

### `outputBytesToString(outputBytes)`
This function formats a response from the pastebin API. It removes the prefix and suffix bytes, converts the response to a string, and returns it. All other functions in this library pass their output through it. You do not need to use this function in your code.

