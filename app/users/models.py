from datetime import datetime
import asyncio, random
from asyncpg.exceptions import UniqueViolationError

from app.models.users import (Individuals, UserAccount, ImageAccounts, Images, Roles, UserRoles)
from app.utils.security_password import hash_password, verify_password
from app.utils import response_json

async def UserLoginAccount(email, password, raw_date=None):
    try:
        results_login = asyncio.create_task(TaskAccount(email, password, 1))

        if verify_password(password, await results_login):
            return response_json.JSON_200_1
        else:
            return response_json.JSON_409_3

    except UniqueViolationError as uve:
        print('2 ',uve)
        return False

async def UserRegisterAccount(raw_data={}):
    try:
        loop = asyncio.get_event_loop()
        is_user = await Individuals.query.where(Individuals.phone == raw_data['phone']).gino.first()
        is_email = await UserAccount.query.where(UserAccount.email == raw_data['email']).gino.first()
        if not is_user and not is_email:
            
            task_Individuals = asyncio.create_task(TaskIndividuals(raw_data, 1))
            await task_Individuals

            return True
        else:
            return False

    except UniqueViolationError as uve:
        print('1 ',uve)
        return False

'''
    Task Loop
'''

async def TaskIndividuals(raw_data, timesleep):
    results_init = await Individuals.create(
        firstname=raw_data['firstname'],
        lastname=raw_data['lastname'],
        phone=raw_data['phone'],
        dateofbirth=datetime.strptime(raw_data['date_of_birth'], '%Y-%m-%d').date(),
        address=raw_data['address']
    )
    latency = (timesleep - random.random())  # in seconds
    await asyncio.sleep(latency)
    results_account = await UserAccount.create(
        email=raw_data['email'],
        password=hash_password(raw_data['password']),
        individual_id=str(results_init)
    )

    results_image = await Images.create()
    await ImageAccounts.create(
        individual_id=str(results_init),
        image_id=str(results_image)
    )
    await asyncio.sleep(latency)

    results_role = await Roles.create(description='active')
    await UserRoles.create(role_id=str(results_role), user_account_id=str(results_account))

async def TaskAccount(email, password, timesleep):
    latency = (timesleep - random.random())  # in seconds
    is_account = await UserAccount.select("password").where(UserAccount.email==email).gino.scalar()
    await asyncio.sleep(latency)
    
    return is_account