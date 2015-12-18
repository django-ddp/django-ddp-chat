"""Django DDP Chat API."""
from __future__ import unicode_literals

from django.contrib.auth import models as auth
from dddp.api import API, Collection, Publication

from dddp_chat.chat import models as chat


class Room(Collection):
    model = chat.Room
    user_rel = [
        'participant__user',
    ]


class User(Collection):
    model = auth.User


class Participant(Collection):
    model = chat.Participant
    user_rel = [
        'room__participant__user',
    ]


class Message(Collection):
    model = chat.Message
    user_rel = [
        'room__participant__user',
    ]


class RoomRelated(Publication):
    @staticmethod
    def get_queries(room_slug):
        yield chat.Room.objects.filter(slug=room_slug)
        yield auth.User.objects.filter(participant__room__slug=room_slug)
        yield chat.Participant.objects.filter(room__slug=room_slug)
        yield chat.Message.objects.filter(room__slug=room_slug)


API.register([
    Room, User, Participant, Message,
    RoomRelated,
])
