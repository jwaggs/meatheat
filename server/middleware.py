from firebase_admin import auth
from flask import request, abort, g
from functools import wraps


def authenticate(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # split and pop so that we strip the word bearer or token off
        dirty_id_token = request.headers.get('HTTP_AUTHORIZATION')
        if not dirty_id_token:
            abort(401, 'header authorization required.')

        id_token, decoded_token = dirty_id_token.split(' ').pop(), None
        try:
            decoded_token = auth.verify_id_token(id_token)
        except Exception as e:
            abort(401, f'jwt validation failed: {e}')

        if not id_token or not decoded_token:
            abort(401, 'missing jwt token')

        fid = decoded_token.get('uid')
        route_fid = kwargs.get('fid')

        # if fid doesn't match the fid in the route, abort.
        if route_fid is not None and route_fid != fid:
            abort(403, 'the auth token does not match the url route')

        return f(*args, **kwargs)
    return decorated_function
