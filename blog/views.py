from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.reverse import reverse
from blog.models import EachCategory
from blog.models import AllCategory
from blog.serializers import AllCategorySerializer,EachCategorySerializer

class AllCategoryList(generics.ListCreateAPIView):
    queryset = AllCategory.objects.all()
    serializer_class = AllCategorySerializer
    name = 'all-category'
    filter_fields = (
      'name',
      )
    search_fields = (
      'name',
      )
    ordering_fields = (
      'name',
      )
class AllcategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AllCategory.objects.all()
    serializer_class = AllCategorySerializer
    name = 'allcategory-detail'
    filter_fields = (
      'Course',
      )
    search_fields = (
      'Course',
      )
    ordering_fields = (
      'Course',
      )
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(instance)
        print(serializer.data)
        return Response(serializer.data)
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status= status.HTTP_204_NO_CONTENT)
class EachCategoryList(generics.ListCreateAPIView):
    queryset = EachCategory.objects.all()
    serializer_class = EachCategorySerializer
    name = 'each-category'
    filter_fields = (
      'Course',
      )
    search_fields = (
      'Course',
      )

class EachcategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EachCategory.objects.all()
    serializer_class = EachCategorySerializer
    name = 'eachcategory-detail'
    filter_fields = (
      'Course',
      'category'
      )
    search_fields = (
      'Course',
      'Title'
      )
    ordering_fields = (
      'Start_date',
    )
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(instance)
        print(serializer.data)
        return Response(serializer.data)
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status= status.HTTP_204_NO_CONTENT)
class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self,request,*args,**kwargs):
        return Response({
            'all-category':reverse(AllCategoryList.name,request=request),
            'blog-details':reverse(EachCategoryList.name,request=request),
            })