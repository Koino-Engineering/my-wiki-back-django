from rest_framework import viewsets
from rest_framework import permissions
from wiki.serializers import ArticleSerializer
from wiki.models import Article

# Create your views here.


class ArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Article.objects.all().order_by('-created_at')
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated]
