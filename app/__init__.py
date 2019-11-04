import random
from sanic import Sanic
from sanic.response import json
from gino.ext.sanic import Gino
from sanic import Blueprint
from sanic_cors import CORS
from app.utils.middleware import setup_middleware

app = Sanic(__name__)
# app.config['CORS_AUTOMATIC_OPTIONS'] = True
# CORS(app)
setup_middleware(app)
app.config.from_envvar('APP_CONFIG_PATH')

# Extensions
db = Gino()
db.init_app(app)

from app.users import blueprint_v1
app.blueprint(blueprint_v1)




# Import endpoint
# ext_android = Android(app)
# app.config['database'] = db
# print(app.config)

# async def view_signup(request):
#     resp = await ext_android.route_signup(request=request)
#     return resp

# async def view_signin(request):
#     resp = await ext_android.route_signin(request=request)
#     return resp

# async def view_profile(request):
#     resp = await ext_android.route_profile(request=request)
#     return resp

# Route Android
# route_android = Blueprint(__name__, url_prefix='/android', version="v1")
# route_android.add_route(view_signup, '/auth/signup', methods=['POST'])
# route_android.add_route(view_signin, '/auth/signin', methods=['POST'])

# Group
# blueprint_v1 = Blueprint.group(route_android, url_prefix='/api')
# app.blueprint(blueprint_v1)









# class User(db.Model):
#     __tablename__ = 'users'

#     id = Column(BigInteger(), primary_key=True)
#     nickname = Column(String())

#     def __repr__(self):
#         return '{}<{}>'.format(self.nickname, self.id)


# @app.route("/users/<user_id>")
# async def get_user(request, user_id):
#     if not user_id.isdigit():
#         abort(400, 'invalid user id')
#     user = await User.get_or_404(int(user_id))
#     return json({'name': user.nickname})


# class RunServerCommand(Command):
#     """
#     Run the HTTP/HTTPS server.
#     """
#     app = app
#     option_list = (
#         Option('--host', '-h', dest='host'),
#         Option('--port', '-p', dest='port'),
#     )

#     def run(self, *args, **kwargs):
#         print("Oke")
#         self.app.run(
#             host=kwargs.get('host', None) or self.app.config["APP_HOST"],
#             port=kwargs.get('port', None) or self.app.config["APP_PORT"],
#             debug=self.app.config["APP_DEBUG"],
#             ssl=self.app.config["APP_SSL"],
#             workers=self.app.config["APP_WORKERS"],
#         )

