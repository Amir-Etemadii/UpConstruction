from django.db import models

class ActivePostManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=True)

    def active_count(self):
        return self.get_queryset().count()