from django.db import models


class Job(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=100)
    By = models.CharField(max_length=50, default=None)
    title = models.CharField(max_length=255, default=None, null=False)

