import logging

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django_currentuser.db.models import CurrentUserField
from django_currentuser.middleware import get_current_authenticated_user

# Create your models here.


def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    create_user = CurrentUserField(
        editable=False,
        on_delete=models.SET(get_sentinel_user),
        related_name="create_user"
    )
    updated_at = models.DateTimeField(auto_now=True)
    update_user = CurrentUserField(
        editable=False,
        on_delete=models.SET(get_sentinel_user),
        related_name="update_user"
    )
    deleted_at = models.DateTimeField(null=True,editable=False)
    delete_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        editable=False,
        null=True,
        on_delete=models.SET(get_sentinel_user),
        related_name="delete_user",
    )

    def save(self, *args, **kwargs):
        logging.debug("save " + str(self.deleted_at))
        self.update_user = get_current_authenticated_user()
        super(BaseModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.deleted_at = timezone.now()
        self.delete_user = get_current_authenticated_user()
        super(BaseModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True
