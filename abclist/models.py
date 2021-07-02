from django.db import models
from json import JSONEncoder, JSONDecoder

class ABCList(models.Model):
    user = models.CharField(max_length=255)
    abclist = models.JSONField(encoder=JSONEncoder, decoder=JSONDecoder)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return str(self.user) + 's List: ' + str(self.abclist)
