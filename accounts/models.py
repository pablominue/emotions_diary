from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
import uuid

class Emotion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    emotion = models.CharField(max_length=50)
    intensity = models.IntegerField(choices=[(i, i) for i in range(1, 11)], default=5)  # Escala del 1 al 10
    note = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.emotion}'

    class Meta:
        ordering = ['-timestamp']