#!/usr/bin/python3
##
# @file aptly-ws/config.py.
#
# @brief    Configuration Module

import os

##
# @class    ConfigHandler
#
# @brief    A configuration handler.
#
# @author   rfolkker
# @date 1/10/2024
#
# @param    self               The class instance that this method operates on.
# @param    config_file_path   Full pathname of the configuration file.

class ConfigHandler:
    config = {}
    def __init__(self, config_file_path):
        self.config["page"] ={"templates":"templates/",
                "images":"images/",
                "content":"Content/",
                "api":"Model/"}
        self.config["ui"]={"favicon":"aptly-icon3x.png", 
              "bind_address":"0.0.0.0", 
              "port":8090}
        self.config["api"] = {"aptly_url":""}
        self.config = self.load_config(config_file_path)
        # Assign default permissions from environment
        page = {"templates":os.environ.get("PAGE_TEMPLATES", self.config["page"]["templates"]),
                "images":os.environ.get("PAGE_IMAGES", self.config["page"]["images"]),
                "content":os.environ.get("PAGE_CONTENT", self.config["page"]["content"]),
                "api":os.environ.get("PAGE_API", self.config["page"]["api"])}
        ui = {"favicon":os.environ.get("UI_FAVICON", self.config["ui"]["favicon"]), 
              "bind_address":os.environ.get("UI_BIND_ADDRESS", self.config["ui"]["bind_address"]), 
              "port":os.environ.get("UI_PORT", self.config["ui"]["port"])}
        api = {"aptly_url":os.environ.get("API_APTLY_URL", self.config["api"]["aptly_url"])}
        self.config["page"] = page
        self.config["ui"] = ui
        self.config["api"] = api

        print("Using the following Properties:")
        for key in self.config:
            for subkey in self.config[key]:
                print(f"{key}_{subkey}={self.config[key][subkey]}")
        print("")
        
    
    # Default parameters
    
    ##
    # @fn   load_config(self, file_path)
    #
    # @brief    Loads a configuration
    #
    # @author   rfolkker
    # @date 1/10/2024
    #
    # @param    self        The class instance that this method operates on.
    # @param    file_path   Full pathname of the file.
    #
    # @returns  The configuration data.

    def load_config(self, file_path):
        # Implement your logic to load configuration from the file
        # For simplicity, let's assume a basic key-value configuration file
        section = "global"
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    if line.strip() == "":
                        continue
                    if line.startswith("["):
                        section = line[1:].split("]")[0]
                        continue
                    key, value = line.strip().split('=')
                    self.config[section][key.strip()] = value.strip()
        except FileNotFoundError:
            print(f"Config file '{file_path}' not found. Using default configuration.")
        return self.config

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