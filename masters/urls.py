from django.urls import path
from .views import ReligionList, ReligionDetail, GenderList, GenderDetail, CitizenList, CitizenDetail
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('religions/', ReligionList.as_view(), name='Religions'),
    path('religions/<int:pk>/', ReligionDetail.as_view(), name='Religion'),
    path('genders/', GenderList.as_view(), name='Genders'),
    path('genders/<int:pk>', GenderDetail.as_view(), name='Genders'),
    path('citizens/', CitizenList.as_view(), name='Citizens'),
    path('citizens/<int:pk>', CitizenDetail.as_view(), name='Citizens')
]

urlpatterns = format_suffix_patterns(urlpatterns)
