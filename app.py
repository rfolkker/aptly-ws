#!/usr/bin/python3
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
script_handler = renderer.script(app_config.config)
favicon_handler = renderer.FaviconResource(app_config.config)
app.add_route("/{page}", template)
app.add_route("/static/{script}",script_handler)
app.add_route('/favicon.ico', favicon_handler)
def main():
   serve(app, host=app_config.config.get("ui").get("bind_address",'0.0.0.0'), port=int(app_config.config.get("ui").get("port",8080)))

if __name__ == '__main__':
    main()