# SDUI API User Class

This code provides a Python class, called sdui-api, that allows interaction with the SDUI API to retrieve user-related information, family information, timetables, and news. The class handles authentication, makes API requests, and handles errors appropriately.

## Installation

1. Clone the repository or download the code.
2. Ensure that Python 3.x is installed on your system.
3. Install the required dependencies by running the following command:
```bash
pip install requests
```
## Usage

1. Import the user.py
```python
from sdui_api.py import sdui_api()
```
2. Use the API:
```python
news = user_instance.get_news()
print(news)
```

## Class Methods

**get_user_infomation()**: Retrieves user information from the SDUI API.

**get_parent_infomation()**: Retrieves family information from the SDUI API.

**get_timetable()**: Retrieves the timetable for the user from the SDUI API.

**get_news()**: Retrieves news for the user from the SDUI API.

**login()**: Performs the login process to authenticate with the SDUI API, to get the access_token.

## Configuration

Before using the sdui_api class, make sure to configure the settings in the "settings.json" file. The file should contain the following keys:

access_token: You dont need to change that 
user_id: You dont need to change that
email: The email address of the user.
password: The password for the user.

## Example
```python
import requests
import json

# Create an instance of the User class
user_instance = User()

# Retrieve news for the user
news = user_instance.get_news()

# Print the news
print(news)
```
**Contributing**

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please open an issue or submit a pull request.
