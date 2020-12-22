
from django.urls import path

from main.views import game

urlpatterns = [
    path('', game.guess_game),
]