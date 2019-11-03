from sanic.response import json
# from .models import Individuals
# UsersCL(app).
class Android:
    def __init__(self, app):
        self.config = app.config

    async def route_signup(self, request=None):
        pass
        # async with self.config['database']:
        #     user = await Individuals.query.all()
        # return json({'name': user.firstname})

    async def route_signin(self, request=None):
        pass