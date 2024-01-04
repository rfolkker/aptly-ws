#!/usr/bin/python3

from jinja2 import Environment, FileSystemLoader
import falcon
import os
from os import listdir
from os.path import isfile, join

class script:
   config = None
   script_root = "scripts/"

   def __init__(self, config):
      self.config = config
      self.script_root = self.config.get("scripts", self.script_root)

   def on_get(self, req, resp, script):
    resp.content_type = falcon.MEDIA_JS
    script_file = join(self.script_root,script)
    with open(script_file,"r") as fp:
      resp.body = fp.read()

class FaviconResource:
   config = None
   favicon_file = "favicon.ico"
   def __init__(self, config):
      self.config = config
      self.favicon_file = join(self.config.get("images", "images/"), self.config.get("favicon", self.favicon_file))

   def on_get(self, req, resp):
      # Replace 'path/to/favicon.ico' with the actual path to your favicon file
      with open(self.favicon_file, 'rb') as f:
         resp.data = f.read()
      resp.content_type = falcon.MEDIA_PNG  # Set the correct content type for your favicon

class ui:
   config = None
   routes = {}
   path_root = "templates/"
   template_env = None
   def __init__(self, config):
      self.config = config
      self.path_root = self.config.get("templates", self.path_root)

      self.template_env = Environment(loader=FileSystemLoader(self.path_root))

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
        template = self.template_env.get_template(f"{name}.html")
        result = template.render(data)
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
              resp.text = result

# This file has no main
def main():
    pass

if __name__ == '__main__':
    main()