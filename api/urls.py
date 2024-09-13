from django.urls import path
from .views import ParcelAPIView, DetailAPIView, PNRList, PNRDelete
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('<int:pk>/', DetailAPIView.as_view()),
    path('', ParcelAPIView.as_view()),
    path("pnr/", PNRList.as_view()),
    path("pnr/<str:pnr_number>/", PNRDelete.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)