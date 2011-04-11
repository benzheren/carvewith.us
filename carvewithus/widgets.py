from deform.widget import MappingWidget

class DivFormWidget(MappingWidget):
    """docstring for DivFormWidget"""
    template = "div_form"
    item_template = "div_mapping_item"


class DivMappingWidget(MappingWidget):
    """docstring for DivMappingWidget"""
    template = "div_mapping"
    item_template = "div_mapping_item"
