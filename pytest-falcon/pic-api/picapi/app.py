import falcon
from .images import Resource

app = application = falcon.API()

images = Resource()
app.add_route('/images', images)

