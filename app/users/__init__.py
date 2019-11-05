import os
import asyncio, random
from sanic.response import text, json
from sanic import Blueprint

from .models import UserRegisterAccount, UserLoginAccount
from .models import TaskCheckIpaddress

from app.models.users import Individuals
from app.utils import response_json

blueprint_v1 = Blueprint('v1', url_prefix='/api', version="v1")

@blueprint_v1.middleware('request')
async def before_request(request):
    rqheaders = request.headers

    # print(rqheaders)


@blueprint_v1.route('/')
async def api_v1_root(request):
    # user = await User.get_or_404(int(1))

    tes = await Individuals.select('individual_id').where(Individuals.firstname == 'Ate').gino.scalar()
    
    # print(user.nickname)
    print(tes)
    return text('Welcome to version 1 of our documentation')


@blueprint_v1.route('/auth/signup', methods=['POST'])
async def auth_view_signup(request):
    request_params = request.raw_args
    request_forms = request.form
    request_headers = request.headers

    if ('firstname' not in request_forms) or ('lastname' not in request_forms) or ('email' not in request_forms):
        return json(response_json.JSON_422_1, 422)
    elif ('password' not in request_forms) or ('phone' not in request_forms) or ('date_of_birth' not in request_forms):
        return json(response_json.JSON_422_1, 422)
    
    raw_head = {'ip': request_headers['x-real-ip'], 'device_name': request_headers['user-agent']}

    raw_data = await UserRegisterAccount({
        'firstname': request_forms.get('firstname'),
        'lastname': request_forms.get('lastname'),
        'phone': request_forms.get('phone'),
        'address': request_forms.get('address'),
        'date_of_birth': request_forms.get('date_of_birth'),
        'email': request_forms.get('email'),
        'password': request_forms.get('password')
    }, raw_head)

    if raw_data:
        return json(response_json.JSON_200_2, 200)
    else:
        return json(response_json.JSON_409_2, 409)
    
    return json({'s': 123})

@blueprint_v1.route('/auth/signin', methods=['POST'])
async def auth_view_signin(request):
    request_params = request.raw_args
    request_forms = request.form
    request_headers = request.headers

    

    raw_head = {'ip': request_headers['x-real-ip'], 'device_name': request_headers['user-agent']}
    raw_data = await UserLoginAccount(request_forms.get('email'), request_forms.get('password'), header=raw_head)

    if raw_data:
        # results_header = await TaskCheckIpaddress(raw_head)
        # print(results_header)
        return json(response_json.JSON_200_1)
    else:
        return json(response_json.JSON_409_3)