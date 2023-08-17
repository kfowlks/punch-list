from ._anvil_designer import ProjectEditTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class ProjectEdit(ProjectEditTemplate):
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

  def file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    self.item['MainPhoto'] = file
    self.refresh_data_bindings()




  