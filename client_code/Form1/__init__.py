from ._anvil_designer import Form1Template
from anvil import *
import anvil.server


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

def submit_button_click(self, **event_args):
  # Set 'name' to the text in the 'name_box'
  name = self.name_box.text
  # Set 'email' to the text in the 'email_box'
  email = self.email_box.text
  # Set 'feedback' to the text in the 'feedback_box'
  feedback = self.feedback_box.text