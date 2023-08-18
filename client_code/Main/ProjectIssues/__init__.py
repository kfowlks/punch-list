from ._anvil_designer import ProjectIssuesTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..IssueEdit import IssueEdit
class ProjectIssues(ProjectIssuesTemplate):
  def __init__(self, project_id, **properties):
    # Set Form properties and Data Bindings.
    print (project_id)
    self.init_components(**properties)
    self.item = anvil.server.call('get_project', project_id)
    
    #print(self.project_dict)
    # Any code you write here will run before the form opens.

  def add_issue_button_click(self, **event_args):
      """This method is called when the button is clicked"""    
      print(self.item)
      new_issue = {}
    
      #new_issue['Project'] = self.item.get_id()
      save_clicked = alert(
        content=IssueEdit(item=new_issue),
        title="Add Issue",
        large=True,
        buttons=[("Save", True), ("Cancel", False)]
      )
    
      print(new_issue)
    
      if save_clicked:
        print(new_issue)
        anvil.server.call('add_issue', new_issue)
        Notification("Issue Added!").show()

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
      


