from ._anvil_designer import ProjectIssuesTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .IssueEdit import IssueEdit
from .IssueView import IssueView

class ProjectIssues(ProjectIssuesTemplate):
  def __init__(self, project_id, **properties):
    # Any code you write here will run before the form opens.
    # Set Form properties and Data Bindings.    
    
    self.init_components(**properties)
    self.project_id = project_id
    self.item = anvil.server.call('get_project', self.project_id) # Get Project dict
    
    print (self.item)
    print (self.item[0])
    print (self.item['Title'])
    
    self.set_event_handler('x-delete-issue', self.delete_issue)
    self.set_event_handler('x-refresh-list', self.reload)
    
    self.repeating_panel_1.set_event_handler('x-delete-issue', self.delete_issue)   
    self.repeating_panel_1.set_event_handler('x-refresh-list', self.reload)
    
    self.repeating_panel_1.items = anvil.server.call('get_project_issues', self.item)
     
    
  def reload(self, **event_args):
    print("Reload called")
    self.repeating_panel_1.items = anvil.server.call('get_project_issues', self.item)    
  
  def add_issue_button_click(self, **event_args):
      """This method is called when the button is clicked"""    
      
      new_issue = {}
      new_issue['Project'] = self.item
    
      #new_issue['Project'] = self.item.get_id()
      save_clicked = alert(
        content=IssueEdit(item=new_issue),
        title="Add Issue",
        large=True,
        buttons=[("Save", True), ("Cancel", False)]
      )
    
      if save_clicked:        
        anvil.server.call('add_issue', new_issue)
        self.raise_event('x-refresh-list')
        Notification("Issue Added!").show()       

  def button_1_click(self, **event_args):
    open_form('Main')

  def delete_issue(self, issue_dict, **event_args):
    anvil.server.call('delete_issue', issue_dict)
    self.raise_event('x-refresh-list')

  def refresh_project(self):
   self.item = anvil.server.call('get_project', item.get_id())
   self.refresh_data_bindings()

    