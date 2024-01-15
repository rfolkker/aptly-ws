#!/usr/bin/python3
##
# @file Model/repo.py.
#
# @brief    Repository module

from aptly_wa import api

##
# @class    Repo
#
# @brief    Repo page data handler.
#
# @author   rfolkker
# @date 1/10/2024
# 
# @param    self      The class instance that this method operates on.
# @param    config    The configuration data.

class Repo():
    config = None
    def __init__(self, config):
       self.config = config

    ##
    # @fn   get_data(self)
    #
    # @brief    Gets a data
    #
    # @author   rfolkker
    # @date 1/10/2024
    #
    # @param    self    The class instance that this method operates on.
    #
    # @returns   Will return a data dictionary to be used on the repo page.

    def get_data(self):
        api_url = self.config.get("api").get("aptly_url")
        repo = api.Repo(api_url)
        repos = repo.list()
            
        return repos #repo.list() # _get(api_url)

##
# @fn   main()
#
# @brief    Main entry-point for this application
#           This file has no main
#
# @author   rfolkker
# @date 1/10/2024

def main():
    pass

if __name__ == '__main__':
    main()
