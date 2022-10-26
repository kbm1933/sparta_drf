from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from articles.serializers import ArticleSerializer
from articles.models import Article
from django.shortcuts import get_object_or_404
# Create your views here.
@api_view(['GET','POST'])
def index(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles,many = True)
        return Response(serializer.data)
    #post요청 처리
    if request.method == 'POST':
        serializer = ArticleSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            #개발할땐 상관없지만 서비스할때는 보안상의 이유로 비추
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        # #검증
        # serializer.is_valid(raise_exception=True) #검증 단계에서 문제가 있을 경우 에러 발생
        # #생성
        # serializer.save() # 검증 단계에서 문제가 없을 경우 데이터 저장
        # return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
def article_view(request,article_id):
    if request.method == 'GET':
        article = get_object_or_404(Article,id=article_id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    if request.method == 'PUT':
        article = get_object_or_404(Article,id=article_id)
        serializer = ArticleSerializer(article,data = request.data) #article의 데이터를 새로 바꿔준다.
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    if request.method == 'DELETE':
        article = get_object_or_404(Article,id=article_id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)