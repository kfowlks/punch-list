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
def get_project_issues(project):
  if app_tables.projects.has_row(project):
    return app_tables.issues.search(Project=project)
  else:
    raise Exception("Project does not exist")


@anvil.server.callable
def add_project(project_dict):
  app_tables.projects.add_row( Created=datetime.now(),
                               Owner = anvil.users.get_user(),
                               **project_dict )

@anvil.server.callable
def add_issue(issue_dict):
  app_tables.issues.add_row( Created=datetime.now(),
                               **issue_dict )


@anvil.server.callable
def delete_project(project_dict):
  # check that the article being deleted exists in the Data Table 
  if app_tables.projects.has_row(project_dict):    
    project_dict.delete()
  else:
    raise Exception("Project does not exist")

@anvil.server.callable
def delete_issue(issue_dict):
  # check that the article being deleted exists in the Data Table 
  if app_tables.issues.has_row(issue_dict):    
    issue_dict.delete()
  else:
    raise Exception("Issue does not exist")

# This function is safe: It will only update rows from the 
# `issue` table. 
@anvil.server.callable
def update_issue(issue, issue_dict):
  if app_tables.issues.has_row(issue):
    issue_dict['Updated'] = datetime.now()
    issue.update(**issue_dict)
  else:
    raise Exception('No such issue')

# This function is safe: It will only update rows from the 
# `projects` table. 
@anvil.server.callable
def update_project(project, project_dict):
  if app_tables.projects.has_row(project):
    project_dict['Updated'] = datetime.now()
    project.update(**project_dict)
  else:
    raise Exception('No such project')


# This function is safe: It will only update rows from the 
# `projects` table. 
@anvil.server.callable
def get_project(project_id):  
  return app_tables.projects.get_by_id(project_id)
