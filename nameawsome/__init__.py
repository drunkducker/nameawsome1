from mycroft import MycroftSkill, intent_file_handler
import re

class CustomNameSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.custom_name = "Mycroft"  # Default custom name
        self.active = False  # Set the skill to inactive by default

    def validate_custom_name(self, custom_name):
        """Validate the custom name to ensure it meets certain criteria.

        Returns True if the custom name is valid, or False otherwise.
        """
        # Ensure the custom name is at least 3 characters long
        if len(custom_name) < 3:
            return False
        
        # Ensure the custom name contains only letters and spaces
        if not re.match(r'^[a-zA-Z ]+$', custom_name):
            return False
        
        # Custom name is valid
        return True

    def is_active(self):
        """Return True if the skill is currently active, or False otherwise."""
        return self.active

    @intent_file_handler('customname.intent')
    def handle_custom_name_intent(self, message):
        # Get the custom name from the user's input
        new_custom_name = message.data.get('CustomName')
        
        # Validate the custom name
        if self.validate_custom_name(new_custom_name):
            # Update the custom name if it is valid
            self.custom_name = new_custom_name
            self.active = True  # Set the skill to active
            self.speak_dialog('customname.set', {'CustomName': self.custom_name})
        else:
            # Speak an error message if the custom name is invalid
            self.speak_dialog('customname.invalid')

    @intent_file_handler('customname.greet.intent')
    def handle_custom_name_greet_intent(self, message):
        if self.is_active():
            self.speak_dialog('customname.greet', {'CustomName': self.custom_name})
        else:
            self.speak_dialog('customname.inactive')


def create_skill():
    return CustomNameSkill()
