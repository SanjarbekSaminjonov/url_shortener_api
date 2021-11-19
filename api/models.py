from django.db import models
from uuid import uuid4

# Create your models here.


class Url(models.Model):
    link = models.CharField(max_length=1500)
    uuid = models.CharField(max_length=20, blank=True)

    def add_uuid(self):
        new_id = str(uuid4())[:5]
        print(new_id)
        self.uuid = new_id

    def get_link(self):
        return self.link

    def __str__(self):
        return self.uuid
