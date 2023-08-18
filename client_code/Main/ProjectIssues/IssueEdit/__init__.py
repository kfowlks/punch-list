from ._anvil_designer import IssueEditTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class IssueEdit(IssueEditTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.

  def Upload(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    self.item['Photo'] = file
    self.refresh_data_bindings()

