#!/usr/bin/python3
##
# @file Model/data.py.
#
# @brief    Page data module
# 
# @param    self      The class instance that this method operates on.
# @param    config    The configuration data.

from os import listdir
from os.path import isfile, join
from .repo import Repo
from .user import User
from .package import Package
from .cert import Cert

##
# @class    Data
#
# @brief    Generic data class to return page data dynamically
#
# @author   rfolkker
# @date 1/10/2024
#
# @param    self      The class instance that this method operates on.
# @param    config    The configuration data.

class Data:
    
    config = None
    def __init__(self, config):
       self.config = config

    ##
    # @fn   get_cert_data(self)
    #
    # @brief    Gets cert data
    #
    # @author   rfolkker
    # @date 1/10/2024
    #
    # @param    self    The class instance that this method operates on.
    #
    # @returns   Cert page data dictionary.

    def get_cert_data(self):
        return Cert(self.config).get_data()

    ##
    # @fn   get_package_data(self)
    #
    # @brief    Gets package data
    #
    # @author   rfolkker
    # @date 1/10/2024
    #
    # @param    self    The class instance that this method operates on.
    #
    # @returns   Package page data dictionary.

    def get_package_data(self):
        return Package(self.config).get_data()

    ##
    # @fn   get_repo_data(self)
    #
    # @brief    Gets repo data
    #
    # @author   rfolkker
    # @date 1/10/2024
    #
    # @param    self    The class instance that this method operates on.
    #
    # @returns   Repo page data dictionary.

    def get_repo_data(self):
        return Repo(self.config).get_data()

    ##
    # @fn   get_user_data(self)
    #
    # @brief    Gets user data
    #
    # @author   rfolkker
    # @date 1/10/2024
    #
    # @param    self    The class instance that this method operates on.
    #
    # @returns   User page data dictionary.

    def get_user_data(self):
        return User(self.config).get_data()

    ##
    # @fn   get_default_data(self)
    #
    # @brief    Gets default data
    #
    # @author   rfolkker
    # @date 1/10/2024
    #
    # @param    self    The class instance that this method operates on.
    #
    # @returns   Default page data dictionary.

    def get_default_data(self):
        return {"testing":"Hello World"}

    ##
    # @fn   get_data(self, name)
    #
    # @brief    Gets a data for the cert page
    #
    # @author   rfolkker
    # @date 1/10/2024
    #
    # @param    self    The class instance that this method operates on.
    # @param    name    The name of page to return the data of.
    #
    # @returns   data based on requested page.

    def get_data(self, name):
        # Hardcoding page mapping for now
        page_data = {"cert":self.get_cert_data, 
                     "package":self.get_package_data,
                     "repo":self.get_repo_data,
                     "user":self.get_user_data}
        return page_data.get(name, self.get_default_data)

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
