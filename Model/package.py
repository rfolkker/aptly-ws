#!/usr/bin/python3
##
# @file Model/package.py.
#
# @brief    Package module

from aptly_wa import api

##
# @class    Package
#
# @brief    Package page data handler.
#
# @author   rfolkker
# @date 1/10/2024
# 
# @param    self      The class instance that this method operates on.
# @param    config    The configuration data.

class Package():
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
    # @returns   Will return a data dictionary to be used on the user page.

    def get_data(self):
        api_url = self.config.get("api").get("aptly_url")
        package = api.Package(api_url)
        packages = package.list()
            
        return packages

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
