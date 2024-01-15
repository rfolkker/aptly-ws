#!/usr/bin/python3
##
# @file aptly-ws/app.py.
#
# @brief    Application class

from aptly_wa import api

# WSGI
from waitress import serve
# Renderer
from jinja2 import Environment
# Web Framework
import falcon

#Custom classes
import renderer
import config

app_config = config.ConfigHandler("config.ini")

app = falcon.App()
template = renderer.ui(app_config.config)
api_handler = renderer.api(app_config.config)
content_handler = renderer.content(app_config.config)
favicon_handler = renderer.FaviconResource(app_config.config)
app.add_route("/{page}", template)
app.add_route("/api/{function_name}", api_handler)
app.add_route("/static/{content}",content_handler)
app.add_route('/favicon.ico', favicon_handler)

##
# @fn   main()
#
# @brief    Main entry-point for this application
#
# @author   rfolkker
# @date 1/10/2024

def main():
   serve(app, host=app_config.config.get("ui").get("bind_address",'0.0.0.0'), port=int(app_config.config.get("ui").get("port",8080)))

if __name__ == '__main__':
    main()