import colander
import deform

class UserLoginSchema(colander.Schema):
    """docstring for UserLoginSchema"""
    email = colander.SchemaNode(colander.String(), validator=colander.Email())
    password = colander.SchemaNode(colander.String(), 
                                   widget=deform.widget.PasswordWidget())
