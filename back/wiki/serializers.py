from utils.serializers import BaseModelSerializer
from wiki.models import Article


class ArticleSerializer(BaseModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
