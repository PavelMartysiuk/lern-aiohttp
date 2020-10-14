from db_context_manager import connect

from tables import User

from aiohttp.web import Response

import json

from sqlalchemy.exc import IntegrityError


def save_user(user, sess):
    try:
        new_user = User(**user)
        sess.add(new_user)
        sess.flush()
    except TypeError:
        return False
    except IntegrityError:
        return False
    else:
        sess.commit()
        return True


async def create_user(request):
    user = await request.json()
    with connect() as sess:
        if save_user(user, sess):
            response = sess.query(User).filter(User.user_id == user['user_id']).first().to_dict()
            return Response(text=json.dumps(response), status=200)
        return Response(text=json.dumps({'bad request': 'invalid data'}), status=401)


async def update_user(request):
    user = await request.json()
    user_id = user['user_id']
    with connect() as sess:
        sess.query(User).filter(User.user_id == user_id).update(user)
        sess.commit()
        response = sess.query(User).filter(User.user_id == user_id).first().to_dict()
        return Response(text=json.dumps(response), status=200)


async def delete_user(request):
    user = await request.json()
    user_id = user['user_id']
    with connect() as sess:
        sess.query(User).filter(User.user_id == user_id).delete()
        sess.commit()
        return Response(text=json.dumps({'delete': 'success'}), status=201)


async def retrieve_user(request):
    user_id = request.query['id']
    with connect() as sess:
        try:
            users = sess.query(User).filter(User.id == user_id).first().to_dict()
        except AttributeError:
            return Response(text=json.dumps({'error': 'user not found'}), status=401)
        return Response(text=json.dumps(users), status=201)
