from sys import path
from os.path import join
from os import getenv

path.append(join(getenv('APP_PATH')))

from src.database.databases import MySQL
from src.database.ORM.user import User as UserDEF

class User:
    def me(self):
        return {'teste':'ok'}

    def get(self, id):
        with MySQL().session() as s:
            result = s.query(
                UserDEF.id
                , UserDEF.full_name
                , UserDEF.display_name
                , UserDEF.email
                , UserDEF.contact_phone
            ).where(UserDEF.id==id).all()
        result = [r._asdict() for r in result]
        
        return {
            'status_code': 200
            , 'user': {
                'full_name': result[0]['full_name']
                , 'display_name': result[0]['display_name']
                , 'email': result[0]['email']
                , 'contact_phone': result[0]['contact_phone']
            }
        }

    def all(self):
        with MySQL().session() as s:
            result = s.query(
                UserDEF.id
                , UserDEF.full_name
                , UserDEF.display_name
                , UserDEF.email
                , UserDEF.contact_phone
            ).all()
        result = [r._asdict() for r in result]
        
        return {
            'status_code': 200
            , 'users': result
        }

    def create(self, user):
        try:
            with MySQL().session() as s:

                result = s.query(UserDEF).where(UserDEF.email==user.email).all()
                if len(result)>0:
                    return {
                        'status_code': 409
                        , 'message': f'Não foi possível criar usuário {user.full_name}. E-mail {user.email} já cadastrado.'
                        , 'user': {
                            'full_name': user.full_name
                            , 'display_name': user.display_name
                            , 'email': user.email
                            , 'contact_phone': user.contact_phone
                        }
                    }
                userInsert = UserDEF()

                userInsert.full_name = user.full_name
                userInsert.display_name = user.display_name
                userInsert.email = user.email
                userInsert.contact_phone = user.contact_phone
                
                s.add(userInsert)
                s.commit()
            return {
                'status_code': 200
                , 'message': f'Usuário {user.full_name} criado com sucesso.'
                , 'user': {
                    'full_name': user.full_name
                    , 'display_name': user.display_name
                    , 'email': user.email
                    , 'contact_phone': user.contact_phone
                }
            }
        except Exception as e:
            print(e)
