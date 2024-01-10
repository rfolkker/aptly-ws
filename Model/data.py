#!/usr/bin/python3

from os import listdir
from os.path import isfile, join
from .repo import Repo
from .user import User
from .package import Package
from .cert import Cert

class Data:
    
    config = None
    def __init__(self, config):
       self.config = config
    def get_cert_data(self):
        return Cert(self.config).get_data()
    def get_package_data(self):
        return Package(self.config).get_data()
    def get_repo_data(self):
        return Repo(self.config).get_data()
    def get_user_data(self):
        return User(self.config).get_data()
    def get_default_data(self):
        return {"testing":"Hello World"}
    
    def get_data(self, name):
        # Hardcoding page mapping for now
        page_data = {"cert":self.get_cert_data, 
                     "package":self.get_package_data,
                     "repo":self.get_repo_data,
                     "user":self.get_user_data}
        return page_data.get(name, self.get_default_data)