from functools import wraps
from flask import request

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return {"message": "No autorizado"}, 401
        try:
            if not token.startswith('Bearer '):
                return {"message": "Formato de token inválido"}, 401
        except:
            return {"message": "Token inválido"}, 401
        return f(*args, **kwargs)
    return decorated 