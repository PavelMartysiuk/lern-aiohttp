from task1.view import calculate


def add_urls(app):
    app.router.add_post('/', calculate)
