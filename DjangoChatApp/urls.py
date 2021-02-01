from django.urls import path
from .views import *
urlpatterns = [
    path("", index, name="home"),
    path("account_view/<user_id>/", account_view, name="account_view"),
]

