import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#

@anvil.server.callable
def get_projects():
   me = anvil.users.get_user()   
   if me:
     return app_tables.projects.client_writable(Owner = me).search(tables.order_by("Created", ascending=False))

@anvil.server.callable
def add_project(project_dict):
  app_tables.projects.add_row( Created=datetime.now(),
                               Owner = anvil.users.get_user(),
                               **project_dict )