from django.urls import path
from .views import RegisterAPIView,LoginAPIView,ChangePasswordAPIView

urlpatterns = [
    path('api/register/', RegisterAPIView.as_view(), name='api-register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('change-password/', ChangePasswordAPIView.as_view(), name='change_password'),

]