from views import create_user, update_user, delete_user, retrieve_user


def add_urls(app):
    app.router.add_post('/user', create_user)
    app.router.add_put('/user', update_user)
    app.router.add_delete('/user', delete_user)
    app.router.add_get('/user', retrieve_user)