
from flask import render_template, request
from . import auth_blueprint

from onetimepass import valid_totp
from secrets import choice

from utils.func import generate_secret

SECRET = generate_secret()

@auth_blueprint.route('/two-factor-auth')
def authenticate():
    return render_template('auth/two-factor-auth.html', secret=SECRET)


@auth_blueprint.route('/validate-otp')
def validate_otp():
    otp: str = request.query_string.decode().split('=')[1]
    authenticated = valid_totp(token=otp, secret=SECRET)
    msg = 'Authentication error, try again'
    if authenticated:
        msg = 'Authenticated!'

    return render_template('auth/validate-otp.html', msg = msg)

