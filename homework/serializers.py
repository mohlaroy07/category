from rest_framework.serializers import ModelSerializer

from .models import Article, Category, Comment


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
