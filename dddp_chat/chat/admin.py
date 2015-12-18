from django.contrib import admin
from dddp_chat.chat import models as chat

admin.site.register(chat.Room)
admin.site.register(chat.Participant)
admin.site.register(chat.Message)
