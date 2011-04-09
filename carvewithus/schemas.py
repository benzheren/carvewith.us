import colander
import deform

class MemoryTmpStore(dict):
    """ Instances of this class implement the
    :class:`deform.interfaces.FileUploadTempStore` interface"""
    def preview_url(self, uid):
        return None

tmpstore = MemoryTmpStore()

class UserLoginSchema(colander.Schema):
    """docstring for UserLoginSchema"""
    email = colander.SchemaNode(colander.String(), validator=colander.Email(), 
                                widget=deform.widget.TextInputWidget(
                                       css_class='inputtext'))
    password = colander.SchemaNode(colander.String(), 
                                   widget=deform.widget.PasswordWidget(
                                          css_class='inputtext'))


class CreateTripOneSchema(colander.Schema):
    """docstring for ClassName"""
    picture = colander.SchemaNode(deform.FileData(),
                                  widget=deform.widget.FileUploadWidget(tmpstore))
    name = colander.SchemaNode(colander.String(),
                               widget=deform.widget.TextInputWidget(
                                   css_class="text large full")) 
    summary = colander.SchemaNode(colander.String(),
                                  widget=deform.widget.TextAreaWidget(
                                      css_class="text small full"))
