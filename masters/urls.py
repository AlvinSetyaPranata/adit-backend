from django.urls import path
from .views import ReligionList, ReligionDetail
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('religions/', ReligionList.as_view(), name='Religions'),
    path('religions/<int:pk>/', ReligionDetail.as_view(), name='Religion'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
