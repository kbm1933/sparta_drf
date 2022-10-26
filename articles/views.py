from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from articles.serializers import ArticleSerializer
from articles.models import Article
from django.shortcuts import get_object_or_404
# Create your views here.

class ArticleList(APIView):
    def get(self,request,format=None):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles,many = True)
        return Response(serializer.data)
    
    def post(self, request,format=None):
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



class Article_detail_view(APIView):
    def get(self,request,article_id,format=None):
        article = get_object_or_404(Article,id=article_id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    def put(self,request,article_id,format=None):
        article = get_object_or_404(Article,id=article_id)
        serializer = ArticleSerializer(article,data = request.data) #article의 데이터를 새로 바꿔준다.
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,article_id,format=None):
        article = get_object_or_404(Article,id=article_id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)