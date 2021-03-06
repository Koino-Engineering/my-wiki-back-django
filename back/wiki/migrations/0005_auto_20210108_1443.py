# Generated by Django 3.1.4 on 2021-01-08 14:43

from django.conf import settings
from django.db import migrations, models
import utils.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wiki', '0004_auto_20210107_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='delete_user',
            field=models.ForeignKey(editable=False, null=True, on_delete=models.SET(utils.models.get_sentinel_user), related_name='delete_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='article',
            name='deleted_at',
            field=models.DateTimeField(editable=False, null=True),
        ),
    ]
