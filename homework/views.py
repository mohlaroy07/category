from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Category 


class IndexApiView(APIView):
    def get(self, request: Request):
        categories = Category.objects.all()
        
        new_categories = []
        for category in categories:
            new_categories.append({
                "name": category.name,
            })
        return Response("categories")



