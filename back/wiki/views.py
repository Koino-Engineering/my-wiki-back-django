from rest_framework import permissions, viewsets
from rest_framework.authentication import SessionAuthentication, TokenAuthentication

from wiki.models import Article
from wiki.serializers import ArticleSerializer

# Create your views here.


class ArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    queryset = Article.objects.all().order_by('-created_at')
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated]
