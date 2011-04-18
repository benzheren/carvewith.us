from formencode import validators, Schema

class Login(Schema):
    allow_extra_fields = True
    filter_extra_fields = False
    email = validators.Email(not_empty=True)
    password = validators.String(not_empty=True)


class Signup(Schema):
    """docstring for Signup"""
    allow_extra_fields = True
    filter_extra_fields = True
    name = validators.UnicodeString(not_empty=True)
    email = validators.Email(not_empty=True)
    password = validators.String(not_empty=True)
    city = validators.OneOf(['sfo', 'nyc', 'chi', 'den', 'other'])

    
