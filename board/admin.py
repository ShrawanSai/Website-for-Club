from django.contrib import admin
from .models import BoardMember, Event


# Register your models here.
admin.site.register(BoardMember)
admin.site.register(Event)
