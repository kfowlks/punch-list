from ._anvil_designer import Form1Template

from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users



class Form1(Form1Template):

  def __init__(self, **properties):

    # Set Form properties and Data Bindings.

    self.init_components(**properties)

    # Continue until user logs in
    while not anvil.users.login_with_form():
      pass

    self.my_projects = anvil.server.call('get_projects')

    #for row in self.my_projects.search():
    #  pd = 


    # Any code you write here will run before the form opens.
