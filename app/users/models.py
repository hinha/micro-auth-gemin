from datetime import datetime
from asyncpg.exceptions import UniqueViolationError

from app.models.users import (Individuals, UserAccount, ImageAccounts, Images, Roles, UserRoles)
from app.utils.security_password import hash_password

async def UserRegistsserAccount(sid, email, password):
    try:
        results = 's'
    except UniqueViolationError as uve:
        print('2 ',uve)
        return False

async def UserRegisterAccount(raw_data={}):
    try:
        is_user = await Individuals.query.where(Individuals.phone == raw_data['phone']).gino.first()
        is_email = await UserAccount.query.where(UserAccount.email == raw_data['email']).gino.first()
        if not is_user and not is_email:
            results_init = await Individuals.create(
                firstname=raw_data['firstname'],
                lastname=raw_data['lastname'],
                phone=raw_data['phone'],
                dateofbirth=datetime.strptime(raw_data['date_of_birth'], '%Y-%m-%d').date(),
                address=raw_data['address']
            )

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

            return True
        else:
            return False

    except UniqueViolationError as uve:
        print('1 ',uve)
        return False