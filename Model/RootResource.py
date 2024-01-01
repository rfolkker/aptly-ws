import falcon
from Model import BaseModel
class RootResource(BaseModel.BaseModel):
   def __init__(self, template, name, filename):
      super().__init__(template, name, filename)
 
   def on_get(self, req, resp):
    """Handles GET requests"""
    resp.content_type = falcon.MEDIA_HTML
    result = self.template.get_page(self.name, {"testing":"Hello World"})
    if result is None:
      resp.status = falcon.HTTP_404
    else:
        resp.status = falcon.HTTP_200
        resp.body = result
