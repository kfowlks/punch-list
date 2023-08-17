from ._anvil_designer import MainTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
from .ProjectEdit import ProjectEdit
from .ProjectView import ProjectView


class Main(MainTemplate):
  def __init__(self, **properties):

    # Set Form properties and Data Bindings.

    self.init_components(**properties)

    # Continue until user logs in
    while not anvil.users.login_with_form():
      pass

    self.my_projects = anvil.server.call('get_projects')

    print(self.my_projects)
    
    self.refresh_projects()
    
    #self.my_projects = [ (project['title'], project) for project in my_projects.search()]

    #for row in self.my_projects.search():
    #  pd = 


    # Any code you write here will run before the form opens.
  def refresh_projects(self):
    # Load existing projects from the Data Table, 
    # and display them in the RepeatingPanel 
    self.projects_panel.items = anvil.server.call('get_projects')
    
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""    
    new_project = {}
    
    save_clicked = alert(
      content=ProjectEdit(item=new_project),
      title="Add Project",
      large=True,
      buttons=[("Save", True), ("Cancel", False)]
    )

    if save_clicked:
      print(new_project)
      anvil.server.call('add_project', new_project)
      Notification("Project Added!").show()

  def add_project_button(self, **event_args):
      """This method is called when the button is clicked"""    
      new_project = {}
    
      save_clicked = alert(
        content=ProjectEdit(item=new_project),
        title="Add Project",
        large=True,
        buttons=[("Save", True), ("Cancel", False)]
      )

      if save_clicked:
        print(new_project)
        anvil.server.call('add_project', new_project)
        Notification("Project Added!").show()
      
      """This method is called when the button is clicked"""
      self.refresh_projects()

