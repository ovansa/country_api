from django.urls import path
from country import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('country/', views.CountryList.as_view()),
    path('country/<str:pk>', views.CountryDetail.as_view()),
    path('state/', views.StateList.as_view()),
    path('city/', views.CityList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
