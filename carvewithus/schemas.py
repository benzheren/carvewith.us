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
