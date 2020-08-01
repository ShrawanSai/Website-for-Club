from django.db import models

class BoardMember(models.Model):
    board_title = models.CharField(max_length=100)
    board_member_name = models.CharField(max_length=100)
    position_value = models.IntegerField()
    image = models.ImageField(upload_to='board/media')

    def __str__(self):
        return self.board_title


class Event(models.Model):
    event_title = models.CharField(max_length=100)
    event_subtitle = models.CharField(max_length=100)
    event_desc = models.TextField(max_length=1000)
    event_image = models.ImageField(upload_to='board/media')

    def __str__(self):
        return self.event_title

    
    



