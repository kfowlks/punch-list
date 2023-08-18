from ._anvil_designer import IssueViewTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..ProjectEdit import ProjectEdit

class IssueView(IssueViewTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.

  def submit_button_click(self, **event_args):
    title = self.title_box.text
    ref = self.ref_box.text
    client_name = self.client_name_box.text
    project_date = self.project_date_picker.date
    comment = self.comment_area.text
    tags = self.tags_box.text
    self.clear_inputs()

  def clear_inputs(self):
    # Clear our text boxes
    self.title_box.text = ""
    self.ref_box.text = ""
    self.client_name_box.text = ""
    self.project_date_picker.date = ""
    self.comment_area.text = ""
    self.tags_box.text = ""

  def submit_button_hide(self, **event_args):
    """This method is called when the Button is removed from the screen"""
    pass

  def ref_box_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def form_refreshing_data_bindings(self, **event_args):
    """This method is called when refreshing_data_bindings is called"""
    pass

  def delete_project_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    print(self.item)
    if confirm(f"Are you sure you want to delete {self.item['Title']}?"):
      self.parent.raise_event('x-delete-project', project_dict=self.item)

  def edit_project_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    # Create a copy of the existing article from the Data Table
    project_copy = dict(self.item)
    # Open an alert displaying the 'ArticleEdit' Form
    # set the `self.item` property of the ArticleEdit Form to a copy of the article to be updated
    save_clicked = alert(
        content=ProjectEdit(item=project_copy),
        title="Update Project",
        large=True,
        buttons=[("Save", True), ("Cancel", False)]
      )
    # Update the article if the user clicks save
    if save_clicked:
      anvil.server.call('update_project', self.item, project_copy)

     # Now refresh the page
    self.refresh_data_bindings()

  def title_show(self, **event_args):
    """This method is called when the Label is shown on the screen"""
    pass
