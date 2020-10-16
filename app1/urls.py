from app1.views import (
    UsersRetrieveUpdateDestroyView,
    ItemsRetrieveUpdateDestroyView,
    UsersListCreateView,
    ItemsListCreateView,
)


def add_urls(app):
    app.router.add_view("/users", UsersListCreateView)
    app.router.add_view("/users/{id}", UsersRetrieveUpdateDestroyView)
    app.router.add_view("/items", ItemsListCreateView)
    app.router.add_view("/items/{id}", ItemsRetrieveUpdateDestroyView)
