from starlette.requests import Request
from fastapi import APIRouter, Path
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from typing import Optional
from sys import path
from os.path import join
from os import getenv

path.append(join(getenv('APP_PATH')))

from src.api.rest.controller.user_controller import UserController
from src.api.rest.pydantic.user import UserItem

Router = APIRouter()

@Router.get(
    '/ip_client'
    , tags=['verification']
)
def get_client_ip(request: Request) -> Optional[str]:
    return JSONResponse(
        status_code=200
        , content={
            'status_code': 200
            , 'ip_client_request': request.client.host
        }
    )
    # return 

@Router.post(
    '/login'
    , tags=['auth']
)
def login():
    """
    Realização de login.
    Retorno válido é um token JWT.
    """
    return JSONResponse(
        status_code=200
        , content={
            'status_code': 200
            , 'message': 'Ainda a ser implementado métodos de autenticação e RBAC'
        }
    )

@Router.get(
    '/user'
    , tags=['users']
)
def get_users():
    """
    Busca dados de todos os usuários.
    Valido somente caso seja um administrador da organização.
    """
    users = UserController().getAll()
    return JSONResponse(
        status_code=users['status_code']
        , content=jsonable_encoder(users)
    )
    return {
        'status_code': 200
        , 'users': jsonable_encoder(users)
    }

@Router.post(
    '/user'
    , tags=['users']
)
def create_user(User: UserItem):
    """
    Insere um novo usuário.
    Valido somente caso seja um administrador da organização.
    """
    # return jsonable_encoder(User)
    users = UserController().create(User)
    return JSONResponse(
        status_code=users['status_code']
        , content=jsonable_encoder(users)
    )

@Router.get(
    '/user/me'
    , tags=['users']
)
def get_user():
    """
    Busca os dados do usuário logado.
    """
    # user = UserController.get('me')
    # UserController.getMe()

    return {
            'status_code': 200
            , 'message': 'Ainda a ser implementado métodos de autenticação e RBAC'
        }

@Router.get(
    '/user/{id}'
    , tags=['users']
)
def get_user_id(
    id: int = Path(describe='Código do usuário que se deseja consultar dados')
):
    """
    Busca os dados de um usuário específico.
    Valido somente caso seja um administrador da organização.
    """
    user = UserController().get(id)
    return JSONResponse(
        status_code=user['status_code']
        , content=jsonable_encoder(user)
    )