from django.urls import path
from .views import ParentList, ParentDetail

urlpatterns = [
    path('parent/', ParentList.as_view(), name='parentlist'),
    path('parent/<int:pk>/', ParentDetail.as_view(), name='parentdetail'),
]