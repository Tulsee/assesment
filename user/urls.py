from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token

from . import views

from rest_framework.routers import DefaultRouter
# router = DefaultRouter()
# router.register('register', views.UserRegistrationViewSet, basename='register')

urlpatterns = [
    # path('', include(router.urls)),
    path('', views.UserRegistrationViewSet.as_view()),
    path('login/', obtain_jwt_token, name='token_obtain_pair'),
]
