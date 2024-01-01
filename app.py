from waitress import serve
import falcon
from Model import RootResource
import Model

import renderer
class RootResource:
   def on_get(self, req, resp):
    """Handles GET requests"""
    
    resp.status = falcon.HTTP_200
    resp.content_type = falcon.MEDIA_TEXT
    resp.text = (
        'Hello World'
    )
app = falcon.App()
template = renderer.ui()

root = Model.RootResource.RootResource(template, "root", "Template/index.html")

app.add_route('/', root)
if __name__ == '__main__':
   serve(app, host='0.0.0.0', port=8000)