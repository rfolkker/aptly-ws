class BaseModel:
  template = None
  name = ""
  filename = ""
  def __init__(self, template, name, filename):
    self.template = template
    self.name = name
    self.filename = filename
    self.template.add_template(name, filename)
