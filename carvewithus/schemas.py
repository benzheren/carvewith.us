from formencode import validators, Schema

class Login(Schema):
    allow_extra_fields = True
    filter_extra_fields = False
    email = validators.Email(not_empty=True)
    password = validators.String(not_empty=True)


class Signup(Schema):
    allow_extra_fields = True
    filter_extra_fields = True
    name = validators.UnicodeString(not_empty=True)
    email = validators.Email(not_empty=True)
    password = validators.String(not_empty=True)
    city = validators.OneOf(['sfo', 'nyc', 'chi', 'den', 'other'])


class Trip(Schema):
    name = validators.UnicodeString(max=50, not_empty=True)
    summary = validators.UnicodeString()
    spots_available = validators.Int(not_empty=True, min=1)
    transportation = validators.OneOf(['DRIVE', 'BUS'])
    has_lodge = validators.Bool()
    lodge_desc = validators.UnicodeString()

    

    
