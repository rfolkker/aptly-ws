#!/usr/bin/python3
from aptly_wa import api

class Repo():
    config = None
    def __init__(self, config):
       self.config = config
    def get_data(self):
        api_url = self.config.get("api").get("aptly_url")
        repo = api.Repo(api_url)
        return repo.list() # _get(api_url)
