import colander
import deform

class UserLoginSchema(colander.Schema):
    """docstring for UserLoginSchema"""
    email = colander.SchemaNode(colander.String(), validator=colander.Email(), 
                                widget=deform.widget.TextInputWidget(
                                       css_class='inputtext'))
    password = colander.SchemaNode(colander.String(), 
                                   widget=deform.widget.PasswordWidget(
                                          css_class='inputtext'))

class CreateProfileSchema(colander.Schema):
    """docstring for CreateProfileSchema"""
    def __init__(self, arg):
        super(CreateProfileSchema, self).__init__()
        self.arg = arg
        
