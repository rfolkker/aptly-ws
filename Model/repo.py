#!/usr/bin/python3
from aptly_wa import api

def get_repos(config):
    api_url = config.get("api").get("aptly_url")
    repo = api.Repo(api_url)
    return repo.list() # _get(api_url)