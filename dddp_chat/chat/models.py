"""Django DDP Chat models."""
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from dddp.models import AleaIdField


@python_2_unicode_compatible
class Room(models.Model):
    aid = AleaIdField(primary_key=True)
    slug = models.SlugField(max_length=50, unique=True)
    title = models.CharField(max_length=255)
    public = models.BooleanField(default=False)

    def __str__(self):
        return self.slug


@python_2_unicode_compatible
class Participant(models.Model):
    aid = AleaIdField(primary_key=True)
    room = models.ForeignKey('chat.Room', db_index=True)
    user = models.ForeignKey('auth.User', db_index=True)
    owner = models.BooleanField(default=False)
    present = models.BooleanField(default=False)

    def __str__(self):
        return '%s@%s' % (self.user, self.room)

    class Meta:
        unique_together = [
            ['room', 'user'],
        ]


@python_2_unicode_compatible
class Message(models.Model):
    aid = AleaIdField(primary_key=True)
    room = models.ForeignKey('chat.Room', db_index=True)
    user = models.ForeignKey('auth.User', db_index=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    updated = models.DateTimeField(auto_now=True)
    message = models.CharField(max_length=1000)

    def __str__(self):
        return '%s [%s] %s' % (self.room, self.created, self.user)

    class Meta:
        ordering = ['-created']
