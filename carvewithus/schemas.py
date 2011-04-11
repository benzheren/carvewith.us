import colander
import deform

from carvewithus.widgets import DivMappingWidget

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


class CreateTripOneRightMapping(colander.Schema):
    """docstring for Mapping"""
    name = colander.SchemaNode(colander.String(),
                               widget=deform.widget.TextInputWidget(
                                   css_class="text large full"), 
                               description="outer") 
    summary = colander.SchemaNode(colander.String(),
                                  widget=deform.widget.TextAreaWidget(
                                      css_class="text small full"), 
                                 description="outer")
        
class CreateTripOneSchema(colander.Schema):
    """docstring for ClassName"""
    picture = colander.SchemaNode(deform.FileData(),
                                  widget=deform.widget.FileUploadWidget(tmpstore),
                                  description="column_1 grid_3")
    right = CreateTripOneRightMapping(widget=DivMappingWidget(), description=\
                                      "grid_9 column_main")
