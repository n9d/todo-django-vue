from django.db import models

class Item(models.Model):
    task = models.CharField(
        blank = False,
        null = False,
        default = "no title",
        max_length = 100,
    )
    done = models.BooleanField(
        default = False,
    )
    deleted = models.BooleanField(
        default = False,
    )
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
