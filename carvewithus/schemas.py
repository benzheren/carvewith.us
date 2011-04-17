import formencode
from formencode import validators

class Login(formencode.Schema):
    allow_extra_fields=True
    filter_extra_fields = False
    email = validators.Email(not_empty=True)
    password = validators.String(not_empty=True)
    
