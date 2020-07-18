from django.urls import path, include

# from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

from country import views


router = DefaultRouter()
router.register('country', views.CountryViewSet)
router.register('state', views.StateViewSet)
router.register('city', views.CityViewSet)

app_name = 'country'

urlpatterns = [
    path('', include(router.urls)),

    # -----------------------------------------------------
    # Based on APIViews

    # path('country/', views.CountryList.as_view()),
    # path('country/<str:pk>', views.CountryDetail.as_view()),
    # path('state/', views.StateList.as_view()),
    # path('city/', views.CityList.as_view()),

    # -----------------------------------------------------
]

# urlpatterns = format_suffix_patterns(urlpatterns)
