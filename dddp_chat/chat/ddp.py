"""Django DDP Chat API."""
from __future__ import unicode_literals

from django.contrib.auth import models as auth
from dddp.api import API, Collection, Publication, api_endpoint

from dddp_chat.chat import models as chat


class Room(Collection):
    model = chat.Room
    def serialize(self, obj, meteor_ds):
        return {
            'collection': 'chat.room',
            'id': obj.aid,
            'fields': {
                'slug': obj.slug,
                'title': obj.title,
            },
        }

    #user_rel = [
    #    'participant__user',
    #]

    @api_endpoint
    def new(self, slug, title, public):
        self.model.objects.create(
            slug=slug, title=title, public=public,
        )


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


class PublicRooms(Publication):
    queries = [
        chat.Room.objects.filter(public=True),
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
    PublicRooms, RoomRelated,
])
