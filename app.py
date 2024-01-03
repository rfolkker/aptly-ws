from waitress import serve
import falcon
from Model import RootResource
import Model

import renderer
import config

app_config = config.ConfigHandler("config.ini")

app = falcon.App()
template = renderer.ui(app_config.config)

app.add_route("/{page}", template)
if __name__ == '__main__':
   serve(app, host=app_config.config.get("bind_address",'0.0.0.0'), port=int(app_config.config.get("port",8080)))