from aiohttp import web
from app1.app import create_app
import argparse
from app1.settings import load_config
from aiohttp_rest_framework import setup_rest_framework

parser = argparse.ArgumentParser()
parser.add_argument('--host', help="Host to listen", default="127.0.0.0")
parser.add_argument('--port', help="Port to accept connections", default=8000)


args = parser.parse_args()

app = create_app(load_config())
setup_rest_framework(app)

if __name__ == '__main__':
    web.run_app(app,)
