from django.db import models

# Create your models here.
class uid(models.Model):
    uid = models.CharField(max_length=30)
    reference_type = models.CharField(max_length=30)
    origin = models.CharField(max_length=30, default='tgac')