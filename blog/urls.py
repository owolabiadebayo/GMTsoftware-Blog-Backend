from django.urls import path
from blog import views

urlpatterns = [
      path('All_category/',
        views.AllCategoryList.as_view(),
        name=views.AllCategoryList.name),
    path('All_category/<int:pk>',
        views.AllcategoryDetail.as_view(),
        name=views.AllcategoryDetail.name),
    path('Each_category/',
        views.EachCategoryList.as_view(),
        name=views.EachCategoryList.name),
    path('Each_category/<int:pk>',
        views.EachcategoryDetail.as_view(),
        name=views.EachcategoryDetail.name),
    path('',
        views.ApiRoot.as_view(),
        name=views.ApiRoot.name),
]