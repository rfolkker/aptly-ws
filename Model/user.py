#!/usr/bin/python3
##
# @file Model/user.py.
#
# @brief    User module

from aptly_wa import api

##
# @class    User
#
# @brief    User page data handler.
#
# @author   rfolkker
# @date 1/10/2024
# 
# @param    self      The class instance that this method operates on.
# @param    config    The configuration data.

class User():
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
        # TODO this is placeholder code until API is properly defined
        return None

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
