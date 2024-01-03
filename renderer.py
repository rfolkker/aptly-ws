from jinja2 import Template
import falcon
import os
from os import listdir
from os.path import isfile, join
class script:
   config = None

   def __init__(self, config):
      self.config = config

   def on_get(self, req, resp, script):
    """Handles GET requests"""
    resp.content_type = falcon.MEDIA_JS
    with open(f"Scripts/{script}","r") as fp:
      resp.body = fp.read()

class ui:
   config = None
   routes = {}
   path_root = "Template/"

   def __init__(self, config):
      self.config = config
      self.path_root = self.config.get("templates", self.path_root)
      for f in listdir(self.path_root):
         if isfile(join(self.path_root, f)) and f.endswith(".html"):
            print(f"{f} found")
            print("Creating dictionary item {}".format({f[:-5]: join(self.path_root, f)}))
            self.routes[f[:-5]] = join(self.path_root, f)
      # self.routes = {f[:-5]:join(self.path_root, f) for f in listdir(self.path_root) if isfile(join(self.path_root, f) and f.endswith(".html"))}

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
      if not (page in self.routes.keys()):
         return False # Short circuit
      if os.path.isfile(self.routes[page]):
         is_valid = not os.path.islink(self.routes[page])

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
