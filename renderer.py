#!/usr/bin/python3
##
# @file aptly-ws/renderer.py.
#
# @brief    Renderer Module

from jinja2 import Environment, FileSystemLoader
import falcon
from jsmin import jsmin
import os
from os import listdir
from os.path import isfile, join
from Model import data
import json
import aptly_wa

##
# @class    api
#
# @brief    The API handler.
#
# @author   rfolkker
# @date 1/10/2024
#
# @param    self     The class instance that this method operates on.
# @param    config   Configuration dictionary.

class api:
   config = None
   api_url = ""
   api_functions = {}
   def __init__(self, config):
      self.config = config
      api_url = self.config.get("api").get("aptly_url")
      # This should be switched to a programatic way of creating
      self.api_functions = {
         "Repo":aptly_wa.api.Repo(api_url),
         "Package":aptly_wa.api.Package(api_url)
      }

   ##
   # @fn    on_get(self, req, resp, function_name)
   #
   # @brief Executes the 'get' action
   #
   # @author    rfolkker
   # @date  1/10/2024
   #
   # @param     self            The class instance that this method operates on.
   # @param     req             The request.
   # @param     resp            The response.
   # @param     function_name   Name of the function.

   def on_get(self, req, resp, function_name):
    resp.content_type = falcon.MEDIA_JSON
    api_call = self.api_functions.get(function_name, aptly_wa.api.API)
    api_action = req.params.get("action","")
    api_data = req.params
    resp.text = json.dumps(api_call.run(api_action, api_data))
    print(f"Get function called for {function_name}")

   ##
   # @fn    on_post(self, req, resp, function_name)
   #
   # @brief Executes the 'post' action
   #
   # @author    rfolkker
   # @date  1/10/2024
   #
   # @param     self            The class instance that this method operates on.
   # @param     req             The request.
   # @param     resp            The response.
   # @param     function_name   Name of the function.

   def on_post(self, req, resp, function_name):
    resp.content_type = falcon.MEDIA_JSON
    resp.text = json.dumps({"function": function_name,"action":"post"})
    print(f"Post function called for {function_name}")

   ##
   # @fn    on_patch(self, req, resp, function_name)
   #
   # @brief Executes the 'patch' action
   #
   # @author    rfolkker
   # @date  1/10/2024
   #
   # @param     self            The class instance that this method operates on.
   # @param     req             The request.
   # @param     resp            The response.
   # @param     function_name   Name of the function.

   def on_patch(self, req, resp, function_name):
    resp.content_type = falcon.MEDIA_JSON
    resp.text = json.dumps({"function": function_name,"action":"patch"})
    print(f"Patch function called for {function_name}")

   ##
   # @fn    on_delete(self, req, resp, function_name)
   #
   # @brief Executes the 'delete' action
   #
   # @author    rfolkker
   # @date  1/10/2024
   #
   # @param     self            The class instance that this method operates on.
   # @param     req             The request.
   # @param     resp            The response.
   # @param     function_name   Name of the function.

   def on_delete(self, req, resp, function_name):
    resp.content_type = falcon.MEDIA_JSON
    resp.text = json.dumps({"function": function_name,"action":"delete"})
    print(f"Delete function called for {function_name}")

##
# @class    script
#
# @brief    The script handler.
#
# @author   rfolkker
# @date 1/10/2024
#
# @param    self     The class instance that this method operates on.
# @param    config   Configuration dictionary.

class content:
   config = None
   content_root = "content/"
   content_list = {}
   content_types ={}
   def __init__(self, config):
      self.config = config
      self.content_root = self.config.get("page").get("content", self.content_root)
      file_list = listdir(self.content_root)
      # Load each script file into dictionary for proper loading
      self.content_list = {
         keyname:join(self.content_root, keyname) 
         for keyname in file_list 
         if isfile(join(self.content_root, keyname))}
      ext_list = list(set([name.split(".")[-1] for name in file_list if not name.startswith("__")]))
      # Currently only accepting js, json and css files as content
      # In the future, use the list generated to build a logical content list
      self.content_types = {"js":falcon.MEDIA_JS, "json":falcon.MEDIA_JSON, "css":"text/css"}
   ##
   # @fn    on_get(self, req, resp, script)
   #
   # @brief Executes the 'get' action
   #
   # @author    rfolkker
   # @date  1/10/2024
   #
   # @param     self    The class instance that this method operates on.
   # @param     req     The request.
   # @param     resp    The response.
   # @param     content  The content to send.

   def on_get(self, req, resp, content):
    resp.content_type = self.content_types.get(content.split('.')[-1], falcon.MEDIA_TEXT) #falcon.MEDIA_JS
    content_file = self.content_list.get(content,None)

    if content_file is None:
       resp.status = falcon.HTTP_404
    else:
       with open(content_file,"r") as fp:
         resp.text = jsmin(fp.read())

