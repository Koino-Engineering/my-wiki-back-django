from utils.serializers import BaseModelSerializer
from wiki.models import Article
from rest_framework import serializers


class ArticleSerializer(BaseModelSerializer):
    description = serializers.CharField(
        max_length=1000,
        style={'base_template': 'textarea.html', 'rows': 10}
    )

    class Meta:
        model = Article
        fields = '__all__'
