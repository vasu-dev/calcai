from django.urls import path
from .views import FacePlusAPIView

urlpatterns = [
    path('faceplus/', FacePlusAPIView.as_view(), name='faceplus'),

]