##
# @class    FaviconResource
#
# @brief    handler for the favicon resource.
#
# @author   rfolkker
# @date 1/10/2024
#
# @param    self     The class instance that this method operates on.
# @param    config   Configuration dictionary.

class FaviconResource:
   config = None
   favicon_file = "favicon.ico"
   def __init__(self, config):
      self.config = config
      self.favicon_file = join(self.config.get("images", "images/"), self.config.get('ui').get("favicon", self.favicon_file))

   ##
   # @fn    on_get(self, req, resp)
   #
   # @brief Executes the 'get' action
   #
   # @author    rfolkker
   # @date  1/10/2024
   #
   # @param     self    The class instance that this method operates on.
   # @param     req     The request.
   # @param     resp    The response.

   def on_get(self, req, resp):
      # Replace 'path/to/favicon.ico' with the actual path to your favicon file
      with open(self.favicon_file, 'rb') as f:
         resp.data = f.read()
      resp.content_type = falcon.MEDIA_PNG  # Set the correct content type for your favicon

##
# @class    ui
#
# @brief    A user interface.
#
# @author   rfolkker
# @date 1/10/2024
#
# @param    self     The class instance that this method operates on.
# @param    config   Configuration dictionary.

class ui:
   page_data = None
   config = None
   routes = {}
   path_root = "templates/"
   template_env = None
   def __init__(self, config):
      self.config = config
      self.path_root = self.config.get("page").get("templates", self.path_root)
      self.page_data = data.Data(config)
      self.template_env = Environment(loader=FileSystemLoader(self.path_root))
      print("Loading template files:")
      for f in listdir(self.path_root):
         if isfile(join(self.path_root, f)) and f.endswith(".html"):
            print(f"{f} found")
            print("Creating dictionary item {}".format({f[:-5]: join(self.path_root, f)}))
            self.routes[f[:-5]] = join(self.path_root, f)
      # self.routes = {f[:-5]:join(self.path_root, f) for f in listdir(self.path_root) if isfile(join(self.path_root, f) and f.endswith(".html"))}
      print("")
   ##
   # @fn    add_template(self, name, filename)
   #
   # @brief Adds a template to the routing table
   #
   # @author    rfolkker
   # @date  1/10/2024
   #
   # @param     self        The class instance that this method operates on.
   # @param     name        The name of the route.
   # @param     filename    Filename to assign to the route.


   def add_template(self, name, filename):
     self.routes[name] = filename

   ##
   # @fn    get_page(self, name, data)
   #
   # @brief Gets a page
   #
   # @author    rfolkker
   # @date  1/10/2024
   #
   # @param     self    The class instance that this method operates on.
   # @param     name    The name.
   # @param     data    The data.
   #
   # @returns   The render page.

   def get_page(self, name, data):
      result = None
      if name in self.routes:
        template = self.template_env.get_template(f"{name}.html")
        result = template.render(data)
      return result

   ##
   # @fn    validate_page(self, page)
   #
   # @brief Validates the page
   #
   # @author    rfolkker
   # @date  1/10/2024
   #
   # @param     self    The class instance that this method operates on.
   # @param     page    The page to validate.
   #
   # @returns   True.

   def validate_page(self, page):
      if not (page in self.routes.keys()):
         return False # Short circuit
      if os.path.isfile(self.routes[page]):
         is_valid = not os.path.islink(self.routes[page])

      return is_valid

   ##
   # @fn    on_get(self, req, resp, page)
   #
   # @brief Executes the 'get' action
   #
   # @author    rfolkker
   # @date  1/10/2024
   #
   # @param     self    The class instance that this method operates on.
   # @param     req     The request.
   # @param     resp    The response.
   # @param     page    The page.

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
            resp.text = result
    else:
      if not self.validate_page(page):
          resp.status = falcon.HTTP_404
      else: # We have a valid page
        # repo = api.Repo(self.config.config.get("api").get("aptly_url"))

        # page_data = repo.get_repos(self.config)
        result = self.get_page(page, {"page_data":self.page_data.get_data(page)()})
        if result is None:
              resp.status = falcon.HTTP_500
        else:
              resp.status = falcon.HTTP_200
              resp.text = result

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
