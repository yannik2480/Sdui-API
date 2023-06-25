import requests
import json

class sdui_api:
    def __init__(self):
        self.payload = None
        self.base_url = f"https://api.sdui.app/v1/"
        with open("settings.json", "r") as f:
            self.content = f.read()
        self.settings = json.loads(self.content)
        self.api_url = None
        self.headers = {
            'Authorization': self.settings["access_token"]
        }
        if self.settings["access_token"] is None:
            self.login()
        if self.settings["user_id"] is None:
            self.get_user_infomation()

    def get_user_infomation(self):
        self.api_url = self.base_url + "users/self"
        response = requests.request("GET", self.api_url, headers=self.headers)
        if self.settings["user_id"] is None:
            response_data = json.loads(response.text)
            self.settings["user_id"] = response_data["data"]["id"]
            with open("settings.json", "w") as f:
                f.write(json.dumps(self.settings, indent=4))
        return self.handle_error(response)

    def get_parent_infomation(self):
        self.api_url = self.base_url + "users/self/family"
        response = requests.request("GET", self.api_url, headers=self.headers)
        return self.handle_error(response)

    def get_timetable(self):
        self.api_url = self.base_url + f"timetables/users/{self.settings['user_id']}/timetable"
        response = requests.request("GET", self.api_url, headers=self.headers)
        return self.handle_error(response)

    def get_news(self):
        self.api_url = self.base_url + f"users/{self.settings['user_id']}/feed/news?"
        response = requests.request("GET", self.api_url, headers=self.headers)
        return self.handle_error(response)

    def handle_error(self, response):
        switcher = {
            200: lambda: response.text,
            400: lambda: (print("Wrong Email or Password"), exit(400)),
            401: lambda: (print("Empty settings.json, this is a bug please report it"), response.status_code),
        }
        return switcher.get(response.status_code, lambda: response.status_code)()

    def login(self):
        self.api_url = self.base_url + "auth/login"
        self.payload = json.dumps({
            "identifier": self.settings["email"],
            "password": self.settings["password"],
            "slink": self.settings["school"]
        })
        self.headers = {
            'content-type': 'application/json'
        }
        response = requests.request("POST", self.api_url, headers=self.headers, data=self.payload)
        print(response.text)
        if response.status_code == 200:
            response_data = json.loads(response.text)
            self.settings["access_token"] = "Bearer " + response_data["data"]["access_token"]
            with open("settings.json", "w") as f:
                f.write(json.dumps(self.settings, indent=4))
            self.__init__()
            return "Updated access_token"
        else:
            return response.status_code