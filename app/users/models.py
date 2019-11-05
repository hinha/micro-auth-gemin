import asyncio, random, os
import geoip2.database
from datetime import datetime
from asyncpg.exceptions import UniqueViolationError
from sqlalchemy import and_

from app.models.users import (Individuals, UserAccount, ImageAccounts, Images, Roles, UserRoles)
from app.models.users import InetProtocol, UserLogin
from app.utils.security_password import hash_password, verify_password
from app.utils import response_json

async def UserLoginAccount(email, password, raw_date=None, header={}):
    try:
        # results_login = asyncio.create_task(TaskAccount(email, password, 1, header))
        # to_list = list(await results_login)

        is_account = await UserAccount.query.where(UserAccount.email==email).gino.first()
        if not is_account:
            return False
        if verify_password(password, is_account.password) and is_account != None:
            task_check = asyncio.create_task(TaskCheckIpaddress(is_account.user_account_id, header, 1))
            await task_check
            return True

    except UniqueViolationError as uve:
        print('2 ',uve)
        return False

async def UserRegisterAccount(raw_data={}, header={}):
    try:
        is_user = await Individuals.query.where(Individuals.phone == raw_data['phone']).gino.first()
        is_email = await UserAccount.query.where(UserAccount.email == raw_data['email']).gino.first()
        if not is_user and not is_email:
            task1 = asyncio.create_task(TaskIndividuals(raw_data, header,1))
            
            await asyncio.wait([task1])
            return True
        else:
            return False

    except UniqueViolationError as uve:
        print('1 ',uve)
        return False

'''
    Task Loop
'''

async def TaskIndividuals(raw_data, header,timesleep):
    results_init = await Individuals.create(
        firstname=raw_data['firstname'],
        lastname=raw_data['lastname'],
        phone="",
        dateofbirth=datetime.strptime(raw_data['date_of_birth'], '%Y-%m-%d').date(),
        address=raw_data['address']
    )
    latency = (timesleep - random.random())  # in seconds
    # await asyncio.sleep(latency)
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

    results_role = await Roles.create(description='active')
    await UserRoles.create(role_id=str(results_role), user_account_id=str(results_account))
    await asyncio.sleep(latency)

async def TaskAccount(email, password, timesleep, header):

    latency = (timesleep - random.random())  # in seconds

    try:
        is_account = await UserAccount.query.where(UserAccount.email==email).gino.first()
    
        return [is_account.user_account_id, is_account.password]
    except:
        return [0,'fails']


async def TaskCheckIpaddress(user_id, header={},timesleep=None):

    latency = (timesleep - random.random())  # in seconds
    files = os.getcwd() + '/app/sample/data/GeoLite2.mmdb'
    reader = geoip2.database.Reader(files)
    read_address = reader.city(header['ip'])
    
    try:
        city = read_address.city.name
        country = read_address.country.name
        latitudes = read_address.location.latitude
        longitudes = read_address.location.longitude
        
    except Exception as e:
        print(e)

    is_address = await InetProtocol.query.where(InetProtocol.ip_address == header['ip']).gino.first()
    is_login = await UserLogin.query.where(UserLogin.user_account_id == user_id).gino.first()
    if not is_address:
        await InetProtocol.create(
            ip_address=header['ip'],
            country=country,
            latitude=str(latitudes),
            longitude=str(longitudes),
            city=city
        )
    elif not is_login:
        await UserLogin.create(
            last_login=datetime.now(),
            device_name=header['device_name'],
            imei_device="tesimei",
            user_account_id=user_id,
            address_id=is_address.address_id
        )
    else:
        # if login retieve time now
        await UserLogin.update.values(last_login=datetime.now()).where(UserLogin.user_account_id == user_id).gino.scalar()

    await asyncio.sleep(latency)