from db_context_manager import connect

from tables import User

from aiohttp.web import Response

import json

from sqlalchemy.exc import IntegrityError


def save_user(user, sess):
    try:
        new_user = User(**user)
        sess.add(new_user)
        sess.commit()
    except TypeError:
        return False
    except IntegrityError:
        sess.rollback()
        return False
    return True


async def create_user(request):
    user = await request.json()
    with connect() as sess:
        if save_user(user,sess):
            response = sess.query(User).filter(User.user_id == user['user_id']).first().to_dict()
            return Response(text=json.dumps(response), status=200)
        return Response(text=json.dumps({'bad request':'invalid data'}), status=401)
