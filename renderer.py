from jinja2 import Template

class ui:
   routes = {}
   def add_template(self, name, filename):
     self.routes[name] = filename

   def get_page(self, name, data):
      result = None
      if name in self.routes:
        with open(self.routes[name],"r") as fp:
            tempobj=Template(fp.read())
            result = tempobj.render(data)
      return result
