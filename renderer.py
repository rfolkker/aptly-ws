from jinja2 import Template
import falcon
import os

class ui:
   config = None
   routes = {"index":"Template/index.html"}
   def __init__(self, config):
      self.config = config

   def add_template(self, name, filename):
     self.routes[name] = filename

   def get_page(self, name, data):
      result = None
      if name in self.routes:
        with open(self.routes[name],"r") as fp:
            tempobj=Template(fp.read())
            result = tempobj.render(data)
      return result
   
   def validate_page(self, page):
      is_valid = False
      path_root = self.config.get("templates", "Template/")
      test_path = f"{path_root}{page}.html"
      if os.path.isfile(test_path):
         is_valid = not os.path.islink(test_path)

      return is_valid
   
   def on_get(self, req, resp, page):
    """Handles GET requests"""
    resp.content_type = falcon.MEDIA_HTML
    # Special handling for root page:

    if page == "":
      result = self.get_page("index", {"testing":"Hello World"})
      if result is None:
            resp.status = falcon.HTTP_500
      else:
            resp.status = falcon.HTTP_200
            resp.body = result
    else:
      if not self.validate_page(page):
          resp.status = falcon.HTTP_404
      else: # We have a valid page
        result = self.get_page(page, {"testing":"Hello World"})
        if result is None:
              resp.status = falcon.HTTP_500
        else:
              resp.status = falcon.HTTP_200
              resp.body = result
