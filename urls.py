from views import create_user


def add_urls(app):
    app.router.add_post('/user', create_user)
