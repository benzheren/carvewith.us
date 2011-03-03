from carvewithus.models import DBSession
from carvewithus.models import User

def my_view(request):
    dbsession = DBSession()
    root = dbsession.query(User).filter(User.name==u'Ben Hu').first()
    return {'root':root, 'project':'carvewithus'}
