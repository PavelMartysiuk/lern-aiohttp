import aiohttp
import asyncio
import json

from app1.tables import engine, users

from sqlalchemy import select

from faker import Faker

import pytest


class Tests:
    def __init__(self):
        self.data = {
            "user_id": 111872,
            "user_name": "Pahs",
            "last_user_name": "GGsssssddxddx"
        }
        self.conn = engine.connect()

    async def fetch(self, session, url, data, method):
        if method == 'post':
            async with session.post(url, data=data) as response:
                return await response.text()
        elif method == 'get':
            async with session.get(url) as response:
                return await response.text()

    async def response(self, url, method):
        async with aiohttp.ClientSession() as session:
            response = await self.fetch(session, url, json.dumps(self.data), method)
            return response

    def delete_test_data_from_db(self):
        self.conn.execute(users.delete().where(users.c.user_id == self.data['user_id']))

    def create_test_data_in_db(self):
        self.conn.execute(users.insert().values(**self.data))

    def select_test_data_from_db(self):
        query = select([users]).where(users.c.user_id == self.data['user_id'])
        result = self.conn.execute(query).fetchone()
        check_response = {
            'id': result['id'],
            'user_id': result['user_id'],
            'user_name': result['user_name'],
            'last_user_name': result['last_user_name']
        }
        return check_response

    async def test_post(self):
        method = 'post'
        url = 'http://0.0.0.0:8080/users'
        response = await self.response(url, method)
        check_response = json.dumps(self.select_test_data_from_db())
        self.delete_test_data_from_db()
        print(response)
        print(check_response)
        assert response == check_response

    async def test_get(self):
        method = 'get'
        self.create_test_data_in_db()
        check_response = self.select_test_data_from_db()
        user_id = check_response['id']
        url = f'http://0.0.0.0:8080/users/{user_id}'
        response = self.response(url, method)
        print(response)

    def run_tests(self):
        ioloop = asyncio.get_event_loop()
        tasks = [self.test_post(), self.test_get()]
        ioloop.run_until_complete(asyncio.wait(tasks))
        ioloop.close()


if __name__ == '__main__':
    tests = Tests()
    tests.run_tests()
