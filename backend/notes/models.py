from django.db import models

from user.models import User


class Note(models.Model):
    body = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.body[:50]

    def delete(self):
        self.deleted = True
        super(Note, self).delete()

