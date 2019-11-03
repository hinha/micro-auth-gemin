import asyncio, random
from sanic.response import text, json
from sanic import Blueprint

from .models import UserRegisterAccount

from app.models.users import Individuals
from app.utils import response_json

blueprint_v1 = Blueprint('v1', url_prefix='/api', version="v1")


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

    if ('firstname' not in request_forms) or ('lastname' not in request_forms) or ('email' not in request_forms):
        return json(response_json.JSON_422_1, 422)
    elif ('password' not in request_forms) or ('phone' not in request_forms) or ('date_of_birth' not in request_forms):
        return json(response_json.JSON_422_1, 422)

    raw_data = await UserRegisterAccount({
        'firstname': request_forms.get('firstname'),
        'lastname': request_forms.get('lastname'),
        'phone': request_forms.get('phone'),
        'address': request_forms.get('address'),
        'date_of_birth': request_forms.get('date_of_birth'),
        'email': request_forms.get('email'),
        'password': request_forms.get('password')
    })

    if raw_data:
        latency = (1 - random.random())  # in seconds
        await asyncio.sleep(latency)
         
        return json(response_json.JSON_200_2, 200)
    else:
        return json(response_json.JSON_409_2, 409)
    
    return json({'s': 123})
