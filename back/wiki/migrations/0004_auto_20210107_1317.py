# Generated by Django 3.1.4 on 2021-01-07 13:17

from django.conf import settings
from django.db import migrations, models
import django_currentuser.db.models.fields
import django_currentuser.middleware
import utils.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wiki', '0003_auto_20210107_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='delete_user',
            field=django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, editable=False, null=True, on_delete=models.SET(utils.models.get_sentinel_user), related_name='delete_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
