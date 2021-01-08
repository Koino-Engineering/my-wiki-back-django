from django.db import models
from utils.models import BaseModel
# Create your models here.


class Article(BaseModel):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)

    class Meta:
        models.UniqueConstraint(
            fields=['title', 'deleted_at'], name='unique_booking')
