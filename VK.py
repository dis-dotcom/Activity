import requests


class VK:
    def __init__(self, token):
        self.token = token
        self.version = "5.131"
        self.method = "users.get"
        self.parameters = "user_ids={0}&fields=last_seen,online"
        self.base_url = "https://api.vk.com/method"

    def get_user_info(self, id):
        parameters = self.parameters.format(id)
        url = f"{self.base_url}/{self.method}?{parameters}&access_token={self.token}&v={self.version}"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()

        raise Exception(response.json())
