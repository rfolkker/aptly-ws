#!/usr/bin/python3
from aptly_wa import api

class Package():
    config = None
    def __init__(self, config):
       self.config = config
    def get_data(self):
        return None
        # api_url = self.config.get("api").get("aptly_url")
        # TODO this is placeholder code until API is properly defined
        # package_data = api.Package(api_url)
        # return package_data.list() # _get(api_url)
